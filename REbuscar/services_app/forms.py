from django import forms
from django.forms import ModelForm
from services_app.models import Service


#Create your forms here.

class NewServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = [
            'user',
            'name',
            'phone',
            'email',
            'logo',
            'material',
            'description',
            'page_url',
            'pickup_locs',
            'certificate'
        ]
        
        labels = {
            'user': 'Nombre de usuario',
            'name': 'Nombre del servicio',
            'phone': 'Teléfono',
            'email': 'Correo electrónico',
            'logo': 'Logo del servicio',
            'material': 'Materiales que recicla',
            'description': 'Descripción de su servicio',
            'page_url': 'Url de la página (opcional)',
            'pickup_locs': 'Lugares de recogida',
            'certificate': 'Certificado de Registro de Personas Certificadas'
        }