from django.shortcuts import render, redirect
from services_app.models import Service
from services_app.forms import NewServiceForm
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'services_app/index.html')

def servicios_oficiales(request):
    services = Service.objects.filter(type='oficial') #query
    return render(request, 'services_app/servicios_oficiales.html', {'services': services})

def servicios_locales(request):
    services = Service.objects.filter(type='local') #query
    return render(request, 'services_app/servicios_locales.html', {'services': services})

def contact(request):
    return render(request, 'services_app/contact.html')

def service_register(request):
    if request.method == 'POST':
        form = NewServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('REbuscar-home')
    else:
        form = NewServiceForm()
    context = {'form':form}
    return render(request, 'services_app/service_register.html', context)
