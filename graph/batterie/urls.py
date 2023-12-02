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

    path('settings', views.settings, name = 'settings'),
    path('results', views.results, name = 'results'),
    path('presentation', views.presentation, name = 'presentation'),
    path('double_pendulum', views.double_pendulum, name = 'double_pendulum'),
    path('game_of_life', views.game_of_life, name = 'game_of_life'),
    path('audio', views.audio, name = 'audio'),
    path('audio_blob', views.audio_blob, name = 'audio_blob'),
    path('random_graph', views.random_graph, name = 'random_graph'),
    path('snake', views.snake, name = 'snake'),
    path('matter', views.matter, name = 'matter'),

]    