from django.shortcuts import render
from django.views import View
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
