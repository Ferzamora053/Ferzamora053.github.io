from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.contrib import admin

# Create your models here.

pickup_locs_choices = (("cerrillos", "Cerrillos"),
                        ("cerro_navia", "Cerro Navia"),
                        ("conchalí", "Conchalí"),
                        ("el_bosque", "El Bosque"),
                        ("estacion_central", "Estación Central"),
                        ("huechuraba", "Huechuraba"),
                        ("independencia", "Independencia"),
                        ("la_cisterna", "La Cisterna"),
                        ("la_florida", "La Florida"),
                        ("la_granja", "La Granja"),
                        ("la_pintana", "La Pintana"),
                        ("la_reina", "La Reina"),
                        ("las_condes", "Las Condes"),
                        ("lo_barnechea", "Lo Barnechea"),
                        ("lo_espejo", "Lo Espejo"),
                        ("lo_prado", "Lo Prado"),
                        ("macul", "Macul"),
                        ("maipú", "Maipú"),
                        ("ñuñoa", "Ñuñoa"),
                        ("pedro_aguirre_cerda", "Pedro Aguirre Cerda"),
                        ("peñalolén", "Peñalolén"),
                        ("providencia", "Providencia"),
                        ("puente_alto", "Puente Alto"),
                        ("pudahuel", "Pudahuel"),
                        ("quilicura", "Quilicura"),
                        ("quinta_normal", "Quinta Normal"),
                        ("recoleta", "Recoleta"),
                        ("renca", "Renca"),
                        ("san_joaquin", "San Joaquín"),
                        ("san_miguel", "San Miguel"),
                        ("san_ramon", "San Ramón"),
                        ("santiago_centro", "Santiago Centro"),
                        ("vitacura", "Vitacura"),
                        ("santiago", "Santiago"))

class Service(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='service_images/', blank=True, null=True)
    material = models.TextField()
    description = models.TextField()
    page_url = models.CharField(max_length=2000, blank=True, null=True)
    pickup_locs = MultiSelectField(max_length=1000, choices=pickup_locs_choices)
    type = models.CharField(choices=(("oficial", "Oficial"), ("local", "Local")), max_length=30, null=True)
    certificate = models.FileField(upload_to='user_certificates/', blank=True, null=True)

    def __str__(self):
        return self.name
