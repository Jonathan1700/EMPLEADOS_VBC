"""CRUD de Empleados y Cargos con Vistas Basadas en Clases (VBC)."""
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Cargo, Empleado
from .forms import CargoForm, EmpleadoForm


class HomeView(TemplateView):
    template_name = 'home.html'


# ---------- CRUD Cargos ----------

class CargoListView(ListView):
    model = Cargo
    template_name = 'cargo_list.html'
    context_object_name = 'cargos'


class CargoCreateView(CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'cargo_form.html'
    success_url = reverse_lazy('cargo_list')
    extra_context = {'titulo': 'Registrar cargo'}


class CargoUpdateView(UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'cargo_form.html'
    success_url = reverse_lazy('cargo_list')
    extra_context = {'titulo': 'Editar cargo'}


class CargoDeleteView(DeleteView):
    model = Cargo
    template_name = 'cargo_confirm_delete.html'
    success_url = reverse_lazy('cargo_list')


# ---------- CRUD Empleados ----------

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleado_list.html'
    context_object_name = 'empleados'


class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado_form.html'
    success_url = reverse_lazy('empleado_list')
    extra_context = {'titulo': 'Registrar empleado'}


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado_form.html'
    success_url = reverse_lazy('empleado_list')
    extra_context = {'titulo': 'Editar empleado'}


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado_list')
