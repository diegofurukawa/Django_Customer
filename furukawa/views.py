from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer, Contact
from django.urls import reverse_lazy


# ========== Customer


class CustomerListView(ListView):
    model = Customer


class CustomerCreateView(CreateView):
    model = Customer
    fields = [
        "cName",
        "cPhone",
        "cEmail",
        "cVendedor",
        "cDescription",
        "dContractCreated",
        "nContractDuration",
    ]
    success_url = reverse_lazy("customer_list")


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = [
        "cName",
        "cPhone",
        "cEmail",
        "cVendedor",
        "cDescription",
        "dContractCreated",
        "nContractDuration",
    ]
    success_url = reverse_lazy("customer_list")


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy("customer_list")


# ========== Contact
class ContactListView(ListView):
    model = Contact


class ContactCreateView(CreateView):
    model = Contact
    fields = [
        "idCustomer",
        "cName",
        "cPhone",
        "cEmail",
    ]
    success_url = reverse_lazy("contact_list")


class ContactUpdateView(UpdateView):
    model = Contact
    fields = [
        "idCustomer",
        "cName",
        "cPhone",
        "cEmail",
    ]
    success_url = reverse_lazy("contact_list")


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy("contact_list")
