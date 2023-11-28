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
    peso_neto = models.DecimalField(max_digits=14, decimal_places=4, null=True) #bruto - tara
    peso_neto_disponible = models.DecimalField(max_digits=14, decimal_places=4, null=True)
    observacion = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'ingreso_producto'
        ordering = ['-id']


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
    capacidad_disponible = models.DecimalField(max_digits=14, decimal_places=4, null=True)

    class Meta:
        db_table = 'tanque'
        ordering = ['-id']


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

    ingreso_producto = models.ForeignKey(IngresoProducto, on_delete=models.SET_NULL, null=True, blank=True)


    class Meta:
        db_table = 'calidad'
        ordering = ['-id']


class IngresoProductoTanque(BaseModel):
    ingreso_producto = models.ForeignKey(IngresoProducto, on_delete=models.SET_NULL, null=True, blank=True)
    tanque = models.ForeignKey(Tanque, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.DecimalField(max_digits=14, decimal_places=4)
    fecha = models.DateField()

    class Meta:
        db_table = 'ingreso_producto_tanque'
        ordering = ['-id']