from django.views import generic
from .forms import DayCreateForm
from .models import Day
from django.urls import reverse_lazy

class IndexView(generic.ListView):
        model = Day


class AddView(generic.CreateView):
        model = Day
        form_class = DayCreateForm
        success_url = reverse_lazy('diary:index') # /diary/


class UpdateView(generic.UpdateView):
        model = Day
        form_class = DayCreateForm
        success_url = reverse_lazy('diary:index') # /diary/


class DeleteView(generic.DeleteView):
        model = Day
        success_url = reverse_lazy('diary:index') # /diary/


class DetailView(generic.DetailView):
        model = Day
