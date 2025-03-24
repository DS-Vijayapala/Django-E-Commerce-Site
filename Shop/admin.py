from django.contrib import admin
from .models import Product, Order


admin.site.site_header = 'Avix Tecno Shop Admin Area'
admin.site.site_title = 'Avix Tecno Shop'
admin.site.index_title = 'Welcome to the Avix , '


class ProductAdmin(admin.ModelAdmin):
    """This class is used to customize the admin panel for the Product model"""

    def change_category_to_default(self, request, queryset):
        """This function is used to change the category of the selected products to default"""

        queryset.update(catogaory='default')

    change_category_to_default.short_description = 'Change default category'

    list_display = ('title', 'price', 'discount_price', 'catogaory',)
    search_fields = ('title', 'catogaory',)
    actions = ('change_category_to_default',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
