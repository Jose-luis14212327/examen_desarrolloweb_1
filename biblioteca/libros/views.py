# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Libros

# Create your views here.


def home_libros(request):
    return render(request, "home.html")
