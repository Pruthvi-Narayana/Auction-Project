from django.shortcuts import *
from .models import *
from django.contrib import messages
from itertools import zip_longest
from django.http import JsonResponse
from django.http import HttpResponseBadRequest


# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        gender = request.POST['gender']
        password = request.POST['password']
        email = request.POST['email']
        print(name,phone,gender,password,email)
        customer = Customer.objects.create(name=name,phone=phone,
                                   gender=gender,password=password,email=email)
        messages.success(request, "Account Registed!")

        return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    if request.method == "POST":
        name = request.POST['un']
        password = request.POST['pd']
        customers = Customer.objects.all()
        print(name,password)
        user = Customer.objects.filter(name=name, password=password).first()
        if user:
            return redirect('dashboard')
        else:
            messages.error(request, "Password incorrect , Try Again...")
            # return HttpResponse("<h3>Password is incorrect.</h3>")
    return render(request,'signin.html')

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)
def dashboard(request):
    products = Product.objects.all()
    # Chunk the products into groups of 4 for the carousel
    chunked_products = list(grouper(products, 4))
    return render(request, 'dashboard.html', {'x': chunked_products})


def sellpage(request):
    if request.method == "POST":
        pname = request.POST['productName']
        pprice = request.POST['productPrice']
        pdec = request.POST['productDescription']
        pimage = request.FILES['productImage']
        product = Product.objects.create(productName=pname,productPrice=pprice,productDescription=pdec,
                                         productImage=pimage)
        return redirect('dashboard')
    return render(request,'sellpage.html')

def showuser(request):
    customers = Customer.objects.all()
    return render(request,'showuser.html',{'x':customers})

def showproducts(request):
    products = Product.objects.all()
    return render(request,'showproducts.html',{'x':products})

def logout_view(request):
    return redirect('signin')

def feedback(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        feedback  = request.POST['feedback']
        f = Feedback.objects.create(name=name,email=email,feedback=feedback)
    feed = Feedback.objects.all()
    return render(request,'feedback.html',{'feed':feed})

def product_view(request):
    return render(request,'done.html',)

def done(request):
    return render(request,'done.html')

def delete(request, id):
        dele = Product.objects.get(id=id)
        dele.delete()
        messages.success(request, "Item Deleted")
        return redirect('showproducts')

# Updated view without URL parameters
def update_bid(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        bid_amount = request.POST.get('bid_amount')

        # Ensure product_id and bid_amount are valid
        if product_id is None or bid_amount is None:
            messages.success(request, "Invalid Input")

        # Retrieve the product object
        item = Product.objects.get(id=product_id)
        item_curr = item.highestbid

        # Convert bid_amount to an integer
        try:
            item_new = int(bid_amount)
        except ValueError:
            messages.success(request, "Invalid Input")
            return redirect('dashboard')

        # Update the highest bid if the new bid is greater
        if item_curr < item_new:
            item.highestbid = item_new
            item.save()
            messages.success(request, "New Bid Updated")

        else:
            messages.success(request, "New bid must be greater than the current highest bid")
        return redirect('dashboard')
    else:
        return HttpResponseNotAllowed(['POST'])


# def update_bid(request,id,bid_amount):
#     item = Product.objects.get(id=id)
#     item_curr = item.highestbid
#     # get the Item frm the Text FIELD
#     item_new = bid_amount
#     print(item_curr)
#     if item_curr <= item_new:
#         item.highestbid = item_new
#     else:
#         return HttpResponseBadRequest("New bid must be greater than the current highest bid")
#     return redirect('dashboard')


