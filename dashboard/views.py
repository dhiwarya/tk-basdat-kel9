from django.shortcuts import render

# Create your views here.
def indexDashboardAtlet(request):
    return render(request, 'dashboard_atlet.html')

def indexDashboardPelatih(request):
    return render(request, 'dashboard_pelatih.html')

def indexDashboardUmpire(request):
    return render(request, 'dashboard_umpire.html')