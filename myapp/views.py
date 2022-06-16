from django.shortcuts import render
from myapp.forms import ResumeForm
from django.http import HttpResponseRedirect
from myapp.models import Resume
from django.views import View
# Create your views here.


class HomeView(View):
    def get(self,request):
        fm=ResumeForm()
        candidates=Resume.objects.all()
        return render(request,"myapp/home.html",{"form":fm,"candidates":candidates})

    def post(self,request):
        fm=ResumeForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")


class CandidateView(View):
    def get(self,request,pk):
        print(pk)
        candidate=Resume.objects.get(pk=pk)
        return render(request,"myapp/candidate.html",{"candidate":candidate})