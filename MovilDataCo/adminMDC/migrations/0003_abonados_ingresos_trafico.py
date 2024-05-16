# Generated by Django 5.0.6 on 2024-05-15 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminMDC', '0002_alter_usuarios_numero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abonados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ANNO', models.FloatField(default=0)),
                ('MES', models.FloatField(default=0)),
                ('COLOMBIA_TELECOMUNICACIONES', models.FloatField(default=0)),
                ('COLOMBIA_MOVIL', models.FloatField(default=0)),
                ('COMUNICACION_CELULAR_COMCEL', models.FloatField(default=0)),
                ('EMPRESA_DE_TELECOMUNICACIONES_DE_BOGOTA', models.FloatField(default=0)),
                ('UNE_EPM', models.FloatField(default=0)),
                ('AVANTEL', models.FloatField(default=0)),
                ('ALMACENES_EXITO', models.FloatField(default=0)),
                ('VIRGIN_MOBILE', models.FloatField(default=0)),
                ('PARTNERS_TELECOM', models.FloatField(default=0)),
                ('SETROC_MOBILE', models.FloatField(default=0)),
                ('UFF_MOVIL', models.FloatField(default=0)),
                ('CELLVOZ_COLOMBIA', models.FloatField(default=0)),
                ('LOGISTICA_FLASH', models.FloatField(default=0)),
                ('LOV_TELECOMUNICACIONES', models.FloatField(default=0)),
                ('SUMA_MOVIL', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ingresos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ANNO', models.FloatField(default=0)),
                ('MES', models.FloatField(default=0)),
                ('COLOMBIA_TELECOMUNICACIONES', models.FloatField(default=0)),
                ('COLOMBIA_MOVIL', models.FloatField(default=0)),
                ('COMUNICACION_CELULAR_COMCEL', models.FloatField(default=0)),
                ('EMPRESA_DE_TELECOMUNICACIONES_DE_BOGOTA', models.FloatField(default=0)),
                ('UNE_EPM', models.FloatField(default=0)),
                ('AVANTEL', models.FloatField(default=0)),
                ('ALMACENES_EXITO', models.FloatField(default=0)),
                ('VIRGIN_MOBILE', models.FloatField(default=0)),
                ('PARTNERS_TELECOM', models.FloatField(default=0)),
                ('SETROC_MOBILE', models.FloatField(default=0)),
                ('UFF_MOVIL', models.FloatField(default=0)),
                ('CELLVOZ_COLOMBIA', models.FloatField(default=0)),
                ('LOGISTICA_FLASH', models.FloatField(default=0)),
                ('LOV_TELECOMUNICACIONES', models.FloatField(default=0)),
                ('SUMA_MOVIL', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Trafico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ANNO', models.FloatField(default=0)),
                ('MES', models.FloatField(default=0)),
                ('COLOMBIA_TELECOMUNICACIONES', models.FloatField(default=0)),
                ('COLOMBIA_MOVIL', models.FloatField(default=0)),
                ('COMUNICACION_CELULAR_COMCEL', models.FloatField(default=0)),
                ('EMPRESA_DE_TELECOMUNICACIONES_DE_BOGOTA', models.FloatField(default=0)),
                ('UNE_EPM', models.FloatField(default=0)),
                ('AVANTEL', models.FloatField(default=0)),
                ('ALMACENES_EXITO', models.FloatField(default=0)),
                ('VIRGIN_MOBILE', models.FloatField(default=0)),
                ('PARTNERS_TELECOM', models.FloatField(default=0)),
                ('SETROC_MOBILE', models.FloatField(default=0)),
                ('UFF_MOVIL', models.FloatField(default=0)),
                ('CELLVOZ_COLOMBIA', models.FloatField(default=0)),
                ('LOGISTICA_FLASH', models.FloatField(default=0)),
                ('LOV_TELECOMUNICACIONES', models.FloatField(default=0)),
                ('SUMA_MOVIL', models.FloatField(default=0)),
            ],
            options={
                'verbose_name_plural': 'tablas',
            },
        ),
    ]