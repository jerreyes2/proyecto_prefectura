from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail,BadHeaderError

#from django.template.loader import get_template

#from django.core.mail import EmailMultiAlternatives
#from configuracion.configuracion import settings

from .models import fauna
from .models import bioma
from .models import fauna_biomas

from django.views.generic import DetailView

# Create your views here.

def index(request):
    print("hola")
    return render(request, 'index.html')   

def administracion(request):
    return render(request, "administracion.html")

def inicio(request):
    return render(request, "inicio.html")

fauna_solo = fauna.objects.all()

def especie(request, id_fauna):
    #print(fauna_solo.items(fauna.id_fauna))
    #fauna_unico = fauna.objects.get(id = id_fauna)
    return render(request, "especie.html", {'fauna_solo' : fauna_solo , 'id_fauna' : id_fauna })

def flora(request):
    return render(request, "flora.html")

#def fauna(request):
#    return render(request, "fauna.html")

def fauna(request, id_bioma):
    bioma_solo = bioma.objects.get(id=id_bioma)
    return render(request, "fauna.html", {'bioma_solo' : bioma_solo})

def areasnat(request):
    return render(request, "areasnat.html")

def infoweb(request):
    return render(request, "infoweb.html")


def familia(request):
    return render(request, "familia.html")

def subfamilia(request):
    return render(request, "subFamilia.html")

def galeria(request, id_fauna_biomas, tipo):
    especie_bioma = fauna_biomas.objects.filter(id_bioma_id = id_fauna_biomas)
    #fauna_s = fauna.objects.filter(tipo = "ave")    
    return render(request, "Galería_especie.html", {'especie_bioma' : especie_bioma , 'fauna_solo' : fauna_solo ,'tipo' : tipo })

biomas = bioma.objects.all()

def galeriabioma(request):
   return render(request, "Galería_bioma.html", { 'bioma' : biomas })


def sugerencias(request):
    if request.method == "POST":
        print(request.POST["asunto"])
        print(request.POST["comentario"])
        print(request.POST["email"])
        print(request.POST["celular"])
        print(request.POST["nombre"])
        print(request.POST["apellido"])
        subject =request.POST["asunto"]
        message =request.POST["comentario"]
        email_from = settings.EMAIL_HOST_USER
        to = request.POST["email"]

        try:
             print("hola")
             mailresult = send_mail(subject, "Enviado desde: " + email_from + "\n\n" + message,settings.DEFAULT_FROM_EMAIL, [to], fail_silently=False)
             print(mailresult)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

       # recipient_list = ["gadpeoeloro@gmail.com"]
       # send_mail(subject,message,email_from,recipient_list)

        return render(request, "gracias.html")

        
    return render(request, "sugerencias.html")
     

#alternativo
'''def send_user_mail(user):
    subject = 'Titulo del correo'
    template = get_template('templates/mi_template_correo.html')

    content = template.render({
        'user': user,
    })

    message = EmailMultiAlternatives(subject, #Titulo
                                    ''",
                                    settings..EMAIL_HOST_USER, #Remitente
                                    [user.email]) #Destinatario

    message.attach_alternative(content, 'text/html')
    message.send()
'''

"""
 
  class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = familia.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context
 
 
 
 
 """
