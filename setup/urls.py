"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from furukawa.views import (
    # === Customer
    CustomerListView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
    # === Contact
    ContactListView,
    ContactCreateView,
    ContactUpdateView,
    ContactDeleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", CustomerListView.as_view(), name="customer_list"),
    path("customer", CustomerListView.as_view(), name="customer_list"),
    path("create", CustomerCreateView.as_view(), name="customer_create"),
    path("update/<int:pk>", CustomerUpdateView.as_view(), name="customer_update"),
    path("delete/<int:pk>", CustomerDeleteView.as_view(), name="customer_delete"),
    path("contact", ContactListView.as_view(), name="contact_list"),
    path("contact/create", ContactCreateView.as_view(), name="contact_create"),
    path("contact/update/<int:pk>", ContactUpdateView.as_view(), name="contact_update"),
    path("contact/delete/<int:pk>", ContactDeleteView.as_view(), name="contact_delete"),
]
