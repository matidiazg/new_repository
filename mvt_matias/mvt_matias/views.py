from django.http import HttpResponse
from django.template import loader
from datetime import date, datetime
from relatives.models import Relatives


def show_relative(self):


    relative = Relatives(nombre="Marcos", age="45", dob= "1973-03-09")
    relative.save()
    documentoDeTexto = f"Nombre: {relative.nombre} Edad: {relative.age} Nacimiento: {relative.dob}"

    return HttpResponse(documentoDeTexto)

def new_relative(self, nombre: str = 'relative', age: int = 0, dob: int = 0):

    plantilla = loader.get_template('template.html')

    relative = Relatives(nombre=nombre, age=age, dob=dob)
    relative.save()

    context_dict = {'relative': relative}

    render = plantilla.render(context_dict)
    return HttpResponse(render)


