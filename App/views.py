from email import message
from multiprocessing import context
from django.shortcuts import render
from .forms import CandidateForm
from django.http import HttpResponseRedirect
from django.contrib import messages




def home(request):
    if request.method == "POST":
        
        form =CandidateForm(request.POST,request.FILES)
        print(request.POST)
        if form.is_valid():
            print("es valido")
            form.save()
            messages.success(request, "Registered Successfully !")
            return HttpResponseRedirect('/')
        else:
            return render(request, "home.html", {'form':form})
    else:
        form= CandidateForm()
        return render(request, "home.html", {'form':form})