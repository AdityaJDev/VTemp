from django.forms import ModelForm
from blogs.models import *


class AddBlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
