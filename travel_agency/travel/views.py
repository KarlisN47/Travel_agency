from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView, FormView

class BaseView(TemplateView):
    template_name = 'index.html'