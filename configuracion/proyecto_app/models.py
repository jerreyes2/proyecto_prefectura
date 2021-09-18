from django import db
from django.db import models
from django.db.models.base import ModelState

#from django.shortcuts import render_to_response

# Create your models here.

class bioma(models.Model):
    nom_bioma = models.CharField('nom_bioma',max_length=200,null=True)
    sigla_bioma = models.CharField('sigla_bioma',max_length=30,null=True)
    des_altitudinal_bioma = models.CharField('des_altitudinal_bioma',max_length=30,null=True)
    has_altitudinal_bioma = models.CharField('has_altitudinal_bioma',max_length=30,null=True)
    remanencia = models.CharField('remanencia',max_length=30,null=True)
    ext_bioma = models.CharField('ext_bioma',max_length=30,null=True)
    def __str__(self):
        return self.nom_bioma

    class Meta:
        db_table = 'bioma'

class locacion(models.Model):
    nom_locacion = models.CharField('nom_locacion',max_length=200,null=True)
    sigla_locacion = models.CharField('sigla_locacion',max_length=30,null=True)
    alt_locacion = models.CharField('alt_locacion',max_length=30,null=True)
    nombre_parroquia = models.CharField('nombre_parroquia',max_length=30,null=True)
    nombre_canton = models.CharField('nombre_canton',max_length=30,null=True)
    altitud = models.CharField('altitud',max_length=30,null=True)
    longitud = models.CharField('longitud',max_length=30,null=True)
    id_bioma = models.ForeignKey(bioma, on_delete=models.CASCADE,null=True)
    foto = models.ImageField(upload_to='albums/images/', null=True, blank=True)
    def __str__(self):
        return self.nom_locacion

    class Meta:
        db_table = 'locacion'
        

class estadoconservacion(models.Model):
    categoria = models.CharField('categoria',max_length=30,null=True)
    sigla = models.CharField('sigla',max_length=30,null=True)
    descripcion = models.CharField('descripcion',max_length=1000,null=True)
    def __str__(self):
        return self.categoria

    class Meta:
        db_table = 'estadoconservacion'

class fauna(models.Model):
    nom_especie = models.CharField('nom_especie',max_length=200,null=True)
    nom_cientifico = models.CharField('nom_cientifico',max_length=200,null=True)
    nom_ingles = models.CharField('nom_ingles',max_length=200,null=True)
    tipo = models.CharField('tipo',max_length=100,null=True)
    rango_altitudinal = models.CharField('rango_altitudinal',max_length=200,null=True)
    ubicacion = models.CharField('ubicacion',max_length=500,null=True)
    descripcion = models.CharField('descripcion',max_length=10000,null=True)
    autor = models.CharField('autor',max_length=200,null=True)
    imagen = models.ImageField(upload_to='albums/images/', null=True, blank=True)
    id_estado_conservacion = models.ForeignKey(estadoconservacion, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.nom_especie

    class Meta:
        db_table = 'fauna'


class fauna_locacion(models.Model):
    id_especie = models.ForeignKey(fauna, on_delete=models.CASCADE,null=True)
    id_locacion = models.ForeignKey(locacion, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'fauna_locacion'

class fauna_biomas(models.Model):
    
    id_especie = models.ForeignKey(fauna, on_delete=models.CASCADE,null=True)
    id_bioma = models.ForeignKey(bioma, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'fauna_biomas'


"""
class familia(models.Model):
    #id_taxon--
    id_taxon = models.IntegerField(default=0)
    #tip_taxon--
    tipo_flor = models.CharField(max_length=10, default='Orquidea', verbose_name='tipo_flor')
    #nom_cientifico--
    nombre_familia = models.CharField(max_length=10, verbose_name='nombre_familia')
    #nom_spanish
    nom_spanish=models.CharField(max_length=10, verbose_name='nom_spanish')
    #nom_ingles
    nom_ingles=models.CharField(max_length=10, verbose_name='nom_ingles')
    #de_caracteristicas
    de_caracteristicas=models.CharField(max_length=10, verbose_name='de_caracteristicas')
    #ubi_taxon
    ubi_taxon=models.CharField(max_length=10, verbose_name='ubi_taxon')
    #ima_animal
    #ima_animal= models.ImageField(upload_to='animal/%Y/%m/%d', null=True, blank=True)
    #migracion_aves
    migracion_aves=models.CharField(max_length=10, verbose_name='migracion_aves')
    #ced_persona
    ced_persona=models.CharField(max_length=10, verbose_name='ced_persona')
    #id_uicn
    id_uicn = models.IntegerField(default=0)
    #id_distribucion
    id_distribucion = models.IntegerField(default=0)
    #id_registro
    id_registro = models.IntegerField(default=0)
    #id_estado_conservacion
    id_registro = models.IntegerField(default=0)
    #id_nicho_trofico
    id_registro = models.IntegerField(default=0)
    #id_nicho_trofico
    id_registro = models.IntegerField(default=0)
    #id_amenaza
    id_amenaza = models.IntegerField(default=0)
    #id_endemisnmo
    id_registro = models.IntegerField(default=0)
    #etimologia--
    etimologia = models.CharField(max_length=10, verbose_name='etimologia')
    #diagnosis--
    diagnosis = models.CharField(max_length=10, verbose_name='diagnosis')
    #comenatarios_taxonomicos--
    comenatarios_taxonomicos = models.CharField(max_length=10, verbose_name='comenatarios_taxonomicos')
    #distribucion_composicion--
    distribucion_composicion = models.CharField(max_length=10, verbose_name='distribucion_composicion')

"""
