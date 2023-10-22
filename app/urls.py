from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import CostumerView, show_cart,Products
from .forms import ChangePasswordForm, Password_ResetForm,ResetConfirm
from .views import plus_button
urlpatterns = [
    path('', views.Products.as_view(), name = 'products'),
    path('product-detail/<int:pk>', views.Product_detail.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name = 'show_cart'),
    path('pluscart/', views.plus_button),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.CostumerView.as_view(), name = 'profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name = 'app/changepassword.html', form_class = ChangePasswordForm,success_url = '/changepassworddone/'), name = 'passwordchange'),
    path('changepassworddone/', auth_views.PasswordChangeView.as_view(template_name = 'app/changepassworddone.html', form_class = ChangePasswordForm), name = 'changepassworddone'),
    path('passwordreset/', auth_views.PasswordResetView.as_view(template_name = 'app/passwordreset.html', form_class = Password_ResetForm), name = 'passwordreset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'app/password_reset_done.html'), name = 'password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'app/password_reset_confirm.html',form_class = ResetConfirm),name = 'password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'app/password_reset_complete.html'),name = 'password_reset_complete'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.Logout_user.as_view(), name = 'logout'),
    path('registration/', views.RegistrationFormView.as_view(), name='registration'),
    path('checkout/', views.checkout, name='checkout'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
