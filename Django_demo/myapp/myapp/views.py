from django.shortcuts import render

def dash_board(request):
    return render(request, 'dashboard.html')

def home_page(request):
    return render(request, 'Home.html')  # Corrected from 'Home.html' to 'home.html'

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')
