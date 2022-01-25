from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import Product,ProductVariants
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import(
                                        LoginView,PasswordResetView,PasswordResetDoneView,
                                        PasswordResetConfirmView,PasswordResetCompleteView
                                     )

User = get_user_model()

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        messages.success(request,"User Registered Successfully...")
        return response
        
class LoginViewPage(LoginView):
    form_class = forms.UserLoginForm
    success_url = reverse_lazy("home")
    template_name = "accounts/login.html"

class EmailPasswordResetView(PasswordResetView):
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    template_name = 'accounts/password_reset_form.html'
    title = _('Reset your password')

class EmailPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'
    title = _('Password reset sent')

class EmailPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')
    title = _('Enter new password')

class EmailPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
    title = _('Password reset complete')


@login_required
def add_new_product(request):
    if request.method == 'POST':
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"New product added successfully...")
            messages.success(request,"If Do not add new variant then click home button....")
            return redirect('accounts:product-variant')
        return redirect('accounts:product-type')
    form = forms.ProductForm()
    return render(request,'registration/product_form.html',{'form':form})

@login_required
def add_product_variant(request,*args,**kwargs):
    if request.method == 'POST':
        form = forms.ProductVariantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"New variant added successfully...")
            return redirect('accounts:product-specification')
        return redirect('home')
    print(request)
    form = forms.ProductVariantForm()
    return render(request,'registration/product_variants_form.html',{'form':form})

@login_required
def add_product_specification(request):
    if request.method == 'POST':
        form = forms.ProductSpecificationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Added successfully...")
            return redirect('home')
        return redirect('accounts:product-specification')
    form = forms.ProductSpecificationForm()
    return render(request,'registration/product_specification_form.html',{'form':form})

@login_required
def delete_product(request,id):
    if request.method =="POST":
        try:
            product = Product.objects.get(id=id)
            product.delete()
            messages.success(request,"Deleted successfully...")
            return redirect("home")
        except:
            messages.warning(request,"data doesnt exists....")
            return redirect("home")
    return render(request, "accounts/delete.html", {})

@login_required
def delete_variant(request,id):
    if request.method == 'POST':
        try:
            product = ProductVariants.objects.get(id=id)
            product.delete()
            messages.success(request,"Deleted successfully...")
            return redirect('home')
        except:
            messages.warning(request,"data doesnt exists....")
            return redirect('home')
    return render(request, "accounts/delete.html", {})

@login_required
def show_data(request,id):
    data = ProductVariants.objects.filter(product=id)
    if not data:
        messages.warning(request,"Don't have any Variant...Please add new variant...")
    return render(request, "accounts/particular_details.html", {"variant_info":data,'id':int(id)})

@login_required
def edit_variant(request,id):
    if request.method == 'POST':
        update = get_object_or_404(ProductVariants, id = id)
        form = forms.ProductVariantForm(request.POST,instance=update)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated Successfully...")
            return redirect('home')
        else:
            data = ProductVariants.objects.get(id=int(id))
            form = forms.ProductVariantForm(instance=data)
            return render(request,'registration/edit_variant.html',{'form':form,'data':data})
    data = ProductVariants.objects.get(id=int(id))
    form = forms.ProductVariantForm(instance=data)
    return render(request,'registration/edit_variant.html',{'form':form,'data':data})
