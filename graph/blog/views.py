from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .models import Post, Contact
from .forms import ArticleForm, SupprForm, NouveauContactForm
from bokeh.embed import components
from bokeh.models import HoverTool
from .Func.test import get_pos
import json
import requests
import random


def index(request):
    posts = Post.objects.all()
    form = ArticleForm(request.POST)
    if form.is_valid():
    	
    	p = Post()
    	p.title = form.cleaned_data['title']
    	p.body = form.cleaned_data['body']
    	p.save()

    return render(request, 'blog/index.html', {'post' : posts})

def suppr_video(request, vid):
    Post.objects.filter(id = vid).delete()
    return redirect('index')


def show(request, ok):
    post = Post.objects.get(id = ok)
    return render(request, 'blog/show.html', {'post' : post}) 


def add(request):
    posts = Post.objects.all()
    form = ArticleForm(request.POST)
    if form.is_valid():
        print("ok")
        p = Post()
        p.title = form.cleaned_data['title']
        p.body = form.cleaned_data['body']
        p.save()
        return render(request, 'blog/index.html', {'post' : posts})

    return render(request, 'blog/add_data.html', locals())


def suppr(request):
    posts = Post.objects.all()
    form = SupprForm(request.POST)
    if form.is_valid():
        p = Post()
        titre = form.cleaned_data['suppr']
        Post.objects.filter(title = titre).delete()
        return render(request, 'blog/index.html', {'post' : posts})

    return render(request, 'blog/suppr_data.html', locals())


def nouveau_contact(request):
    form = NouveauContactForm(request.POST or None, request.FILES)
    print(request.FILES)
    print("hors_boucle")
    if form.is_valid():
        print("form is valid")
        contact = Contact()
        contact.description = form.cleaned_data["description"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        return render(request, 'blog/voir_contacts.html', {'contacts': Contact.objects.all()})

    return render(request, 'blog/contact_image.html', locals())




def voir_contacts(request):
    return render(request, 'blog/voir_contacts.html', {'contacts': Contact.objects.all()})

def suppr_photo(request, ok):
    Contact.objects.filter(id = ok).delete()
    return redirect('voir_contacts')

def ISS(request):
    pos = get_pos()
    pos = json.dumps(pos)
    return render(request, 'blog/pos_iss.html', locals())



def get_ISS_pos(request):
    pos = get_pos()
    return JsonResponse(pos)

def chucknorris(request):
    r = requests.get("https://api.chucknorris.io/jokes/random").json()
    blague = r["value"]

    id = random.randint(0,115)
    q = requests.get("https://bridge.buddyweb.fr/api/blagues/blagues/" + str(id)).json()
    blague2 = q["blagues"]

    dico = {"blague" : blague, "blague2" : blague2}
    dico = json.dumps(dico)
    
    return render(request, 'blog/chucknorris.html', locals())

def chucknorris_json(request):
    r = requests.get("https://api.chucknorris.io/jokes/random")
    r = r.json()
    blague = {"value" : str(r["value"])}
    return JsonResponse(blague)

def blague2_json(request):
    
    id = random.randint(0,115)
    q = requests.get("https://bridge.buddyweb.fr/api/blagues/blagues/" + str(id)).json()
    blague = {"value" : str(q["blagues"])}
    return JsonResponse(blague)





















