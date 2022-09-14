from django.urls import path

from . import views

app_name = "books"
urlpatterns = [
    path("", views.LibListView.as_view(), name="library"),
    path("<int:pk>/", views.SelectDetailView.as_view(), name="select"),
]
