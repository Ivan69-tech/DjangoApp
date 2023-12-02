# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def Gaya(request):
    return render(request, "Gaya.html")

def Roger(request):
    return render(request, "Roger.html")

def Blague(request):
    return render(request, "Blague.html")