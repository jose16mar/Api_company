#from django.shortcuts import render
from django.views import View  # para utilizar las vistas en las rutas

from .models import company  # umportamos el modelo de la base de datos
from django.http import JsonResponse  # convertir en un arvhivo Json de lectura, nuestra respuesta de la API

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

class companyListView(View):

    @method_decorator(csrf_exempt)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):

        if (id>0):
            list_company = list(company.objects.filter(id=id).values())
            if len(list_company)>0:
                datos = { 'message': "Empresa Encontrada", 'companies':  list_company}
            else:
                datos = { 'message': "El ID de la empresa dada no existe"}
            return JsonResponse(datos)
        else:
            list_company = list(company.objects.all().values())
            if len(list_company) > 0 :
                datos = { 'message': "Success", 'companies':  list_company}
            else:
                datos = { 'message': "Comapanies not found..."}
            return JsonResponse(datos)

    def post(self, request):

        nuevo_dato = json.loads(request.body)
        print(nuevo_dato)
        company.objects.create(name=nuevo_dato['name'], email=nuevo_dato['email'], fundador=nuevo_dato['fundador'])
        datos = { 'message': "Su Nueva empresa ha sido registrada exitosamente..."}
        return JsonResponse(datos)

    def put(self, request, id):

        nuevo_dato = json.loads(request.body)  # cargamos los nuevos datos de la empresa, ha modificar
        print(nuevo_dato)
        list_company = list(company.objects.filter(id=id).values())  #filtro, para obtener la empresa especifica con el ID
        if len(list_company)>0:
            company2 = company.objects.get(id=id)
            company2.name = nuevo_dato['name']
            company2.email = nuevo_dato['email']
            company2.fundador = nuevo_dato['fundador']
            company2.save()

            datos = { 'message': "Su Empresa ha sido modificada con exito!!!"}
        else:
            datos = { 'message': "El ID de la empresa dada no existe"}
        return JsonResponse(datos)    

    def delete(self, request, id):
        list_company = list(company.objects.filter(id=id).values())  #filtro, para obtener la empresa especifica con el ID
        if len(list_company)>0:
            company.objects.filter(id=id).delete()

            datos = { 'message': "Su Empresa ha sido eliminada con exito!!!"}
        else:
            datos = { 'message': "El ID de la empresa dada no existe"}
        return JsonResponse(datos)


class companyListName(View):
    def get(self, request, name):

            list_company = list(company.objects.filter(name=name).values())  #filtro, para obtener la empresa especifica con el ID
            if len(list_company)>0:
                datos = { 'message': "Empresa Encontrada", 'companies':  list_company}
            else:
                datos = { 'message': "El ID de la empresa dada no existe"}
            return JsonResponse(datos)