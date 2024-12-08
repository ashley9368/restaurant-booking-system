from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'core/homepage.html')

def booking_page(request):
    return render(request, 'core/booking.html')

def menu_page(request):
    return render(request, 'core/menu.html')

def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')