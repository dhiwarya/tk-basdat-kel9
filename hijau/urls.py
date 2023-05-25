from django.urls import path
from .views import *

app_name = "hijau"

urlpatterns = [
    path('', r_ujian_kualifikasi, name='r_ujian_kualifikasi'),
    path('buat/', c_ujian_kualifikasi, name='c_ujian_kualifikasi'),
    path('question/', c_k_ujian_kualifikasi, name='c_k_ujian_kualifikasi'),
    path('riwayat-ujian/', r_k_ujian_kualifikasi,name='r_k_ujian_kualifikasi')
]