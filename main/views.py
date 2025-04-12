from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # For user registration form
from django.contrib import messages  # For sending messages to the user



def home(request):
    return render(request, 'main/home.html')

def africa(request):
    return render(request, 'main/africa.html')

def eastern_african(request):
    return render(request, 'main/eastern_african.html')

def western_african(request):
    return render(request, 'main/western_african.html')

def northern_african(request):
    return render(request, 'main/northern_african.html')

def southern_african(request):
    return render(request, 'main/southern_african.html')

def central_african(request):
    return render(request, 'main/central_african.html')

def legal(request):
    return render(request, 'main/legal.html')

def business(request):
    return render(request, 'main/business.html')

def security(request):
    return render(request, 'main/security.html')

def services(request):
    return render(request, 'main/services.html')

def scholarship(request):
    return render(request, 'main/scholarship.html')
def agriculture(request):
    return render(request, 'main/agriculture.html')

def mining_energy(request):
    return render(request, 'main/mining_energy.html')

def technology(request):
    return render(request, 'main/technology.html')

def infrastructure(request):
    return render(request, 'main/infrastructure.html')

def sustainable(request):
    return render(request, 'main/sustainable.html')

def market_entry(request):
    return render(request, 'main/market_entry.html')

def risk_management(request):
    return render(request, 'main/risk_management.html')

def market_trends(request):
    return render(request, 'main/market_trends.html')

def emerging_industries(request):
    return render(request, 'main/emerging_industries.html')

def case_studies(request):
    return render(request, 'main/case_studies.html')
def terms(request):
    return render(request, 'main/terms.html')

def privacy(request):
    return render(request, 'main/privacy.html')

def investment(request):
    return render(request, 'main/investment.html')

def compliance(request):
    return render(request, 'main/compliance.html')

def contact_legal(request):
    return render(request, 'main/contact_legal.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the user to the database
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})