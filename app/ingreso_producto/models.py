from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Producto(BaseModel):
    nombre = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        db_table = 'producto'
        ordering = ['-id']


class TipoIngreso(BaseModel):
    nombre = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'tipo_ingreso'
        ordering = ['-id']


class Proveedor(BaseModel):
    nombre = models.CharField(max_length=255, null=True, blank=True)
    ruc = models.CharField(max_length=30, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'proveedor'
        ordering = ['-id']


class Planta(BaseModel):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'planta'
        ordering = ['-id']


class IngresoProducto(BaseModel):
    fecha_ingreso = models.DateField()
    ticket = models.CharField(max_length=255)
    tipo_ingreso = models.ForeignKey(TipoIngreso, on_delete=models.SET_NULL, null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)
    planta = models.ForeignKey(Planta, on_delete=models.SET_NULL, null=True, blank=True)
    tanque_procedencia = models.CharField(max_length=255, null=True, blank=True)
    conductor = models.CharField(max_length=255, null=True, blank=True)
    placa_tracto = models.CharField(max_length=255, null=True, blank=True)
    placa_cisterna = models.CharField(max_length=255, null=True, blank=True)
    guia_remision = models.CharField(max_length=255, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    peso_guia = models.DecimalField(max_digits=14, decimal_places=4, null=True)
    peso_bruto = models.DecimalField(max_digits=14, decimal_places=4, null=True)
    peso_tara = models.DecimalField(max_digits=14, decimal_places=4, null=True)
    observacion = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'ingreso_producto'
        ordering = ['-id']

