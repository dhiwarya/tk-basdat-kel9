from django.urls import path
from atlet.views import *

app_name = 'atlet'

urlpatterns = [
    path('', tes_kualifiasi, name='tes_kualifikasi'),
    path('question/', ques_kualifikasi, name='ques_kualifikasi'),
    path('daftar-event/', daftar_eventS, name='daftar_eventS'),
    path('pilih/', daftar_eventK, name='daftar_eventK'),
    path('daftar-event-stadium', daftar_eventE, name='daftar_eventE'),
    path('daftar-sponsor/', daftar_sponsor, name='daftar_sponsor')
]