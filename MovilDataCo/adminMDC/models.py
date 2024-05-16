from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    rol = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
    
class Abonados(models.Model):
    ANNO = models.FloatField(default=0)
    MES = models.FloatField(default=0)
    COLOMBIA_TELECOMUNICACIONES = models.FloatField(default=0)
    COLOMBIA_MOVIL = models.FloatField(default=0)
    COMUNICACION_CELULAR_COMCEL = models.FloatField(default=0)
    EMPRESA_DE_TELECOMUNICACIONES_DE_BOGOTA = models.FloatField(default=0)
    UNE_EPM = models.FloatField(default=0)
    AVANTEL = models.FloatField(default=0)
    ALMACENES_EXITO = models.FloatField(default=0)
    VIRGIN_MOBILE = models.FloatField(default=0)
    PARTNERS_TELECOM = models.FloatField(default=0)
    SETROC_MOBILE = models.FloatField(default=0)
    UFF_MOVIL = models.FloatField(default=0)
    CELLVOZ_COLOMBIA = models.FloatField(default=0)
    LOGISTICA_FLASH = models.FloatField(default=0)
    LOV_TELECOMUNICACIONES = models.FloatField(default=0)
    SUMA_MOVIL = models.FloatField(default=0)

class Ingresos(models.Model):
    ANNO = models.FloatField(default=0)
    MES = models.FloatField(default=0)
    COLOMBIA_TELECOMUNICACIONES = models.FloatField(default=0)
    COLOMBIA_MOVIL = models.FloatField(default=0)
    COMUNICACION_CELULAR_COMCEL = models.FloatField(default=0)
    EMPRESA_DE_TELECOMUNICACIONES_DE_BOGOTA = models.FloatField(default=0)
    UNE_EPM = models.FloatField(default=0)
    AVANTEL = models.FloatField(default=0)
    ALMACENES_EXITO = models.FloatField(default=0)
    VIRGIN_MOBILE = models.FloatField(default=0)
    PARTNERS_TELECOM = models.FloatField(default=0)
    SETROC_MOBILE = models.FloatField(default=0)
    UFF_MOVIL = models.FloatField(default=0)
    CELLVOZ_COLOMBIA = models.FloatField(default=0)
    LOGISTICA_FLASH = models.FloatField(default=0)
    LOV_TELECOMUNICACIONES = models.FloatField(default=0)
    SUMA_MOVIL = models.FloatField(default=0)

class Trafico(models.Model):
    ANNO = models.FloatField(default=0)
    MES = models.FloatField(default=0)
    COLOMBIA_TELECOMUNICACIONES = models.FloatField(default=0)
    COLOMBIA_MOVIL = models.FloatField(default=0)
    COMUNICACION_CELULAR_COMCEL = models.FloatField(default=0)
    EMPRESA_DE_TELECOMUNICACIONES_DE_BOGOTA = models.FloatField(default=0)
    UNE_EPM = models.FloatField(default=0)
    AVANTEL = models.FloatField(default=0)
    ALMACENES_EXITO = models.FloatField(default=0)
    VIRGIN_MOBILE = models.FloatField(default=0)
    PARTNERS_TELECOM = models.FloatField(default=0)
    SETROC_MOBILE = models.FloatField(default=0)
    UFF_MOVIL = models.FloatField(default=0)
    CELLVOZ_COLOMBIA = models.FloatField(default=0)
    LOGISTICA_FLASH = models.FloatField(default=0)
    LOV_TELECOMUNICACIONES = models.FloatField(default=0)
    SUMA_MOVIL = models.FloatField(default=0)

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name_plural="tablas"