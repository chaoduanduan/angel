from django.contrib import admin

# Register your models here.
from .models import Product,ProductImage,CarModel,CarInfo,CarImage,ModelImage

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ['make','vin_number','mileage']
    list_display = ['make','vin_number','mileage']   
    list_filter = ['mileage']
    readonly_fields = ['updated','timestamp']    
    class Meta:
        model = Product
class CarInfoAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ['model','price','exterior_color','interior_color']
    list_display = ['vin_number','model','exterior_color','interior_color','price','updated']
    list_editable = ['price',]
    list_filter = ['price','exterior_color']
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {"slug":("model","vin_number")}
    class Meta:
        model = CarInfo
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(CarModel)
admin.site.register(CarInfo,CarInfoAdmin)
admin.site.register(CarImage)
admin.site.register(ModelImage)