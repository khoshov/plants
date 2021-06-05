from django.urls import path

from core.views import PlantCreateView, main

app_name = 'core'

urlpatterns = [
    path('', main, name='list'),
    path('create', PlantCreateView.as_view(), name='create')
]
