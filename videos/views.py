from django.urls import reverse_lazy
from django.views import generic
from .forms import VideoCreateForm
from .models import Video


class IndexView(generic.ListView):
    model = Video
    paginate_by = 2


class CreateView(generic.CreateView):
    model = Video
    form_class = VideoCreateForm
    success_url = reverse_lazy('videos:index')


class PlayView(generic.DetailView):
    model = Video
