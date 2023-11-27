from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TipoMuestra(BaseModel):
    nombre = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'tipo_muestra'
        ordering = ['-id']


class Calidad(BaseModel):
    tipo_muestra = models.ForeignKey(TipoMuestra, on_delete=models.SET_NULL, null=True, blank=True, )
    nombre_muestreador = models.CharField(max_length=255, null=True, blank=True)
    acidez = models.DecimalField(max_digits=14, decimal_places=4, null=True)
    humedad = models.DecimalField(max_digits=14, decimal_places=4, null=True)
    impureza = models.DecimalField(max_digits=14, decimal_places=4, null=True)
    estearina = models.DecimalField(max_digits=14, decimal_places=4, null=True)
    anisidina = models.DecimalField(max_digits=14, decimal_places=4, null=True)
    linoleico = models.DecimalField(max_digits=14, decimal_places=4, null=True)
    epa = models.DecimalField(max_digits=14, decimal_places=4, null=True)
    dha = models.DecimalField(max_digits=14, decimal_places=4, null=True)
    indice_yodo = models.DecimalField(max_digits=14, decimal_places=4, null=True)

    ingreso_producto = models.ForeignKey('ingreso_producto.IngresoProducto', on_delete=models.SET_NULL, null=True, blank=True)


    class Meta:
        db_table = 'calidad'
        ordering = ['-id']

