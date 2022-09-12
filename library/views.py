import pkgutil
from django.shortcuts import render
from django.views import View
from library.models import *


class LibView(View):
    def get(self, request):
        data = Book.objects.all()
        return render(request, "library/display.html", {"data": data})


class SelectView(View):
    def get(self, request, pk):
        auth_name = pk
        data = Book.objects.filter(author__name=auth_name)
        return render(request, "library/display.html", {"data": data})
