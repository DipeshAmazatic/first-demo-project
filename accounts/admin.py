from django.contrib import admin
from .user_admin import CustomUserAdmin
from .models import CustomUser,Company,Product,ProductVariants,ProductSpecification

# Register your models here


admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Company)
admin.site.register(Product)
admin.site.register(ProductVariants)
admin.site.register(ProductSpecification)
