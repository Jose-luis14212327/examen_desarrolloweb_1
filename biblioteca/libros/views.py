# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Libros

# Create your views here.


def lista_libros(request):
    result_set = Libros.objects.all()
    context = {"result": result_set}
    return render(request, "lista_libros.html", context)


def detalle_libros(request, id=10):
    result_set = Libros.objects.get(id=id)
    context = {"result": result_set}
    return render(request, "detalle_libro.html", context)
