from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'accounts'

urlpatterns = [
    path("login/", views.LoginViewPage.as_view(template_name="accounts/login.html"),name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('product-type/',views.add_new_product,name='product-type'),
    path('product-variant/',views.add_product_variant,name='product-variant'),
    path('product-specification/',views.add_product_specification,name='product-specification'),
    path('password-reset/',views.EmailPasswordResetView.as_view(),name='password-reset'),
    path('password-reset/done/',views.EmailPasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',views.EmailPasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/complete/',views.EmailPasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('<id>/variant/delete/',views.delete_variant,name='delete-variant'),
    path("<id>/delete/", views.delete_product, name="delete"),
    path('<id>/',views.show_data,name='show-data'),
    path('<id>/update/',views.edit_variant,name='update-variant'),
    
]
