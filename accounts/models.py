from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager

class CustomUser(AbstractUser):
    username = models.CharField(
        _('username'),
        max_length=150,
        blank=True,
        null=True
    )
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30,unique=True)
    phone_no = models.CharField(max_length=10,unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.email)

class Company(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return str(str(self.company)+' '+self.name)

class ProductVariants(models.Model):
    rating_choice = [
                ('1', 1),
                ('2', 2),
                ('3', 3),
                ('4', 4),
                ('5', 5),
    ]
    product = models.ForeignKey(Product,on_delete=models.CASCADE)#related_name='productvariants',
    name = models.CharField(max_length=100,null=False,blank=False)
    description = models.CharField(max_length=100,null=False,blank=False)
    variant_type = models.CharField(max_length=100,null=False,blank=False)
    price = models.DecimalField(max_digits=100,decimal_places=4)
    feature = models.CharField(max_length=200,null=False,blank=False)
    rating = models.CharField(max_length=11,choices=rating_choice)

    def __str__(self):
        return str(str(self.product)+' '+self.variant_type)

class ProductSpecification(models.Model):
    variant = models.OneToOneField(ProductVariants,on_delete=models.CASCADE)#related_name='productspecifications'
    specification_details = models.CharField(max_length=200,null=False,blank=False)

    def __str__(self):
        return self.specification_details
