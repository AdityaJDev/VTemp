from django.urls import path

from . import views

app_name = "blogs"
urlpatterns = [
    path("", views.BlogsListView.as_view(), name="home"),
    path("insert/", views.BlogFormView.as_view(), name="addition"),
]
