from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('executor/', ExecutorView.as_view(), name='executor_list'),
    path('customer/', CustomerUserView.as_view(), name='customer_list'),
    path('customer/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/edit/<int:pk>/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),
    path('login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'), name='signup'),
]
