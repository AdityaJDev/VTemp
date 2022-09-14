from urllib import request
from django.shortcuts import render
from django.views import View, generic
from blogs.forms import AddBlogForm
from blogs.models import *


class BlogsView(View):
    def get(self, request, *args, **kwargs):
        b_id = request.GET.get("blogid", None)
        print(b_id)
        if b_id is not None:
            data = Blog.objects.filter(id=b_id)
        else:
            data = Blog.objects.all()
        return render(request, "blogs/show.html", {"blogs": data})


class BlogsListView(generic.ListView):
    model = Blog
    template_name = "blogs/show.html"

    def get_queryset(self):
        b_id = self.request.GET.get("blogid", None)
        if b_id is not None:
            return Blog.objects.filter(id=b_id)
        else:
            return Blog.objects.all()


class BlogFormView(View):
    def get(self, request):
        form = AddBlogForm()
        return render(request, "blogs/show_form.html", {"form": form})

    def post(self, request):
        message = ""
        form = AddBlogForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = AddBlogForm()
            message = "Data added"
        else:
            form = AddBlogForm()
            message = "Data not added"
        return render(
            request, "blogs/show_form.html", {"form": form, "message": message}
        )
