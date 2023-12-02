import pandas as pd
import json
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, JsonResponse
from .forms import BattForm
from .Func.simu import Simu
from .Func.random_graph import random_data
from django.contrib.staticfiles.storage import staticfiles_storage
import os 
from graph.settings import STATIC_ROOT
from os import listdir
from io import StringIO
import speech_recognition as sr
import wave

def mame(request):
    path = os.path.join(STATIC_ROOT, 'batterie/images')
    P = listdir(path)
    P_tot = [os.path.join('batterie/images', k) for k in P]
    print(P_tot)
    return render(request, "batterie/mame.html", locals())


def settings(request):
    form = BattForm(request.POST or None)
    print("Hors de la boucle")
    
    print(request.POST)
    if form.is_valid():
        
        print("Dans la boucle")

        type_mod = form.cleaned_data['type_mod']
        nb_mod = form.cleaned_data['nb_mod']
        nb_rack = form.cleaned_data['nb_rack']
        c_rate = float(form.cleaned_data['c_rate'])
        nb_jour = form.cleaned_data['nb_jour']
        jour_deb = str(form.cleaned_data['jour_deb'])[0:10]

        h = form.cleaned_data['h']
        mass = form.cleaned_data['mass']
        set_min_c = form.cleaned_data['set_min_c']
        set_max_c = form.cleaned_data['set_max_c']
        set_min_f = form.cleaned_data['set_min_f']
        set_max_f = form.cleaned_data['set_max_f']
        Pclim = float(form.cleaned_data['Pclim'])
        Pchal = float(form.cleaned_data['Pchal'])
        path = os.path.join(STATIC_ROOT, 'batterie/T_Lyon.xls')

        S = Simu()
        S.Simulation(type_mod, nb_mod, nb_rack, c_rate, nb_jour, jour_deb, path, h,
         mass, set_min_c, set_max_c, set_min_f, set_max_f, Pclim, Pchal)
        divk  = []
        div = S.div
        script = S.script
        for key in S.plots :
        	divk.append(div[key])

        return render(request, 'batterie/results.html', locals())
    
    else:
    	print (form.errors)

    return render(request, 'batterie/settings.html', locals())




def results(request):
	return render(request, 'batterie/results.html', locals())

def presentation(request):
    return render(request, 'batterie/presentation.html', locals())

def double_pendulum(request):
    return render(request, 'batterie/double-pendulum-sim.html', locals())

def game_of_life(request):
    return render(request, 'batterie/gameoflife.html', locals())

def snake(request):
    return render(request, 'batterie/snake.html', locals())

def matter(request):
    return render(request, 'batterie/matter.html', locals())


def audio(request) : 

    if request.method =='POST' :
        nbr = request.POST.get('nbr')
        nbr = int(nbr)**2
        return JsonResponse({"nbr" : nbr})

    return render(request, 'batterie/audio.html', locals())


def audio_blob(request) :
    print(request.POST)
    if request.method =='POST' :
        
        langue = request.POST['langue']
        audio_data = request.FILES['audio']
        r = sr.Recognizer()
        audiofile = sr.AudioFile(audio_data)

        with audiofile as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.record(source)
        try :
            if langue == "francais" :
                text = r.recognize_google(audio, language="fr-FR")
            else :
                text = r.recognize_google(audio)
        except :
            text = "Unrecognized audio"
        print(text)

        return JsonResponse({"Text" : text})

    return render(request, 'batterie/audio.html', locals())


def random_graph(request):
    res = random_data(10)
    
    div = res["div"]
    script = res["script"]
    
    # if request.method =='POST' :
    #     return JsonResponse({"script" : script,
    #                          "div": div})

    return render(request, 'batterie/random_graph.html', locals())


