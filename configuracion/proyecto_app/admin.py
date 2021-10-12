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
