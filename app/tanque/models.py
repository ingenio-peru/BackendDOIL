from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class TipoTanque(BaseModel):
    nombre = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'tipo_tanque'
        ordering = ['-id']


class Tanque(BaseModel):
    tipo_tanque = models.ForeignKey(TipoTanque, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    capacidad = models.DecimalField(max_digits=14, decimal_places=4, null=True)

    class Meta:
        db_table = 'tanque'
        ordering = ['-id']

