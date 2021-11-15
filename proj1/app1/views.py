from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contact

class ContactList(ListView): 
    model = Contact
    template_name = 'app1/contact_list.html'

class ContactDetail(DetailView): 
    model = Contact
    template_name = 'app1/contact_details.html'

class ContactCreate(CreateView): 
    model = Contact
    fields = ['name','email','address','phone']
    template_name = 'app1/contact_form.html'
    success_url = '/fa/contacts'

class ContactUpdate(UpdateView): 
    model = Contact
    fields = ['name','email','address','phone']
    template_name = 'app1/contact_form.html'
    success_url = '/fa/contacts'

class ContactDelete(DeleteView): 
    model = Contact
    template_name = 'app1/contact_confirm_delete.html'
    success_url = '/fa/contacts'

