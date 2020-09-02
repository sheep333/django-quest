from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, DetailView, UpdateView

from .forms import HumanForm
from .models import Human


def index(request):
    return HttpResponse("Hello, World!!")


def index_1(request):
    contexts = {
        "greeting": "Hello, World!!"
    }
    return render(request, "earth/index_1.html", contexts)


class Index2View(TemplateView):
    template_name = "earth/index_2.html"


class Index3View(TemplateView):
    template_name = "earth/index_1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["greeting"] = "Hello, World!!"
        return context


class HumanCreateView(CreateView):
    model = Human
    form_class = HumanForm
    success_url = reverse_lazy("earth:index")


class HumanListView(ListView):
    model = Human


class HumanDetailView(DetailView):
    model = Human


class HumanUpdateView(UpdateView):
    model = Human
    form_class = HumanForm
    success_url = reverse_lazy("earth:index")
