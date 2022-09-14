import pkgutil
from django.shortcuts import render
from django.views import View, generic
from library.models import *


class LibView(View):
    def get(self, request):
        data = Book.objects.all()
        return render(request, "library/display.html", {"data": data})


class LibListView(generic.ListView):
    model = Book
    template_name = "library/display.html"

    def get_queryset(self):
        return Book.objects.all()


class SelectView(View):
    def get(self, request, pk):
        auth_name = pk
        data = Book.objects.filter(author__name=auth_name)
        return render(request, "library/display.html", {"data": data})


class SelectDetailView(generic.DetailView):
    model = Book
    template_name = "library/display_detail.html"
