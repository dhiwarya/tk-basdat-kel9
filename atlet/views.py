from django.shortcuts import render

# Create your views here.
def tes_kualifiasi(request):
    return render(request, 'qualification.html')

def ques_kualifikasi(request):
    return render(request, 'question.html')

def daftar_eventS(request):
    return render(request, 'daftarEvent.html')

def daftar_eventK(request):
    return render(request, 'daftarEventK.html')

def daftar_eventE(request):
    return render(request, 'daftarEventE.html')

def daftar_sponsor(request):
    return render(request, 'daftarSponsor.html')