from email import message
from multiprocessing import context
from django.shortcuts import render
from .forms import CandidateForm
from .models import Candidate
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required # to access private pages
from django.views.decorators.cache import cache_control # destroy the section after logout


#---------------FRONTEND ---------------------------------#
# Home
def home(request):
    return render(request,"home.html")

# CAndidate registration 
def register(request):
    if request.method == "POST":
        
        form =CandidateForm(request.POST,request.FILES)
        print(request.POST)
        if form.is_valid():
            print("es valido")
            form.save()
            messages.success(request, "Registered Successfully !")
            return HttpResponseRedirect('/')
        else:
            return render(request, "register.html", {'form':form})
    else:
        form= CandidateForm()
        return render(request, "register.html", {'form':form})
    
    
    
#---------------BACKEND ---------------------------------#
# HR - Home Page (backend)
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend(request):
    
    context = {'data_read': Candidate.objects.all()}    
    return render(request,"backend.html", context)

# Acces candidates (individually)
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def candidate(request,id):
    data = Candidate.objects.get(pk=id)
    form = CandidateForm(instance = data)
    # si quiero desabilitar la edicion de datos en el frontend, lo puedo hacer aca de lla siguiente manera
    array= ['experience', 'gender','firstname','image']
    for field in array:
        # deshabilito la edicion del contro
        form.fields[field].disabled=True
        # puedo ocultar un control
        form.fields['image'].widget.attrs.update({'style':'display:none'})
        
    return render(request,'candidate.html',{'form':form})
    # podiria haceer asi
    #context = {'form',data}
    #return render(request,'candidate.html',context)

