from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from accounts.models import (Company, Product, 
                                ProductSpecification, ProductVariants)
from django.db.models import Q
User = get_user_model()

class UserCreateForm(UserCreationForm):
    name = forms.CharField()
    phone_no = forms.CharField(widget = forms.NumberInput())
    class Meta:
        model = User
        fields = ("name","username", "email", "password1", "password2","phone_no")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["phone_no"].label = "Phone Number"
        self.fields["email"].label = "Email address"


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=request,*args, **kwargs)
        
        self.fields['username'].label = "Email or Phone"


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = "Company Name"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = "Product Type Name"

class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariants
        fields = '__all__'

class ProductSpecificationForm(forms.ModelForm):
    class Meta:
        model = ProductSpecification
        fields = '__all__'


