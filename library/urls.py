from django.urls import path

from . import views

app_name = "books"
urlpatterns = [
    path("", views.LibView.as_view(), name="library"),
    path("<str:pk>/", views.SelectView.as_view(), name="select"),
]
