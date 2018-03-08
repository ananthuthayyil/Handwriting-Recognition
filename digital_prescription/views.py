from django.shortcuts import render

def home(request):
   return render(request, "home.html", {})
def doc_login(request):
    return render(request,"doc_login.html", {})
def pre_pad(request):
     return render(request,"prescription_pad.html", {})
