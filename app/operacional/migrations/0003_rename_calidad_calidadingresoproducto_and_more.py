# Generated by Django 4.2.7 on 2023-11-29 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operacional', '0002_historialingresoproductotanque'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Calidad',
            new_name='CalidadIngresoProducto',
        ),
        migrations.AlterModelTable(
            name='calidadingresoproducto',
            table='calidad_ingreso_producto',
        ),
        migrations.CreateModel(
            name='CalidadTanque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nombre_muestreador', models.CharField(blank=True, max_length=255, null=True)),
                ('acidez', models.DecimalField(decimal_places=4, max_digits=14, null=True)),
                ('humedad', models.DecimalField(decimal_places=4, max_digits=14, null=True)),
                ('impureza', models.DecimalField(decimal_places=4, max_digits=14, null=True)),
                ('estearina', models.DecimalField(decimal_places=4, max_digits=14, null=True)),
                ('anisidina', models.DecimalField(decimal_places=4, max_digits=14, null=True)),
                ('linoleico', models.DecimalField(decimal_places=4, max_digits=14, null=True)),
                ('epa', models.DecimalField(decimal_places=4, max_digits=14, null=True)),
                ('dha', models.DecimalField(decimal_places=4, max_digits=14, null=True)),
                ('indice_yodo', models.DecimalField(decimal_places=4, max_digits=14, null=True)),
                ('tanque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operacional.tanque')),
                ('tipo_muestra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='operacional.tipomuestra')),
            ],
            options={
                'db_table': 'calidad_tanque',
                'ordering': ['-id'],
            },
        ),
    ]