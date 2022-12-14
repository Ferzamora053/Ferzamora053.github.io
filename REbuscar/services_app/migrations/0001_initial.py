# Generated by Django 4.1.4 on 2022-12-11 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='service_images/')),
                ('material', models.TextField()),
                ('description', models.TextField()),
                ('page_url', models.CharField(blank=True, max_length=2000, null=True)),
                ('pickup_locs', multiselectfield.db.fields.MultiSelectField(choices=[('cerrillos', 'Cerrillos'), ('cerro_navia', 'Cerro Navia'), ('conchalí', 'Conchalí'), ('el_bosque', 'El Bosque'), ('estacion_central', 'Estación Central'), ('huechuraba', 'Huechuraba'), ('independencia', 'Independencia'), ('la_cisterna', 'La Cisterna'), ('la_florida', 'La Florida'), ('la_granja', 'La Granja'), ('la_pintana', 'La Pintana'), ('la_reina', 'La Reina'), ('las_condes', 'Las Condes'), ('lo_barnechea', 'Lo Barnechea'), ('lo_espejo', 'Lo Espejo'), ('lo_prado', 'Lo Prado'), ('macul', 'Macul'), ('maipú', 'Maipú'), ('ñuñoa', 'Ñuñoa'), ('pedro_aguirre_cerda', 'Pedro Aguirre Cerda'), ('peñalolén', 'Peñalolén'), ('providencia', 'Providencia'), ('puente_alto', 'Puente Alto'), ('pudahuel', 'Pudahuel'), ('quilicura', 'Quilicura'), ('quinta_normal', 'Quinta Normal'), ('recoleta', 'Recoleta'), ('renca', 'Renca'), ('san_joaquin', 'San Joaquín'), ('san_miguel', 'San Miguel'), ('san_ramon', 'San Ramón'), ('santiago_centro', 'Santiago Centro'), ('vitacura', 'Vitacura'), ('santiago', 'Santiago')], max_length=1000)),
                ('type', models.CharField(choices=[('oficial', 'Oficial'), ('local', 'Local')], max_length=30)),
                ('certificate', models.FileField(blank=True, null=True, upload_to='user_certificates/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
