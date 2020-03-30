from django.urls import reverse_lazy

from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm
from django.views.generic import (ListView,
                                  UpdateView,
                                  DeleteView,
                                  CreateView)

# Create your views here.

class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
# A estrutura abaixo indica que RegistroHoraExta por funcionario
# E funcionario pertence a uma empresa, que é representado pelo "__"
        queryset = RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
        return queryset


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')

class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

# É desta forma que é injetado o usuário logado "user" para o formulário HoraExtraCreate
# que será remodelado no novo formulário form-class = RegistroHoraExtraForm
# form_class é o formulário inicial do django mas que foi alterado
    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs