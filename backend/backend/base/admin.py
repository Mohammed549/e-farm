from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Farmer)
admin.site.register(Product)
admin.site.register(FarmProduct)
admin.site.register(AnimalProduct)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(ShipmentCompany)
admin.site.register(DirectDelivery)
admin.site.register(Box)
admin.site.register(BoxDelivery)
