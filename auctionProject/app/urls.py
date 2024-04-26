from django.contrib import admin
from django.urls import path , include
from django.views.generic.base import TemplateView
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',home,name='home'),
    path('signin',signin,name='signin'),
    path('sellpage',sellpage,name='sellpage'),
    path('signup',signup,name='signup'),
    path('dashboard',dashboard,name='dashboard'),
    path('showuser',showuser,name='showuser'),
    path('showproducts',showproducts,name='showproducts'),
    path('logout_view', logout_view, name='logout_view'),
    path('feedback', feedback, name='feedback'),
    path('done', done, name='done'),
    path('delete/<int:id>', delete, name='delete'),
    # path('update_bid/<int:id>/<int:bid_amount>/', update_bid, name='update_bid'),
    path('update_bid/', update_bid, name='update_bid'),

    # path('kpn', TemplateView.as_view(template_name='index.html'), name='index'),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)