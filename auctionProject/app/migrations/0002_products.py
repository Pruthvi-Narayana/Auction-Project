# Generated by Django 5.0.1 on 2024-03-09 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=255)),
                ('productPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('productDescription', models.TextField()),
            ],
        ),
    ]
