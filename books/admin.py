from django.contrib import admin
from .models import Book, Order


admin.site.register(Book)
admin.site.register(Order) 
admin.site.site_header = 'Storebooks Admin Panel'
admin.site.site_title = 'storebooks'


