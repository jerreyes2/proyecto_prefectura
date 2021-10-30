from django.contrib import admin
#from .models import familia
#admin.site.register(familia)

# Register your models here.

class biomaAdmin (admin.ModelAdmin):
    list_display = ("nom_bioma","sigla_bioma","des_altitudinal_bioma","has_altitudinal_bioma","remanencia","ext_bioma")

from .models import bioma
admin.site.register(bioma, biomaAdmin)




class locacionAdmin (admin.ModelAdmin):
    list_display = ("nom_locacion","sigla_locacion","alt_locacion","nombre_parroquia","nombre_canton","longitud")
    

from .models import locacion
admin.site.register(locacion, locacionAdmin)




class estadoAdmin (admin.ModelAdmin):
    list_display = ("categoria","sigla","descripcion")

from .models import estadoconservacion
admin.site.register(estadoconservacion, estadoAdmin)



class faunaAdmin (admin.ModelAdmin):
    list_display = ("nom_especie","nom_cientifico","nom_ingles","tipo","rango_altitudinal","ubicacion","descripcion")
    #list_filter = ("id_estado_conservacion")
    search_fields = ("nom_especie","nom_cientifico","nom_ingles")
    
from .models import fauna
admin.site.register(fauna, faunaAdmin)


class imagenAdmin (admin.ModelAdmin):
    list_display = ("id_imagen","id_especie","autor","imagen")
    
from .models import imagen_fauna
admin.site.register(imagen_fauna, imagenAdmin)


class faunaLocacionAdmin (admin.ModelAdmin):
    list_display = ("id_especie","id_locacion")
    list_filter = (
        ('id_locacion', admin.RelatedOnlyFieldListFilter),
    )
    #list_filter = ("id_locacion")

from .models import fauna_locacion
admin.site.register(fauna_locacion, faunaLocacionAdmin)

class faunaBiomaAdmin (admin.ModelAdmin):
    list_display = ("id_especie","id_bioma")
    list_filter = (
        ('id_bioma', admin.RelatedOnlyFieldListFilter),
    )
    #list_filter = ('fauna','bioma')
  

from .models import fauna_biomas
admin.site.register(fauna_biomas, faunaBiomaAdmin)


