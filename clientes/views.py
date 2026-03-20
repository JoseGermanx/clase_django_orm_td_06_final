from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente
from django.contrib import messages

from django.urls import reverse_lazy

# Create your views here.

class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'clientes'

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    fields = ['nombre', 'apellido', 'edad', 'correo', 'telefono', 'activo']
    success_url = reverse_lazy('cliente_list')

    def form_valid(self, form):
        messages.success(self.request,"Cliente creado correctamente.")
        return super().form_valid(form)

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    fields = ['nombre', 'apellido', 'edad', 'correo', 'telefono', 'activo']
    success_url = reverse_lazy('cliente_list')

    def form_valid(self, form):
        messages.success(self.request,"Cliente actualizado correctamente.")
        return super().form_valid(form)

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, "Cliente eliminado correctamente.")
        return super().post(request, *args, **kwargs)

       