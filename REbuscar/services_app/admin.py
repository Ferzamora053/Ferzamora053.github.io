from django.contrib import admin
from services_app.models import *
from django.apps import apps

# Register your models here.
app_models = apps.get_app_config('services_app').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except:
        pass
