from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from car.models import *


#=======================================================================
class MakeListView(ListView):

    model = Make

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


#=======================================================================
class CarListView(ListView):
  
    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

#=======================================================================
class CarDetailView(DetailView):

    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

#=======================================================================
