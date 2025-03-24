from django.contrib import admin
from .models import Product, Order


admin.site.site_header = 'Avix Tecno Shop Admin Area'
admin.site.site_title = 'Avix Tecno Shop'
admin.site.index_title = 'Welcome to the Avix , '

admin.site.register(Product)
admin.site.register(Order)
