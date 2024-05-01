from django.urls import path
from .views import *

urlpatterns = [
    path('executor/', ExecutorView.as_view(), name='executor_list'),
    path('customer/', CustomerUserView.as_view(), name='customer_list'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer_reply'),
    path('customer/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/edit/<int:pk>/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),
    path('reply/<int:pk_post>/', ReplyCreateView.as_view(), name='reply_create'),
]
