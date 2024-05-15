from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    rol = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
    
class Demanda_Abonados(models.Model):
    ANNO = models.FloatField(default=0)
    TRIMESTRE = models.FloatField(default=0)
    MES_DEL_TRIMESTRE = models.FloatField(default=0)
    ID_EMPRESA = models.TextField(default="")
    EMPRESA = models.TextField(default="")
    ID_MODALIDAD_PAGO = models.FloatField(default=0)
    MODALIDAD_PAGO = models.TextField(default="")
    ID_TERMINAL = models.FloatField(default=0)
    TERMINAL = models.TextField(default="")
    ID_TECNOLOGIA = models.FloatField(default=0)
    TECNOLOGIA = models.TextField(default="")
    CANTIDAD_ABONADOS = models.FloatField(default=0)

class Demanda_Ingresos(models.Model):
    ANNO = models.FloatField(default=0)
    TRIMESTRE = models.FloatField(default=0)
    MES_DEL_TRIMESTRE = models.FloatField(default=0)
    ID_EMPRESA = models.FloatField(default=0)
    EMPRESA = models.TextField(default="")
    ID_MODALIDAD_PAGO = models.TextField(default="")
    MODALIDAD_PAGO = models.TextField(default="")
    ID_TERMINAL = models.FloatField(default=0)
    TERMINAL = models.TextField(default="")
    CANTIDAD_INGRESOS = models.FloatField(default=0)

class Demanda_Trafico(models.Model):
    ANNO = models.FloatField(default=0)
    TRIMESTRE = models.FloatField(default=0)
    MES_DEL_TRIMESTRE = models.FloatField(default=0)
    ID_EMPRESA = models.FloatField(default=0)
    EMPRESA = models.TextField(default="")
    ID_MODALIDAD_PAGO = models.TextField(default="")
    TRAFICO = models.FloatField(default=0)
    MODALIDAD_PAGO = models.TextField(default="")

class Cargo_Ingresos(models.Model):
    ANNO = models.FloatField(default=0)
    TRIMESTRE = models.FloatField(default=0)
    MES_DEL_TRIMESTRE = models.FloatField(default=0)
    ID_EMPRESA = models.FloatField(default=0)
    EMPRESA = models.TextField(default="")
    ID_SEGMENTO = models.FloatField(default=0)
    SEGMENTO = models.TextField(default="")
    ID_TERMINAL = models.FloatField(default=0)
    TERMINAL = models.TextField(default="")
    INGRESOS = models.FloatField(default=0)

class Cargo_Suscriptores(models.Model):
    ANNO = models.FloatField(default=0)
    TRIMESTRE = models.FloatField(default=0)
    MES_DEL_TRIMESTRE = models.FloatField(default=0)
    ID_SEGMENTO = models.FloatField(default=0)
    SEGMENTO = models.TextField(default="")
    ID_EMPRESA = models.FloatField(default=0)
    EMPRESA = models.TextField(default="")
    ID_TERMINAL = models.FloatField(default=0)
    TERMINAL = models.TextField(default="")
    ID_TECNOLOGIA = models.FloatField(default=0)
    TECNOLOGIA = models.TextField(default="")
    CANTIDAD_SUSCRIPTORES = models.FloatField(default=0)

class Cargo_Trafico(models.Model):
    ANNO = models.FloatField(default=0)
    TRIMESTRE = models.FloatField(default=0)
    MES_DEL_TRIMESTRE = models.FloatField(default=0)
    ID_EMPRESA = models.FloatField(default=0)
    EMPRESA = models.TextField(default="")
    CANTIDAD_ABONADOS = models.FloatField(default=0)

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name_plural="Demandas"