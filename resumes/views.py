from django.shortcuts import render, HttpResponse
from .models import Resume


def resume_view(request, pk):
    resume = Resume.objects.get(id=pk)
    print("hello world")
    return render(request, "resumes/resume.html",{"resume": resume})


def resumes(request):
    resumes = Resume.objects.all()
    return render(request, "resumes/resumes.html", {"resumes": resumes})
