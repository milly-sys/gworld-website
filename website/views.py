from django.shortcuts import render

def home(request):
    return render(request,'website/index.html')

def about(request):
    return render(request,'website/about.html')

def services(request):
    return render(request,'website/services.html')

def company_profile(request):
    return render(request,'website/company_profile.html')

def why_us(request):
    return render(request,'website/why_us.html')
