from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Product

class HomePage(LoginRequiredMixin,TemplateView):
    data = Product.objects.all()
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            data= self.data.all()
            return render(request,'index.html',{'datas':data})

