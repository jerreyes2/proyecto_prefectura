from django.test import TestCase

from proyecto_app.models import bioma
#from configuracion.wsgi import *



# Create your tests here.


# Para testear los filtros
#listar_biomas = bioma.objects.all()
#print(listar_biomas)

f = bioma.objects.filter(sigla_bioma="BPCA")
print(f)


#