"""
class clasesAdmin (admin.ModelAdmin):
    list_display = ("id_clase","nom_clase","tipo","abund_clase","num_ord_clase")
  
from .models import clases
admin.site.register(clases, clasesAdmin)

class ordenesAdmin (admin.ModelAdmin):
    list_display = ("id_orden","nom_orden","tipo","id_clase")
  
from .models import ordenes
admin.site.register(ordenes, ordenesAdmin)

#---guachamin

class familiasAdmin (admin.ModelAdmin):
    list_display = ("id_familia","nom_familia","tipo","id_orden","id_clase")
  
from .models import familias
admin.site.register(familias, familiasAdmin)

class abundanciasAdmin (admin.ModelAdmin):
    list_display = ("id_abundancia","tax_abundancia","num_abundancia","ran_abundancia","id_familia",
    "id_orden","id_clase")
  
from .models import abundancias
admin.site.register(abundancias, abundanciasAdmin)

class pisos_zeogeograficosAdmin (admin.ModelAdmin):
    list_display = ("id_pisozeogeografico","nom_pisozeogeografico","sigla_pisozeogeografico")
  
from .models import pisos_zeogeograficos
admin.site.register(pisos_zeogeograficos, pisos_zeogeograficosAdmin)

class provinciasAdmin (admin.ModelAdmin):
    list_display = ("id_provincia","nom_provincia")
  
from .models import provincias
admin.site.register(provincias, provinciasAdmin)

class biomasAdmin (admin.ModelAdmin):
    list_display = ("id_bioma","nom_bioma","sigla_bioma","des_altitudinal_bioma","has_altitudinal_bioma",
    "remanencia","ext_bioma","id_provincia")
  
from .models import biomas
admin.site.register(biomas, biomasAdmin)

class ecosistemasAdmin (admin.ModelAdmin):
    list_display = ("id_ecosistema","nom_ecosistema","cod_ecosistema","id_pisozeogeografico","id_bioma")
  
from .models import ecosistemas
admin.site.register(ecosistemas, ecosistemasAdmin)

class abundancias_ecosistemasAdmin (admin.ModelAdmin):
    list_display = ("id_ecosistema","id_abundancia")
  
from .models import abundancias_ecosistemas
admin.site.register(abundancias_ecosistemas, abundancias_ecosistemasAdmin)

class unidades_hidrograficasAdmin (admin.ModelAdmin):
    list_display = ("id_uh","nom_uh","cod_uh","riqueza_uh","abundancia_uh")
  
from .models import unidades_hidrograficas
admin.site.register(unidades_hidrograficas, unidades_hidrograficasAdmin)

class abundancias_uhAdmin (admin.ModelAdmin):
    list_display = ("id_abundancia","id_uh")
  
from .models import abundancias_uh
admin.site.register(abundancias_uh, abundancias_uhAdmin)

class actividadesAdmin (admin.ModelAdmin):
    list_display = (" id_actividad","nom_actividad","sigla_actividad")
  
from .models import actividades
admin.site.register(actividades, actividadesAdmin)

class riosAdmin (admin.ModelAdmin):
    list_display = ("id_rio","nom_rio","categoria")
  
from .models import rios
admin.site.register(rios, riosAdmin)

class bosquesAdmin (admin.ModelAdmin):
    list_display = ("id_bosque","nom_bosque","pro_administrador_bosque","localizacion_area","micro_cuencas",
    "reg_oficial_bosque","hec_bosque","vegetacion_remanente","altitud_max","altitud_min")
  
from .models import bosques
admin.site.register(bosques, bosquesAdmin)

class bosques_riosAdmin (admin.ModelAdmin):
    list_display = ("id_rio","id_bosque")
  
from .models import bosques_rios
admin.site.register(bosques_rios, bosques_riosAdmin)

class arbolesAdmin (admin.ModelAdmin):
    list_display = ("id_arbol","nom_arbol","esp_arbol","alt_arbol","tip_arbol","id_bosque")
  
from .models import arboles
admin.site.register(arboles, arbolesAdmin)

class areasAdmin (admin.ModelAdmin):
    list_display = ("id_area","cat_area","nom_area","fe_creacion","acu_resolucion_area","aut_competente_area",
     "superfici_area","tipo")
  
from .models import areas
admin.site.register(areas, areasAdmin)

class areas_naturales_corredor_ecologAdmin (admin.ModelAdmin):
    list_display = ("id_area_corredor","asp_min_cap_inst","analisis","observaciones")
  
from .models import areas_naturales_corredor_ecolog
admin.site.register(areas_naturales_corredor_ecolog, areas_naturales_corredor_ecologAdmin)

class cantonesAdmin (admin.ModelAdmin):
    list_display = ("id_canton","nom_canton","id_provincia")
  
from .models import cantones
admin.site.register(cantones, cantonesAdmin)

class biomas_cantonesAdmin (admin.ModelAdmin):
    list_display = ("id_bioma","id_canton")
  
from .models import biomas_cantones
admin.site.register(biomas_cantones, biomas_cantonesAdmin)

class biomas_ecosistemasAdmin (admin.ModelAdmin):
    list_display = ("id_bioma","id_ecosistema")
  
from .models import biomas_ecosistemas
admin.site.register(biomas_ecosistemas, biomas_ecosistemasAdmin)

class estado_conservacionAdmin (admin.ModelAdmin):
    list_display = ("id_estado_conservacion","categoria","sigla","descripcion")
  
from .models import estado_conservacion
admin.site.register(estado_conservacion, estado_conservacionAdmin)

class clasificacionAdmin (admin.ModelAdmin):
    list_display = ("id_clasificacion","nom_clasificacion","id_estado_conservacion")
  
from .models import clasificacion
admin.site.register(clasificacion, clasificacionAdmin)

class distribucionesAdmin (admin.ModelAdmin):
    list_display = ("id_distribucion","nom_distribucion","sigla_distribucion")
  
from .models import distribuciones
admin.site.register(distribuciones, distribucionesAdmin)

class nichotroficoAdmin (admin.ModelAdmin):
    list_display = ("id_nicho_trofico","nom_nicho","sigla_nicho","descripcion")
  
from .models import nichotrofico
admin.site.register(nichotrofico, nichotroficoAdmin)

class personasAdmin (admin.ModelAdmin):
    list_display = ("id_persona","nom_persona","ape_pesona","tipo")
  
from .models import personas
admin.site.register(personas, personasAdmin)

class ordenesAdmin (admin.ModelAdmin):
    list_display = ("id_orden","nom_orden","tipo","id_clase")
  
from .models import ordenes
admin.site.register(ordenes, ordenesAdmin)

class migracion_avesAdmin (admin.ModelAdmin):
    list_display = ("id_migracion","nom_migracion","sigla")
  
from .models import migracion_aves
admin.site.register(migracion_aves, migracion_avesAdmin)

class especiesAdmin (admin.ModelAdmin):
    list_display = ("id_especie","nom_especie","tipo","rango_altitudinal","ubicacion","descripcion","nom_cientifico",
    "nom_ingles","id_estado_conservacion","nacional","id_nicho_trofico","id_persona","id_familia","id_orden",
    "id_clase","anio_descubrimiento","id_migracion")
  
from .models import especies
admin.site.register(especies, especiesAdmin)

class canton_areaAdmin (admin.ModelAdmin):
    list_display = ("id_area","id_canton")
  
from .models import canton_area
admin.site.register(canton_area, canton_areaAdmin)

class canton_bosqueAdmin (admin.ModelAdmin):
    list_display = ("id_bosque","id_canton")
  
from .models import canton_bosque
admin.site.register(canton_bosque, canton_areaAdmin)

class canton_ecosistemaAdmin (admin.ModelAdmin):
    list_display = ("id_canton","id_ecosistema")
  
from .models import canton_ecosistema
admin.site.register(canton_ecosistema, canton_ecosistemaAdmin)



#--figueroa

class cantones_rios_Admin (admin.ModelAdmin):
    list_display = ("id_canton","id_rio")
  
from .models import cantones_rios
admin.site.register(cantones_rios, cantones_rios_Admin)



class cantones_unidades_hidrograficas_Admin (admin.ModelAdmin):
    list_display = ("id_uh","id_canton","id_provincia")
  
from .models import cantones_unidades_hidrograficas
admin.site.register(cantones_unidades_hidrograficas, cantones_unidades_hidrograficas_Admin)



class circuitos_integracion_biolog_Admin (admin.ModelAdmin):
    list_display = ("id_circuito","nombre_circuito","desc_circuito")
  
from .models import circuitos_integracion_biolog
admin.site.register(circuitos_integracion_biolog, circuitos_integracion_biolog_Admin)



class endemismos_Admin (admin.ModelAdmin):
    list_display = ("id_endemismo","nom_endemismo","sigla_endemismo")
  
from .models import endemismos
admin.site.register(endemismos, endemismos_Admin)



class registros_Admin (admin.ModelAdmin):
    list_display = ("id_registro","nom_registro","literal")
  
from .models import registros
admin.site.register(registros, registros_Admin)



class parroquias_Admin (admin.ModelAdmin):
    list_display = ("id_parroquias","nom_parroquia","id_canton","id_provincia")
  
from .models import parroquias
admin.site.register(parroquias, parroquias_Admin)



class locaciones_Admin (admin.ModelAdmin):
    list_display = ("id_locacion","nom_locacion","sigla_locacion","alt_locacion",
    "id_parroquia","id_canton","id_provincia","coordenadas","id_bioma","latitud_locacion","longitud_locacion")
  
from .models import locaciones
admin.site.register(locaciones, locaciones_Admin)



class estaciones_muestreos_Admin (admin.ModelAdmin):
    list_display = ("id_em","nom_em","nom_formal_em","cod_em","id_rio","ind_shannon_em")
  
from .models import estaciones_muestreos
admin.site.register(estaciones_muestreos, estaciones_muestreos_Admin)



class localidades_muestreo_Admin (admin.ModelAdmin):
    list_display = ("id_em","num_muestreo","nom_muestreo","des_muestreo","log_muestreo",
    "lat_muestreo", "alt_muestreo","tipo_animal","id_em")
  
from .models import localidades_muestreo
admin.site.register(estaciones_muestreos, estaciones_muestreos_Admin)



class especie_locaciones_Admin (admin.ModelAdmin):
    list_display = ("id_especie","id_locacion")
  
from .models import especie_locaciones
admin.site.register(especie_locaciones, especie_locaciones_Admin)



class especie_registros_Admin (admin.ModelAdmin):
    list_display = ("id_especie","id_registro")
  
from .models import especie_registros
admin.site.register(especie_registros, especie_registros_Admin)



class especies_actividades_Admin (admin.ModelAdmin):
    list_display = ("id_especie","id_actividad")
  
from .models import especies_actividades
admin.site.register(especies_actividades, especies_actividades_Admin)



class especies_distribucion_Admin (admin.ModelAdmin):
    list_display = ("id_especie","id_distribucion")
  
from .models import especies_distribucion
admin.site.register(especies_distribucion, especies_distribucion_Admin)



class especies_localidades_muestreo_Admin (admin.ModelAdmin):
    list_display = ("id_especie","id_muestreo")
  
from .models import especies_localidades_muestreo
admin.site.register(especies_localidades_muestreo, especies_localidades_muestreo_Admin)



class tipos_vegetacion_Admin (admin.ModelAdmin):
    list_display = ("id_tipovegetacion","nom_tipovegetacion","sigla_tipovegetacion")
  
from .models import tipos_vegetacion
admin.site.register(tipos_vegetacion, tipos_vegetacion_Admin)



class especies_tiposvegetacion_Admin (admin.ModelAdmin):
    list_display = ("id_especie","id_tiposvegetacion")
  
from .models import especies_tiposvegetacion
admin.site.register(especies_tiposvegetacion, especies_tiposvegetacion_Admin)



class flora_Admin (admin.ModelAdmin):
    list_display = ("id_flora","nom_flora","tipo","etimologia","diagnosis",
    "comentarios_taxonomicos","distribucion_composicion","autor")
  
from .models import flora
admin.site.register(flora, flora_Admin)



class flora_biomas_Admin (admin.ModelAdmin):
    list_display = ("id_flora","id_bioma")
  
from .models import flora_biomas
admin.site.register(flora_biomas, flora_biomas_Admin)


#--id_flora y uicn_cites tienen # en el modelo
class flora_endemica_amenazada_Admin (admin.ModelAdmin):
    list_display = ("id_flora","nombre_cientifico","uicn_cites")
  
from .models import flora_endemica_amenazada
admin.site.register(flora_endemica_amenazada, flora_endemica_amenazada_Admin)



class flora_imagen_Admin (admin.ModelAdmin):
    list_display = ("id_flora_imagen","imagenflora","tipo_flora","autor_imagen","id_flora")
  
from .models import flora_imagen
admin.site.register(flora_imagen, flora_imagen_Admin)



class flora_locaciones_Admin (admin.ModelAdmin):
    list_display = ("id_flora","id_locacion")
  
from .models import flora_locaciones
admin.site.register(flora_locaciones, flora_locaciones_Admin)



class genero_Admin (admin.ModelAdmin):
    list_display = ("id_genero","nom_genero", "etimologia","diagnosis",
    "comentarios_taxonomicos","distribucion_composicion")
  
from .models import genero
admin.site.register(genero, genero_Admin)



class genero_flora_Admin (admin.ModelAdmin):
    list_display = ("id_flora","id_genero")
  
from .models import genero_flora
admin.site.register(genero_flora, genero_flora_Admin)



class microcuencas_Admin (admin.ModelAdmin):
    list_display = ("id_microcuenca","nom_microcuenca", "sup_km2_microcuenca","zona1_microcuenca","zona2_microcuenca",
    "zona3_microcuenca","zona4_microcuenca","zona5_microcuenca","zona6_microcuenca")
  
from .models import microcuencas
admin.site.register(microcuencas, microcuencas_Admin)



class ordenes_biomas_Admin (admin.ModelAdmin):
    list_display = ("id_orden","id_bioma")
  
from .models import ordenes_biomas
admin.site.register(ordenes_biomas, ordenes_biomas_Admin)



class ordenes_familias_Admin (admin.ModelAdmin):
    list_display = ("id_orden","id_familia","num_generos","num_especies","porcentaje")
  
from .models import ordenes_familias
admin.site.register(ordenes_familias, ordenes_familias_Admin)



class activida_no_permitida_zonas_res_Admin (admin.ModelAdmin):
    list_display = ("id_zona_restauracion","actividades_permitidas")
  
from .models import activida_no_permitida_zonas_res
admin.site.register(activida_no_permitida_zonas_res, activida_no_permitida_zonas_res_Admin)



class actividades_no_permitidad_macro_Admin (admin.ModelAdmin):
    list_display = ("id_zona_macrona","actividades_no_permitidas")
  
from .models import actividades_no_permitidad_macro
admin.site.register(actividades_no_permitidad_macro, actividades_no_permitidad_macro_Admin)



class actividades_no_permitidas_zona_Admin (admin.ModelAdmin):
    list_display = ("id_zona_prot_est","actividades_no_permitidas")
  
from .models import actividades_no_permitidas_zona_
admin.site.register(actividades_no_permitidas_zona_, actividades_no_permitidas_zona_Admin)



class actividades_permitidad_macrona_Admin (admin.ModelAdmin):
    list_display = ("id_zona_macrona","actividades_permitidas")
  
from .models import actividades_permitidad_macrona_
admin.site.register(actividades_permitidad_macrona_, actividades_permitidad_macrona_Admin)



#--ricky

class actividades_permitidad_zonas_coAdmin (admin.ModelAdmin):
    list_display = ("id_zona_conservacion","actividades_permitidas")
  
from .models import actividades_permitidad_zonas_co
admin.site.register(actividades_permitidad_zonas_co, actividades_permitidad_zonas_coAdmin)

class actividades_permitidad_zonas_prAdmin (admin.ModelAdmin):
    list_display = ("id_zona_prot_est","actividades_permitidas")
  
from .models import actividades_permitidad_zonas_pr
admin.site.register(actividades_permitidad_zonas_pr, actividades_permitidad_zonas_prAdmin)

class actividades_permitidad_zonas_reAdmin (admin.ModelAdmin):
    list_display = ("id_zona_restauracion","actividades_permitidas")
  
from .models import actividades_permitidad_zonas_re
admin.site.register(actividades_permitidad_zonas_re, actividades_permitidad_zonas_reAdmin)

class arbol_alimento_pericosAdmin (admin.ModelAdmin):
    list_display = ("id_arbol","especie_arbol","mes_epoca")
  
from .models import arbol_alimento_pericos
admin.site.register(arbol_alimento_pericos, arbol_alimento_pericosAdmin)

class area_naturales_conservacionAdmin (admin.ModelAdmin):
    list_display = ("id_areanatural","nombre_area","desc_area")
  
from .models import area_naturales_conservacion
admin.site.register(area_naturales_conservacion, area_naturales_conservacionAdmin)

class area_vegetalAdmin (admin.ModelAdmin):
    list_display = ("id_areanatural","covertura_vegetal","hectareas","porcentaje")
  
from .models import area_vegetal
admin.site.register(area_vegetal, area_vegetalAdmin)

class geologiasAdmin (admin.ModelAdmin):
    list_display = ("id_geologia","nom_geologia")
  
from .models import geologias
admin.site.register(geologias, geologiasAdmin)

class geomorfologiaAdmin (admin.ModelAdmin):
    list_display = ("id_geomorfologia","nom_geomorfologia")
  
from .models import geomorfologia
admin.site.register(geomorfologia, geomorfologiaAdmin)

class areanatural_geologiaAdmin (admin.ModelAdmin):
    list_display = ("id_areanatural","id_geologia","hec_geologia","porcentaje")
  
from .models import areanatural_geologia
admin.site.register(areanatural_geologia, areanatural_geologiaAdmin)

class areanatural_geomorfologiaAdmin (admin.ModelAdmin):
    list_display = ("id_areanatural","id_geomorfologia","hec_geomorfologia","porcentaje")
  
from .models import areanatural_geomorfologia
admin.site.register(areanatural_geomorfologia, areanatural_geomorfologiaAdmin)

class areanatural_locacionAdmin (admin.ModelAdmin):
    list_display = ("id_areanatural","id_canton","id_parroquia","km_cuadrados","porcentaje")
  
from .models import areanatural_locacion
admin.site.register(areanatural_locacion, areanatural_locacionAdmin)

class suelosAdmin (admin.ModelAdmin):
    list_display = ("id_suelos","nom_suelos")
  
from .models import suelos
admin.site.register(suelos, suelosAdmin)

class areanatural_sueloAdmin (admin.ModelAdmin):
    list_display = ("id_suelos","id_areanatural","hec_geologia","porcentaje")
  
from .models import areanatural_suelo
admin.site.register(areanatural_suelo, areanatural_sueloAdmin)

class ben_corredores_ecologicosAdmin (admin.ModelAdmin):
    list_display = ("id_beneficio","nobre_beneficio","descripcion_beneficio")
  
from .models import ben_corredores_ecologicos
admin.site.register(ben_corredores_ecologicos, ben_corredores_ecologicosAdmin)

class biomas_especiesAdmin (admin.ModelAdmin):
    list_display = ("id_especie","id_bioma")
  
from .models import biomas_especies
admin.site.register(biomas_especies, biomas_especiesAdmin)

class gremio_alimentarioAdmin (admin.ModelAdmin):
    list_display = ("id_gremio_alimentario","nom_gremio_alimentario","sigla")
  
from .models import gremio_alimentario
admin.site.register(gremio_alimentario, gremio_alimentarioAdmin)

class especie_gremioalimentarioAdmin (admin.ModelAdmin):
    list_display = ("id_especie","id_gremio_alimentario")
  
from .models import especie_gremioalimentario
admin.site.register(especie_gremioalimentario, especie_gremioalimentarioAdmin)

class estado_conservacion_cuerpos_aguAdmin (admin.ModelAdmin):
    list_display = ("id_rio","codigo","bmwp_Col","calidad_agua")
  
from .models import estado_conservacion_cuerpos_agu
admin.site.register(estado_conservacion_cuerpos_agu, estado_conservacion_cuerpos_aguAdmin)

class estudios_pericosAdmin (admin.ModelAdmin):
    list_display = ("id_estudioperico","id_provincia","localidad_especie",
    "numero_pericos_especie","grupo_especie","anio_estudio")
  
from .models import estudios_pericos
admin.site.register(estudios_pericos, estudios_pericosAdmin)

class fisiotopicoAdmin (admin.ModelAdmin):
    list_display = ("id_fisiotopico","nombre_fisiotopico","descripcion","recomendacion_y_uso")
  
from .models import fisiotopico
admin.site.register(fisiotopico, fisiotopicoAdmin)

class imagenesAdmin (admin.ModelAdmin):
    list_display = ("id_imagen","imagen","tipo","autor","id_especie")
  
from .models import imagenes
admin.site.register(imagenes, imagenesAdmin)

class imagenes_abundanciaAdmin (admin.ModelAdmin):
    list_display = ("id_imagen","imagen","id_abundancia")
  
from .models import imagenes_abundancia
admin.site.register(imagenes_abundancia, imagenes_abundanciaAdmin)

class infraordenesAdmin (admin.ModelAdmin):
    list_display = ("id_infraorden","nom_infraorden","id_clase")
  
from .models import infraordenes
admin.site.register(infraordenes, infraordenesAdmin)

class linea_corredores_ecologicosAdmin (admin.ModelAdmin):
    list_display = ("id_linea","nom_linea","descripcion_linea")
  
from .models import linea_corredores_ecologicos
admin.site.register(linea_corredores_ecologicos, linea_corredores_ecologicosAdmin)

class paisajesAdmin (admin.ModelAdmin):
    list_display = ("id_paisaje","nom_paisaje")
  
from .models import paisajes
admin.site.register(paisajes, paisajesAdmin)

class parroquias_riosAdmin (admin.ModelAdmin):
    list_display = ("id_rio","id_parroquia","id_canton","id_provincia")
  
from .models import parroquias_rios
admin.site.register(parroquias_rios, parroquias_riosAdmin)

class imagenes_biomasAdmin (admin.ModelAdmin):
    list_display = ("id_imagenbioma","id_bioma","url_imagen","autor")
  
from .models import imagenes_biomas
admin.site.register(imagenes_biomas, imagenes_biomasAdmin)

class personasAdmin (admin.ModelAdmin):
    list_display = ("id_persona","nom_persona","apre_persona","tipo")
  
from .models import personas
admin.site.register(personas, personasAdmin)

class regiones_naturalezAdmin (admin.ModelAdmin):
    list_display = ("id_zona","nom_zona")
  
from .models import regiones_naturalez
admin.site.register(regiones_naturalez, regiones_naturalezAdmin)

class relievesAdmin (admin.ModelAdmin):
    list_display = ("id_relieve","ubicacion_relieve","longitud_min","longitud_max","territorio_relieve")
  
from .models import relieves
admin.site.register(relieves, relievesAdmin)

class servicios_ecosistemicosAdmin (admin.ModelAdmin):
    list_display = ("id_servicioecosistemico","nom_servicioecosistemico",
    "hec_servicioecosistemico","por_servicioecosistemico")
  
from .models import servicios_ecosistemicos
admin.site.register(servicios_ecosistemicos, servicios_ecosistemicosAdmin)

class sitios_muestreo_bioecologiaAdmin (admin.ModelAdmin):
    list_display = ("id_sitio","id_canton","id_locacion","bioma","coordenadas")
  
from .models import sitios_muestreo_bioecologia
admin.site.register(sitios_muestreo_bioecologia, sitios_muestreo_bioecologiaAdmin)

class subfamiliasAdmin (admin.ModelAdmin):
    list_display = ("id_subfamilia","nom_subfamilia","tipo","id_familia")
  
from .models import subfamilias
admin.site.register(subfamilias, subfamiliasAdmin)

class tribuAdmin (admin.ModelAdmin):
    list_display = ("id_tribu","nom_tribu","id_subfamilia")
  
from .models import tribu
admin.site.register(tribu, tribuAdmin)

class subtribuAdmin (admin.ModelAdmin):
    list_display = ("id_subtribu","nom_subtribu","id_tribu")
  
from .models import subtribu
admin.site.register(subtribu, subtribuAdmin)

class telemetria_pericosAdmin (admin.ModelAdmin):
    list_display = ("id_telemetria","num_pericos","cant_telemetria",
    "estado_grupo_perico","distancia_vuelo_max","distancia_vuelo_promedio",
    "tiempo_estancia_bosques_max","tiempo_estancia_bosques_pro","tiempo_estancia_pastos_max",
    "tiempo_estancia_pastos_pro","habitat_bosques","habitat_pasto_arbolado",
    "habitat_area_vida_semanal","habitat_area_vida_diaria")
  
from .models import telemetria_pericos
admin.site.register(telemetria_pericos, telemetria_pericosAdmin)

class unidades_fisiotopicosAdmin (admin.ModelAdmin):
    list_display = ("id_areanatural","id_fisiotopico","hectareas","porcentaje")
  
from .models import unidades_fisiotopicos
admin.site.register(unidades_fisiotopicos, unidades_fisiotopicosAdmin)

class usersAdmin (admin.ModelAdmin):
    list_display = ("id_user","email_user","image_user","password_user",
    "estado_user","creat_at_user","modif_at_user")
  
from .models import users
admin.site.register(users, usersAdmin)

class usuarios_appAdmin (admin.ModelAdmin):
    list_display = ("idusuario","username","email","password")
  
from .models import usuarios_app
admin.site.register(usuarios_app, usuarios_appAdmin)

class variables_climaticasAdmin (admin.ModelAdmin):
    list_display = ("id_variable","codigo","variable","porcentaje","importancia")
  
from .models import variables_climaticas
admin.site.register(variables_climaticas, variables_climaticasAdmin)

class zonas_corredor_ecologicoAdmin (admin.ModelAdmin):
    list_display = ("id_zona","nombre_zona","hectarias_zona","porcentaje_zona")
  
from .models import zonas_corredor_ecologico
admin.site.register(zonas_corredor_ecologico, zonas_corredor_ecologicoAdmin)

class zonas_vidaAdmin (admin.ModelAdmin):
    list_display = ("id_zona","nombre_zona")
  
from .models import zonas_vida
admin.site.register(zonas_vida, zonas_vidaAdmin)

class zonificacion_microcuenca_rio_caAdmin (admin.ModelAdmin):
    list_display = ("id_macrozonas","nom_macrozonas","recomendacion_de_uso","hectara","porcentaje")
  
from .models import zonificacion_microcuenca_rio_ca
admin.site.register(zonificacion_microcuenca_rio_ca, zonificacion_microcuenca_rio_caAdmin)


"""