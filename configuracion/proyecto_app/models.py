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
    
    id_estado_conservacion = models.ForeignKey(estadoconservacion, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.nom_especie

    class Meta:
        db_table = 'fauna'


class imagen_fauna(models.Model):
    id_imagen = models.IntegerField('id_imagen',primary_key = True)
    id_especie = models.ForeignKey(fauna, on_delete=models.CASCADE,null=True)
    autor = models.CharField('autor',max_length=200,null=True)
    imagen = models.ImageField(upload_to='fauna', null=True, blank=True)

    class Meta:
        db_table = 'imagen_fauna'

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
class clases(models.Model):
    id_clase = models.IntegerField('id_clase',primary_key = True)
    nom_clase = models.CharField('nom_clase',max_length=200,null=True)
    tipo = models.CharField('tipo',max_length=200,null=True)
    abund_clase = models.CharField('abund_clase',max_length=200,null=True)
    num_ord_clase = models.CharField('num_ord_clase',max_length=200,null=True)
    def __str__(self):
        return self.nom_clase

    class Meta:
        db_table = 'clases'

class ordenes(models.Model):
    id_orden = models.IntegerField('id_orden',primary_key = True)
    nom_orden = models.CharField('nom_orden',max_length=200,null=True)
    tipo = models.CharField('tipo',max_length=200,null=True)
    id_clase = models.ForeignKey(clases, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.nom_orden

    class Meta:
        db_table = 'ordenes'

class familias(models.Model):
    id_familia = models.IntegerField('id_familia',primary_key = True)
    nom_familia = models.CharField('nom_familia',max_length=200,null=True)
    tipo = models.CharField('tipo',max_length=200,null=True)
    id_orden = models.ForeignKey(ordenes, on_delete=models.CASCADE,null=True)
    id_clase = models.ForeignKey(clases, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.nom_familia

    class Meta:
        db_table = 'familias'

class abundancias(models.Model):
    id_abundancia = models.IntegerField('id_abundancia',primary_key = True)
    tax_abundancia = models.CharField('tax_abundancia',max_length=200,null=True)
    num_abundancia = models.FloatField(null=True)
    ran_abundancia = models.CharField('ran_abundancia',max_length=200,null=True)
    id_familia = models.ForeignKey(familias, on_delete=models.CASCADE,null=True)
    id_orden = models.ForeignKey(ordenes, on_delete=models.CASCADE,null=True)
    id_clase = models.ForeignKey(clases, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.tax_abundancia

    class Meta:
        db_table = 'abundancias'

class pisos_zeogeograficos(models.Model):
    id_pisozeogeografico = models.IntegerField('id_pisozeogeografico',primary_key = True)
    nom_pisozeogeografico = models.CharField('nom_pisozeogeografico',max_length=200,null=True)
    sigla_pisozeogeografico = models.CharField('sigla_pisozeogeografico',max_length=200,null=True)
    def __str__(self):
        return self.nom_pisozeogeografico

    class Meta:
        db_table = 'pisos_zeogeograficos'

class provincias(models.Model):
    id_provincia = models.IntegerField('id_provincia',primary_key = True)
    nom_provincia = models.CharField("nomb_provincia",max_length=30,null=True)

    class Meta:
        db_table = 'provincias' 

class biomas(models.Model):
    id_bioma = models.IntegerField('id_bioma',primary_key = True)
    nom_bioma = models.CharField('nom_bioma',max_length=200,null=True)
    sigla_bioma = models.CharField('sigla_bioma',max_length=30,null=True)
    des_altitudinal_bioma = models.CharField('des_altitudinal_bioma',max_length=30,null=True)
    has_altitudinal_bioma = models.CharField('has_altitudinal_bioma',max_length=30,null=True)
    remanencia = models.CharField('remanencia',max_length=30,null=True)
    ext_bioma = models.CharField('ext_bioma',max_length=30,null=True)
    id_provincia = models.ForeignKey(provincias, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nom_bioma

    class Meta:
        db_table = 'biomas'

class ecosistemas(models.Model):
    id_ecosistema = models.IntegerField('id_ecosistema',primary_key = True)
    nom_ecosistema = models.CharField('nom_ecosistema',max_length=200,null=True)
    cod_ecosistema = models.CharField('cod_ecosistema',max_length=200,null=True)
    id_pisozeogeografico = models.ForeignKey(pisos_zeogeograficos, on_delete=models.CASCADE,null=True)
    id_bioma = models.ForeignKey(biomas, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.nom_ecosistema
    
    class Meta:
        db_table = 'ecosistemas'

class abundancias_ecosistemas(models.Model):
    id_ecosistema = models.ForeignKey(ecosistemas, on_delete=models.CASCADE,null=True)
    id_abundancia = models.ForeignKey(abundancias, on_delete=models.CASCADE,null=True)
    
    class Meta:
        db_table = 'abundancias_ecosistemas'

class unidades_hidrograficas(models.Model):
    id_uh = models.IntegerField('id_uh',primary_key = True)
    nom_uh = models.CharField('nom_uh',max_length=200,null=True)
    cod_uh = models.IntegerField(null=True)
    riqueza_uh = models.FloatField(null=True)
    abundancia_uh = models.FloatField(null=True)
    def __str__(self):
        return self.nom_uh

    class Meta:
        db_table = 'unidades_hidrograficas'

class abundancias_uh(models.Model):
    id_abundancia = models.ForeignKey(abundancias, on_delete=models.CASCADE,null=True)
    id_uh = models.ForeignKey(unidades_hidrograficas, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'abundancias_uh'

class actividades(models.Model):
    id_actividad = models.IntegerField('id_actividad',primary_key = True)
    nom_actividad = models.CharField('nom_actividad',max_length=200,null=True)
    sigla_actividad = models.CharField('sigla_actividad',max_length=200,null=True)
    def __str__(self):
        return self.nom_actividad

    class Meta:
        db_table = 'actividades'

# --> aqui debajo poner modelo bosques (Rene)
#08/10 KEv

class rios(models.Model):
    id_rio = models.IntegerField('id_rio',primary_key = True)
    nom_rio = models.CharField('nom_rio',max_length=200,null=True)
    categoria = models.CharField('categoria',max_length=200,null=True)

    class Meta:
        db_table = 'rios'


class bosques(models.Model):
    id_bosque = models.IntegerField('id_bosque',primary_key = True)
    nom_bosque = models.CharField('nom_bosque',max_length=200,null=True)
    pro_administrador_bosque = models.CharField('pro_administrador_bosque',max_length=200,null=True)
    localizacion_area = models.CharField('localizacion_area',max_length=200,null=True)
    micro_cuencas = models.CharField('micro_cuencas',max_length=200,null=True)
    reg_oficial_bosque = models.CharField('reg_oficial_bosque',max_length=200,null=True)
    hec_bosque = models.FloatField(null=True)
    vegetacion_remanente = models.FloatField(null=True)
    altitud_max = models.FloatField(null=True)
    altitud_min = models.FloatField(null=True)

    class Meta:
        db_table = 'bosques'

class bosques_rios(models.Model):
    id_rio = models.ForeignKey(rios, on_delete=models.CASCADE,null=True)
    id_bosque = models.ForeignKey(bosques, on_delete=models.CASCADE,null=True)
    
    class Meta:
        db_table = 'bosques_rios'


class arboles(models.Model):
    id_arbol = models.IntegerField('id_arbol',primary_key = True)
    nom_arbol = models.CharField('nom_arbol',max_length=200,null=True)
    esp_arbol = models.CharField('esp_arbol',max_length=200,null=True)
    alt_arbol = models.FloatField(null=True)
    tip_arbol = models.CharField('tip_arbol',max_length=200,null=True)
    id_bosque = models.ForeignKey(bosques, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'arboles'


# ----- Erreyes

class areas(models.Model):
    #id_area = models.IntegerField()
    cat_area = models.CharField("cant_area", max_length=100, null=True)
    nom_area = models.CharField("nom_area", max_length=100, null= True)
    fe_creacion = models.DateField( "fe_creacion", null= True)
    acu_resolucion_area = models.CharField("acu_resolucion_area", max_length=200, null= True)
    aut_competente_area = models.CharField("aut_competente_area", max_length=200, null=True)    
    superfici_area = models.CharField("superfici_area", max_length=200, null=True)    
    tipo = models.CharField("tipo", max_length=200, null=True)    

    class Meta:
        db_table = 'areas'

class areas_naturales_corredor_ecolog(models.Model):
    
    #id_area_corredor = models.IntegerField()
    asp_min_cap_inst = models.CharField("asp_min_cap_inst", max_length=200, null=True)
    analisis = models.CharField("analisis", max_length=200, null=True)
    observaciones = models.CharField("observaciones", max_length=200, null=True)

    class Meta:
        db_table = 'areas_naturales_corredor_ecolog'



# -- tabla de cantones ->
class cantones(models.Model):
    id_canton = models.IntegerField('id_canton',primary_key = True)
    nom_canton = models.CharField('nom_canton',max_length=200,null=True)
    id_provincia = models.ForeignKey(provincias, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.nom_canton

    class Meta:
        db_table = 'cantones'


class biomas_cantones(models.Model):
    id_bioma = models.ForeignKey(biomas,on_delete= models.CASCADE, null=True)
    id_canton = models.ForeignKey(cantones,on_delete= models.CASCADE, null=True)

    class Meta:
        db_table = 'biomas_cantones'

class biomas_ecosistemas(models.Model):
    id_bioma = models.ForeignKey(biomas,on_delete= models.CASCADE, null=True)
    id_ecosistema = models.ForeignKey(ecosistemas,on_delete= models.CASCADE, null=True)

    class Meta:
        db_table = 'biomas_ecosistemas'


#07/10




# Erreyes 2

class estado_conservacion(models.Model):
    id_estado_conservacion = models.IntegerField('id_estado_conservacion',primary_key = True)
    categoria = models.CharField('categoria',max_length=100,null=True)
    sigla =  models.CharField('sigla',max_length=50,null=True)
    descripcion = models.CharField('descripcion',max_length=200,null=True)

    class Meta:
            db_table = 'estado_conservacion'
    
class clasificacion(models.Model):
    id_clasificacion = models.IntegerField('id_clasificacion',primary_key = True)
    nom_clasificacion = models.CharField('nom_clasificacion',max_length=200,null=True)
    id_estado_conservacion = models.ForeignKey(estado_conservacion,on_delete= models.CASCADE, null=True)
    
    class Meta:
        db_table = 'clasificacion'


class distribuciones(models.Model):
    id_distribucion = models.IntegerField('id_distribucion',primary_key = True)
    nom_distribucion = models.CharField('nom_distribucion',max_length=200,null=True)
    sigla_distribucion = models.CharField('sigla_distribucion',max_length=50,null=True)
    
    class Meta:
        db_table = 'distribuciones'


    
class nichotrofico(models.Model):
    id_nicho_trofico = models.IntegerField('id_nicho_trofico',primary_key = True)
    nom_nicho = models.CharField('nom_nicho',max_length=150,null=True)
    sigla_nicho = models.CharField('sigla_nicho',max_length=50,null=True)
    descripcion = models.CharField('descripcion',max_length=150,null=True)
    
    class Meta:
        db_table = 'nichotrofico'


class personas(models.Model):
    id_persona = models.IntegerField('id_persona', primary_key = True)
    nom_persona = models.CharField('nom_persona',max_length=255,null=True)
    ape_pesona = models.CharField('ape_persona',max_length=255,null=True)
    tipo = models.CharField('tipo',max_length=100,null=True)
    
    class Meta:
        db_table = 'personas'
    
class ordenes(models.Model):
    id_orden = models.IntegerField('id_orden', primary_key = True)
    nom_orden = models.CharField('nom_orden',max_length=255,null=True)
    tipo = models.CharField('tipo',max_length=100,null=True)
    id_clase = models.ForeignKey(clases, on_delete= models.CASCADE, null=True)
    
    class Meta:
        db_table = 'ordenes'

class migracion_aves(models.Model):
    id_migracion = models.IntegerField('id_migracion', primary_key = True)
    nom_migracion = models.CharField('nom_migracion',max_length=255,null=True)
    sigla = models.CharField('sigla',max_length=100,null=True)
    
    class Meta:
        db_table = 'migracion_aves'    

class especies(models.Model):
    id_especie = models.IntegerField('id_especie', primary_key = True)
    nom_especie = models.CharField('nom_especie',max_length=255,null=True)
    tipo =  models.CharField('tipo',max_length=100,null=True)
    rango_altitudinal = models.CharField('rango_altitudinal',max_length=255,null=True)
    ubicacion = models.CharField('ubicacion',max_length=255,null=True)
    descripcion = models.CharField('descripcion',max_length=255,null=True)
    nom_cientifico = models.CharField('nom_cientifico',max_length=100,null=True)
    nom_ingles = models.CharField('nom_ingles',max_length=100,null=True)

    id_estado_conservacion = models.ForeignKey(estado_conservacion,on_delete= models.CASCADE, null=True)
    nacional = models.IntegerField('nacional')
    id_nicho_trofico = models.ForeignKey(nichotrofico, on_delete= models.CASCADE, null=True)
    id_persona =  models.ForeignKey(personas, on_delete= models.CASCADE, null=True)
    id_familia =  models.ForeignKey(familias, on_delete= models.CASCADE, null=True)
    id_orden = models.ForeignKey(ordenes, on_delete= models.CASCADE, null=True)
    id_clase = models.ForeignKey(clases, on_delete= models.CASCADE, null=True)
    anio_descubrimiento = models.FloatField('')
    id_migracion = models.ForeignKey(migracion_aves, on_delete= models.CASCADE, null=True)

    class Meta:
        db_table = 'especies'


# -- ricky 2

class canton_area(models.Model):
    id_area = models.ForeignKey(areas, on_delete=models.CASCADE,null=True)
    id_canton = models.ForeignKey(cantones, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'canton_area'

class canton_bosque(models.Model):
    id_bosque = models.ForeignKey(bosques, on_delete=models.CASCADE,null=True)
    id_canton = models.ForeignKey(cantones, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'canton_bosque'

class canton_ecosistema(models.Model):
    id_canton = models.ForeignKey(cantones, on_delete=models.CASCADE,null=True)
    id_ecosistema = models.ForeignKey(ecosistemas, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'canton_ecosistema'


class cantones_rios(models.Model):
    id_canton = models.ForeignKey(cantones, on_delete=models.CASCADE,null=True)
    id_rio = models.ForeignKey(rios, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'cantones_rios'

class cantones_unidades_hidrograficas(models.Model):
    id_uh = models.ForeignKey(unidades_hidrograficas, on_delete=models.CASCADE,null=True)
    id_canton = models.ForeignKey(cantones, on_delete=models.CASCADE,null=True)
    id_provincia = models.ForeignKey(provincias, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'cantones_unidades_hidrograficas'

class circuitos_integracion_biolog(models.Model):
    id_circuito = models.IntegerField('id_circuito',primary_key = True)
    nombre_circuito = models.CharField('nombre_circuito',max_length=200,null=True)
    desc_circuito = models.CharField('desc_circuito',max_length=200,null=True)

    def __str__(self):
        return self.nombre_circuito
        
    class Meta:
        db_table = 'circuitos_integracion_biolog'

        
#08/10 KEv2
class endemismos(models.Model):
    id_endemismo = models.IntegerField('id_endemismo',primary_key = True)
    nom_endemismo = models.CharField('nom_endemismo',max_length=100,null=True)
    sigla_endemismo = models.CharField('sigla_endemismo',max_length=50,null=True)
        
    class Meta:
        db_table = 'endemismos'

class registros(models.Model):
    id_registro = models.IntegerField('id_registro',primary_key = True)
    nom_registro = models.CharField('nom_registro',max_length=200,null=True)
    literal = models.CharField('literal',max_length=200,null=True)
        
    class Meta:
        db_table = 'registros'

class parroquias(models.Model):
    id_parroquias = models.IntegerField('id_parroquias',primary_key = True) 
    nom_parroquia = models.CharField('nom_parroquia',max_length=100,null=True)
    id_canton = models.ForeignKey(cantones,on_delete= models.CASCADE, null=True)
    id_provincia = models.ForeignKey(provincias,on_delete= models.CASCADE, null=True)
    
    class Meta:
        db_table = 'parroquias'

class locaciones(models.Model):
    id_locacion = models.IntegerField('id_locacion',primary_key = True)
    nom_locacion = models.CharField('nom_locacion',max_length=100,null=True)
    sigla_locacion = models.CharField('sigla_locacion',max_length=50,null=True)
    alt_locacion = models.FloatField(null=True)
    id_parroquia = models.ForeignKey(parroquias, on_delete=models.CASCADE,null=True)
    id_canton = models.ForeignKey(cantones, on_delete=models.CASCADE,null=True)
    id_provincia = models.ForeignKey(provincias, on_delete=models.CASCADE,null=True)
    coordenadas = models.CharField('nom_endemismo',max_length=100,null=True)
    id_bioma = models.ForeignKey(biomas, on_delete=models.CASCADE,null=True)
    latitud_locacion = models.FloatField(null=True)
    longitud_locacion = models.FloatField(null=True)
    
    class Meta:
        db_table = 'locaciones'

class estaciones_muestreos(models.Model):
    id_em = models.IntegerField('id_em',primary_key = True)
    nom_em = models.CharField('nom_em',max_length=200,null=True)
    nom_formal_em = models.CharField('nom_formal_em',max_length=200,null=True)
    cod_em = models.CharField('cod_em',max_length=200,null=True)
    id_rio = models.ForeignKey(rios, on_delete=models.CASCADE,null=True)
    ind_shannon_em = models.FloatField(null=True)

    def __str__(self):
        return self.nom_em

    class Meta:
        db_table = 'estaciones_muestreos'

class localidades_muestreo(models.Model):
    id_muestreo = models.IntegerField('id_muestreo',primary_key = True)
    num_muestreo = models.FloatField(null=True)
    nom_muestreo = models.CharField('nom_muestreo',max_length=50,null=True)
    des_muestreo = models.CharField('des_muestreo',max_length=50,null=True)
    log_muestreo = models.FloatField(null=True)
    lat_muestreo = models.FloatField(null=True)
    alt_muestreo = models.FloatField(null=True)
    tipo_animal = models.CharField('sigla_locacion',max_length=50,null=True)
    id_em = models.ForeignKey(estaciones_muestreos, on_delete=models.CASCADE,null=True)
    
    class Meta:
        db_table = 'localidades_muestreo'

class especie_locaciones(models.Model):
    id_especie = models.ForeignKey(especies, on_delete=models.CASCADE,null=True)
    id_locacion = models.ForeignKey(locaciones, on_delete=models.CASCADE,null=True)
    
    class Meta:
        db_table = 'especie_locaciones'



class especie_registros(models.Model):
    id_especie = models.ForeignKey(especies, on_delete=models.CASCADE,null=True)
    id_registro = models.ForeignKey(registros, on_delete=models.CASCADE,null=True)
    
    class Meta:
        db_table = 'especie_registros'

class especies_actividades(models.Model):
    id_especie = models.ForeignKey(especies, on_delete=models.CASCADE,null=True)
    id_actividad = models.ForeignKey(actividades, on_delete=models.CASCADE,null=True)
    
    class Meta:
        db_table = 'especies_actividades'


class especies_distribucion(models.Model):
    id_especie = models.ForeignKey(especies, on_delete=models.CASCADE,null=True)
    id_distribucion = models.ForeignKey(distribuciones, on_delete=models.CASCADE,null=True)
    
    class Meta:
        db_table = 'especies_distribucion'

class especies_localidades_muestreo(models.Model):
    id_especie = models.ForeignKey(especies, on_delete=models.CASCADE,null=True)
    id_muestreo = models.ForeignKey(localidades_muestreo, on_delete=models.CASCADE,null=True)
    
    class Meta:
        db_table = 'especies_localidades_muestreo'


# -- Ricky 3 -

class tipos_vegetacion(models.Model):
    id_tipovegetacion = models.IntegerField('id_tipovegetacion',primary_key = True)
    nom_tipovegetacion = models.CharField('nom_tipovegetacion',max_length=200,null=True)
    sigla_tipovegetacion = models.CharField('sigla_tipovegetacion',max_length=200,null=True)

    def __str__(self):
        return self.nom_tipovegetacion

    class Meta:
        db_table = 'tipos_vegetacion'

class especies_tiposvegetacion(models.Model):
    id_especie = models.ForeignKey(especies, on_delete=models.CASCADE,null=True)
    id_tiposvegetacion = models.ForeignKey(tipos_vegetacion, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'especies_tiposvegetacion'

class flora(models.Model):
    id_flora = models.IntegerField('id_flora',primary_key = True)
    nom_flora = models.CharField('nom_flora',max_length=200,null=True)
    tipo = models.CharField('tipo',max_length=200,null=True)
    etimologia = models.CharField('etimologia',max_length=200,null=True)
    diagnosis = models.CharField('diagnosis',max_length=200,null=True)
    comentarios_taxonomicos = models.CharField('comentarios_taxonomicos',max_length=200,null=True)
    distribucion_composicion = models.CharField('distribucion_composicion',max_length=200,null=True)
    autor = models.CharField('autor',max_length=200,null=True)

    def __str__(self):
        return self.nom_flora

    class Meta:
        db_table = 'flora'

class flora_biomas(models.Model):
    id_flora = models.ForeignKey(flora, on_delete=models.CASCADE,null=True)
    id_bioma = models.ForeignKey(biomas, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'flora_biomas'

class flora_endemica_amenazada(models.Model):
    #id_flora = models.ForeignKey(flora, on_delete=models.CASCADE,null=True)
    nombre_cientifico = models.CharField('nombre_cientifico',max_length=200,null=True)
    #uicn_cites = models.CharField('uicn_cites',max_length=200,null=True)

    class Meta:
        db_table = 'flora_endemica_amenazada'

class flora_imagen(models.Model):
    id_flora_imagen = models.IntegerField('id_flora_imagen',primary_key = True)
    imagenflora = models.CharField('imagenflora',max_length=200,null=True)
    tipo_flora = models.CharField('tipo_flora',max_length=200,null=True)
    autor_imagen = models.CharField('autor_imagen',max_length=200,null=True)
    id_flora = models.ForeignKey(flora, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'flora_imagen'

class flora_locaciones(models.Model):
    id_flora = models.ForeignKey(flora, on_delete=models.CASCADE,null=True)
    id_locacion = models.ForeignKey(locaciones, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'flora_locaciones'

class genero(models.Model):
    id_genero = models.IntegerField('id_genero',primary_key = True)
    nom_genero = models.CharField('nom_genero',max_length=200,null=True)
    etimologia = models.CharField('etimologia',max_length=200,null=True)
    diagnosis = models.CharField('diagnosis',max_length=200,null=True)
    comentarios_taxonomicos = models.CharField('comentarios_taxonomicos',max_length=200,null=True)
    distribucion_composicion = models.CharField('distribucion_composicion',max_length=200,null=True)

    def __str__(self):
        return self.nom_genero

    class Meta:
        db_table = 'genero'

class genero_flora(models.Model):
    id_flora = models.ForeignKey(flora, on_delete=models.CASCADE,null=True)
    id_genero = models.ForeignKey(genero, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'genero_flora'

# --KEv
class microcuencas(models.Model):
    id_microcuenca = models.IntegerField('id_microcuenca',primary_key = True)
    nom_microcuenca = models.CharField('nom_microcuenca',max_length=100,null=True)
    sup_km2_microcuenca = models.CharField('sup_km2_microcuenca',max_length=100,null=True)
    zona1_microcuenca = models.CharField('zona1_microcuenca',max_length=100,null=True)
    zona2_microcuenca = models.CharField('zona2_microcuenca',max_length=100,null=True)
    zona3_microcuenca = models.CharField('zona3_microcuenca',max_length=100,null=True)
    zona4_microcuenca = models.CharField('zona4_microcuenca',max_length=100,null=True)
    zona5_microcuenca = models.CharField('zona5_microcuenca',max_length=100,null=True)
    zona6_microcuenca = models.CharField('zona6_microcuenca',max_length=100,null=True)
    
    class Meta:
        db_table = 'microcuencas'


class ordenes_biomas(models.Model):
    id_orden = models.ForeignKey(ordenes,on_delete= models.CASCADE, null=True)
    id_bioma = models.ForeignKey(biomas,on_delete= models.CASCADE, null=True)
    
    class Meta:
        db_table = 'ordenes_biomas'

class ordenes_familias(models.Model):
    id_orden = models.ForeignKey(ordenes,on_delete= models.CASCADE, null=True)
    id_familia = models.ForeignKey(familias,on_delete= models.CASCADE, null=True)
    num_generos = models.IntegerField('num_generos',null=True)
    num_especies = models.IntegerField('num_especies',null=True)
    porcentaje = models.FloatField(null=True)
    
    class Meta:
        db_table = 'ordenes_familias'

#-----------------------------------

class activida_no_permitida_zonas_res(models.Model):
    id_zona_restauracion = models.IntegerField('id_zona_restauracion',primary_key = True)
    actividades_permitidas = models.CharField('actividades_permitidas',max_length=100,null=True)
    
    class Meta:
        db_table = 'activida_no_permitida_zonas_res'

class actividades_no_permitidad_macro(models.Model):
    id_zona_macrona = models.IntegerField('id_zona_macrona',primary_key = True)
    actividades_no_permitidas = models.CharField('actividades_no_permitidas',max_length=100,null=True)
    
    class Meta:
        db_table = 'actividades_no_permitidad_macro'

class actividades_no_permitidas_zona_(models.Model):
    id_zona_prot_est = models.IntegerField('id_zona_prot_est',primary_key = True)
    actividades_no_permitidas = models.CharField('actividades_no_permitidas',max_length=100,null=True)
    
    class Meta:
        db_table = 'actividades_no_permitidas_zona_'

class actividades_permitidad_macrona_(models.Model):
    id_zona_macrona = models.IntegerField('id_zona_macrona',primary_key = True)
    actividades_permitidas = models.CharField('actividades_permitidas',max_length=100,null=True)
    
    class Meta:
        db_table = 'actividades_permitidad_macrona_'

class actividades_permitidad_zonas_co(models.Model):
    id_zona_conservacion = models.IntegerField('id_zona_conservacion',primary_key = True)
    actividades_permitidas = models.CharField('actividades_permitidas',max_length=100,null=True)
    
    class Meta:
        db_table = 'actividades_permitidad_zonas_co'

class actividades_permitidad_zonas_pr(models.Model):
    id_zona_prot_est = models.IntegerField('id_zona_prot_est',primary_key = True)
    actividades_permitidas = models.CharField('actividades_permitidas',max_length=100,null=True)
    
    class Meta:
        db_table = 'actividades_permitidad_zonas_pr'

class actividades_permitidad_zonas_re(models.Model):
    id_zona_restauracion = models.IntegerField('id_zona_restauracion',primary_key = True)
    actividades_permitidas = models.CharField('actividades_permitidas',max_length=100,null=True)
    
    class Meta:
        db_table = 'actividades_permitidad_zonas_re'
        
class arbol_alimento_pericos(models.Model):
    id_arbol = models.IntegerField('id_arbol',primary_key = True)
    especie_arbol = models.CharField('especie_arbol',max_length=100,null=True)
    mes_epoca = models.CharField('mes_epoca',max_length=100,null=True)

    class Meta:
        db_table = 'arbol_alimento_pericos'


class area_naturales_conservacion(models.Model):
    id_areanatural = models.IntegerField('id_areanatural',primary_key = True)
    nombre_area = models.CharField('nombre_area',max_length=100,null=True)
    desc_area = models.CharField('desc_area',max_length=100,null=True)

    class Meta:
        db_table = 'area_naturales_conservacion'
    
class area_vegetal(models.Model):
    id_areanatural = models.ForeignKey(area_naturales_conservacion,on_delete= models.CASCADE, null=True)
    covertura_vegetal = models.CharField('covertura_vegetal',max_length=100,null=True)
    hectareas = models.FloatField(null=True)
    porcentaje = models.FloatField(null=True)

    class Meta:
        db_table = 'area_vegetal'

class geologias(models.Model):
    id_geologia = models.IntegerField('id_geologia',primary_key = True)
    nom_geologia = models.CharField('nom_geologia',max_length=100,null=True)

    class Meta:
        db_table = 'geologias'

class geomorfologia(models.Model):
    id_geomorfologia = models.IntegerField('id_geomorfologia',primary_key = True)
    nom_geomorfologia = models.CharField('nom_geomorfologia',max_length=100,null=True)

    class Meta:
        db_table = 'geomorfologia'

class areanatural_geologia(models.Model):
    id_areanatural = models.ForeignKey(area_naturales_conservacion,on_delete= models.CASCADE, null=True)
    id_geologia = models.ForeignKey(geologias,on_delete= models.CASCADE, null=True)
    hec_geologia = models.FloatField(null=True)
    porcentaje = models.FloatField(null=True)

    class Meta:
        db_table = 'areanatural_geologia'

class areanatural_geomorfologia(models.Model):
    id_areanatural = models.ForeignKey(area_naturales_conservacion,on_delete= models.CASCADE, null=True)
    id_geomorfologia = models.ForeignKey(geologias,on_delete= models.CASCADE, null=True)
    hec_geomorfologia = models.FloatField(null=True)
    porcentaje = models.FloatField(null=True)

    class Meta:
        db_table = 'areanatural_geomorfologia'

class areanatural_locacion(models.Model):
    id_areanatural = models.ForeignKey(area_naturales_conservacion,on_delete= models.CASCADE, null=True)
    id_canton = models.ForeignKey(cantones,on_delete= models.CASCADE, null=True)
    id_parroquia = models.ForeignKey(parroquias,on_delete= models.CASCADE, null=True)
    km_cuadrados = models.FloatField(null=True)
    porcentaje = models.FloatField(null=True)

    class Meta:
        db_table = 'areanatural_locacion'

class suelos(models.Model):
    id_suelos = models.IntegerField('id_suelos',primary_key = True) 
    nom_suelos = models.CharField('nom_suelos',max_length=100,null=True)

    class Meta:
        db_table = 'suelos'

class areanatural_suelo(models.Model):
    id_suelos = models.ForeignKey(suelos,on_delete= models.CASCADE, null=True)
    id_areanatural = models.ForeignKey(area_naturales_conservacion,on_delete= models.CASCADE, null=True)
    hec_geologia = models.FloatField(null=True)
    porcentaje = models.FloatField(null=True)

    class Meta:
        db_table = 'areanatural_suelo'

class ben_corredores_ecologicos(models.Model):
    id_beneficio = models.IntegerField('id_beneficio',primary_key = True) 
    nobre_beneficio = models.CharField('nobre_beneficio',max_length=100,null=True)
    descripcion_beneficio = models.CharField('descripcion_beneficio',max_length=100,null=True)

    class Meta:
        db_table = 'ben_corredores_ecologicos'

class biomas_especies(models.Model):
    id_especie = models.ForeignKey(especies,on_delete= models.CASCADE, null=True)
    id_bioma = models.ForeignKey(biomas,on_delete= models.CASCADE, null=True)
    
    class Meta:
        db_table = 'biomas_especies'

class gremio_alimentario(models.Model):
    id_gremio_alimentario = models.IntegerField('id_gremio_alimentario',primary_key = True) 
    nom_gremio_alimentario = models.CharField('nom_gremio_alimentario',max_length=100,null=True)
    sigla = models.CharField('sigla',max_length=100,null=True)

    class Meta:
        db_table = 'gremio_alimentario'

class especie_gremioalimentario(models.Model):
    id_especie = models.ForeignKey(especies,on_delete= models.CASCADE, null=True)
    id_gremio_alimentario = models.ForeignKey(gremio_alimentario,on_delete= models.CASCADE, null=True)
    
    class Meta:
        db_table = 'especie_gremioalimentario'


class estado_conservacion_cuerpos_agu(models.Model):
    #id_rio = models.IntegerField('id_rio',primary_key = True) 
    codigo = models.CharField('codigo',max_length=100,null=True)
    #bmwp_Col = models.CharField('BMWP_Col',max_length=100,null=True)
    calidad_agua = models.CharField('calidad_agua',max_length=100,null=True)

    class Meta:
        db_table = 'estado_conservacion_cuerpos_agu'

class estudios_pericos(models.Model):
    id_estudioperico = models.IntegerField('id_estudioperico',primary_key = True)
    id_provincia = models.ForeignKey(provincias,on_delete= models.CASCADE, null=True) 
    localidad_especie = models.IntegerField('localidad_especie',null=True)
    numero_pericos_especie = models.IntegerField('numero_pericos_especie',null=True)
    grupo_especie = models.IntegerField('grupo_especie',null=True)
    anio_estudio = models.IntegerField('anio_estudio',null=True)

    class Meta:
        db_table = 'estudios_pericos'

class fisiotopico(models.Model):
    id_fisiotopico = models.IntegerField('id_fisiotopico',primary_key = True)
    nombre_fisiotopico = models.CharField('nombre_fisiotopico',max_length=100,null=True)
    descripcion = models.CharField('descripcion',max_length=100,null=True)
    recomendacion_y_uso = models.CharField('recomendacion_y_uso',max_length=100,null=True)

    class Meta:
        db_table = 'fisiotopico'

class imagenes(models.Model):
    id_imagen = models.IntegerField('id_imagen',primary_key = True)
    imagen = models.CharField('imagen',max_length=100,null=True)
    tipo = models.CharField('tipo',max_length=100,null=True)
    autor = models.CharField('autor',max_length=100,null=True)
    id_especie = models.ForeignKey(especies,on_delete= models.CASCADE, null=True)

    class Meta:
        db_table = 'imagenes'

class imagenes_abundancia(models.Model):
    id_imagen = models.ForeignKey(imagenes,on_delete= models.CASCADE, null=True)
    imagen = models.CharField('imagen',max_length=100,null=True)
    id_abundancia = models.ForeignKey(abundancias,on_delete= models.CASCADE, null=True)

    class Meta:
        db_table = 'imagenes_abundancia'

class infraordenes(models.Model):
    id_infraorden = models.IntegerField('id_infraorden',primary_key = True)
    nom_infraorden = models.CharField('nom_infraorden',max_length=100,null=True)
    id_clase = models.ForeignKey(clases,on_delete= models.CASCADE, null=True)

    class Meta:
        db_table = 'infraordenes'

class linea_corredores_ecologicos(models.Model):
    id_linea = models.IntegerField('id_linea',primary_key = True)
    nom_linea = models.CharField('nom_linea',max_length=100,null=True)
    descripcion_linea = models.CharField('descripcion_linea',max_length=100,null=True)

    class Meta:
        db_table = 'linea_corredores_ecologicos'

class paisajes(models.Model):
    id_paisaje = models.IntegerField('id_paisaje',primary_key = True)
    nom_paisaje = models.CharField('nom_paisaje',max_length=100,null=True)

    class Meta:
        db_table = 'paisajes'

class parroquias_rios(models.Model):
    id_rio = models.ForeignKey(rios,on_delete= models.CASCADE, null=True)
    id_parroquia = models.ForeignKey(parroquias,on_delete= models.CASCADE, null=True)
    id_canton = models.ForeignKey(cantones,on_delete= models.CASCADE, null=True)
    id_provincia = models.ForeignKey(provincias,on_delete= models.CASCADE, null=True)

    class Meta:
        db_table = 'parroquias_rios'

class imagenes_biomas(models.Model):
    id_imagenbioma = models.IntegerField('id_imagenbioma',primary_key = True)
    id_bioma = models.ForeignKey(biomas,on_delete= models.CASCADE, null=True)
    url_imagen = models.CharField('url_imagen',max_length=100,null=True)
    autor = models.CharField('autor',max_length=100,null=True)

    class Meta:
        db_table = 'imagenes_biomas'
#----------------------

class personas(models.Model):
    id_persona = models.IntegerField('id_persona',primary_key = True)
    nom_persona = models.CharField('nom_persona',max_length=100,null=True)
    apre_persona = models.CharField('apre_persona',max_length=100,null=True)
    tipo = models.CharField('tipo',max_length=100,null=True)

    class Meta:
        db_table = 'personas'

class regiones_naturalez(models.Model):
    id_zona = models.IntegerField('id_zona',primary_key = True)
    nom_zona = models.CharField('nom_zona',max_length=100,null=True)
    
    class Meta:
        db_table = 'regiones_naturalez'

class relieves(models.Model):
    id_relieve = models.IntegerField('id_relieve',primary_key = True)
    ubicacion_relieve = models.CharField('ubicacion_relieve',max_length=100,null=True)
    longitud_min = models.CharField('longitud_min',max_length=100,null=True)
    longitud_max = models.CharField('longitud_max',max_length=100,null=True)
    territorio_relieve = models.CharField('territorio_relieve',max_length=100,null=True)

    class Meta:
        db_table = 'relieves'

class servicios_ecosistemicos(models.Model):
    id_servicioecosistemico = models.IntegerField('id_servicioecosistemico',primary_key = True)
    nom_servicioecosistemico = models.CharField('nom_servicioecosistemico',max_length=100,null=True)
    hec_servicioecosistemico = models.FloatField(null=True)
    por_servicioecosistemico = models.FloatField(null=True)
    
    class Meta:
        db_table = 'servicios_ecosistemicos'

class sitios_muestreo_bioecologia(models.Model):
    id_sitio = models.IntegerField('id_sitio',primary_key = True)
    id_canton = models.ForeignKey(cantones,on_delete= models.CASCADE, null=True)
    id_locacion = models.ForeignKey(locaciones,on_delete= models.CASCADE, null=True)
    bioma = models.CharField('bioma',max_length=100,null=True)
    coordenadas = models.CharField('coordenadas',max_length=100,null=True)
    
    class Meta:
        db_table = 'sitios_muestreo_bioecologia'

class subfamilias(models.Model):
    id_subfamilia = models.IntegerField('id_subfamilia',primary_key = True)
    nom_subfamilia =  models.CharField('nom_subfamilia',max_length=100,null=True)
    tipo =  models.CharField('tipo',max_length=100,null=True)
    id_familia = models.ForeignKey(familias,on_delete= models.CASCADE, null=True)
    
    class Meta:
        db_table = 'subfamilias'

class tribu(models.Model):
    id_tribu = models.IntegerField('id_tribu',primary_key = True)
    nom_tribu =  models.CharField('nom_tribu',max_length=100,null=True)
    id_subfamilia =  models.ForeignKey(subfamilias,on_delete= models.CASCADE, null=True)
    
    class Meta:
        db_table = 'tribu'

class subtribu(models.Model):
    id_subtribu = models.IntegerField('id_subtribu',primary_key = True)
    nom_subtribu =  models.CharField('nom_subtribu',max_length=100,null=True)
    id_tribu =  models.ForeignKey(tribu,on_delete= models.CASCADE, null=True)
    
    class Meta:
        db_table = 'subtribu'

class telemetria_pericos(models.Model):
    id_telemetria = models.IntegerField('id_telemetria',primary_key = True)
    num_pericos =  models.IntegerField('num_pericos',null=True)
    cant_telemetria =  models.IntegerField('cant_telemetria',null=True)
    estado_grupo_perico =  models.CharField('estado_grupo_perico',max_length=100,null=True)
    distancia_vuelo_max =  models.CharField('distancia_vuelo_max',max_length=100,null=True)
    distancia_vuelo_promedio =  models.CharField('distancia_vuelo_promedio',max_length=100,null=True)
    tiempo_estancia_bosques_max =  models.CharField('tiempo_estancia_bosques_max',max_length=100,null=True)
    tiempo_estancia_bosques_pro =  models.CharField('tiempo_estancia_bosques_pro',max_length=100,null=True)
    tiempo_estancia_pastos_max =  models.CharField('tiempo_estancia_pastos_max',max_length=100,null=True)
    tiempo_estancia_pastos_pro =  models.CharField('tiempo_estancia_pastos_pro',max_length=100,null=True)
    habitat_bosques =  models.CharField('habitat_bosques',max_length=100,null=True)
    habitat_pasto_arbolado =  models.CharField('habitat_pasto_arbolado',max_length=100,null=True)
    habitat_area_vida_semanal =  models.CharField('habitat_area_vida_semanal',max_length=100,null=True)
    habitat_area_vida_diaria =  models.CharField('habitat_area_vida_diaria',max_length=100,null=True)
    
    class Meta:
        db_table = 'telemetria_pericos'
    
class unidades_fisiotopicos(models.Model):
    id_areanatural = models.ForeignKey(area_naturales_conservacion,on_delete= models.CASCADE, null=True)
    id_fisiotopico = models.ForeignKey(fisiotopico,on_delete= models.CASCADE, null=True)
    hectareas =  models.FloatField(null=True)
    porcentaje =  models.FloatField(null=True)
    
    class Meta:
        db_table = 'unidades_fisiotopicos'

class users(models.Model):
    id_user = models.IntegerField('id_user',primary_key = True)
    email_user = models.CharField('email_user',max_length=100,null=True)
    image_user =  models.CharField('image_user',max_length=100,null=True)
    password_user =   models.CharField('password_user',max_length=100,null=True)
    estado_user =  models.CharField('estado_user',max_length=100,null=True)
    creat_at_user = models.DateTimeField(null=True)
    modif_at_user = models.DateTimeField(null=True)

    class Meta:
        db_table = 'users'

class usuarios_app(models.Model):
    idusuario = models.IntegerField('idusuario',primary_key = True)
    username = models.CharField('username',max_length=100,null=True)
    email =  models.CharField('email',max_length=100,null=True)
    password =  models.CharField('password',max_length=100,null=True)

    class Meta:
        db_table = 'usuarios_app'

class variables_climaticas(models.Model):
    id_variable = models.IntegerField('id_variable',primary_key = True)
    codigo = models.CharField('codigo',max_length=100,null=True)
    variable =  models.CharField('variable',max_length=100,null=True)
    porcentaje =  models.FloatField(null=True)
    importancia = models.FloatField(null=True)

    class Meta:
        db_table = 'variables_climaticas'
    
class zonas_corredor_ecologico(models.Model):
    id_zona = models.IntegerField('id_zona',primary_key = True)
    nombre_zona = models.CharField('nombre_zona',max_length=100,null=True)
    hectarias_zona =  models.FloatField(null=True)
    porcentaje_zona =  models.FloatField(null=True)

    class Meta:
        db_table = 'zonas_corredor_ecologico'

class zonas_vida(models.Model):
    id_zona = models.IntegerField('id_zona',primary_key = True)
    nombre_zona = models.CharField('nombre_zona',max_length=100,null=True)

    class Meta:
        db_table = 'zonas_vida'

class zonificacion_microcuenca_rio_ca(models.Model):
    #id_macrozonas = models.IntegerField('id_macrozonas',primary_key = True)
    nom_macrozonas = models.CharField('nom_macrozonas',max_length=100,null=True)
    recomendacion_de_uso = models.CharField('recomendacion_de_uso',max_length=100,null=True)
    hectara = models.FloatField(null=True)
    porcentaje = models.FloatField(null=True)

    class Meta:
        db_table = 'zonificacion_microcuenca_rio_ca'

"""