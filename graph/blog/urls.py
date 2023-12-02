#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 00:09:48 2020

@author: ivanpouradierduteil
"""

from django.urls import path
from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.index, name = 'youtube'),
    path('post/<id>', views.show, name = 'show'),
    path('add_data', views.add, name = 'add_data'),
    path('suppr_data', views.suppr, name = 'suppr_data'),
    path('image', views.nouveau_contact, name = 'image'),
    path('voir_contacts', views.voir_contacts, name = 'voir_contacts'),
    path('pos_iss', views.ISS, name = 'pos_iss'),
    path('get_ISS_pos', views.get_ISS_pos, name = 'get_ISS_pos'),
    path('chucknorris', views.chucknorris, name = 'chucknorris'),
    path('chucknorris_json', views.chucknorris_json, name = 'chucknorris_json'),
    path('blague2_json', views.blague2_json, name = 'blague2_json'),
    path('suppr_photo/<ok>', views.suppr_photo, name = 'suppr_photo'),
    path('suppr_video/<vid>', views.suppr_video, name = 'suppr_video'),
    

]    