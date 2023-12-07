from django.urls import path
from . import views
from .views import run_python_script

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:train_id>", views.train, name="train"),
    path("<int:train_id>/book", views.book, name="book"),
    path('run_python_script/', run_python_script, name='run_python_script'),
]
