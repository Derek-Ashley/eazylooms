from django.contrib import admin
from .models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

admin.site.register(
    [Admin, Customer, Category, Product, Cart, CartProduct, Order, ContactForm,ProductImage])
