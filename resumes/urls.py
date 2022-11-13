from django.urls import path
from . import views


urlpatterns = [
    path("resumes/<int:pk>", views.resume_view, name="resume_view"),
    path("resumes", views.resumes, name="resumes"),
]
