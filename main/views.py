from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import Http404


# Mapping between region codes and template names
REGION_TEMPLATES = {
    'east': 'main/eastern_african.html',
    'west': 'main/western_african.html',
    'north': 'main/northern_african.html',
    'south': 'main/southern_african.html',
    'central': 'main/central_african.html',
}

def regional_news(request, region):
    # Validate region; if not found, return 404
    template_name = REGION_TEMPLATES.get(region)
    if not template_name:
        raise Http404("Region does not exist")

    # Filter articles based on the provided region and published status, then paginate
    articles_list = NewsArticle.objects.filter(region=region, published=True).order_by('-publish_date')
    paginator = Paginator(articles_list, 10)  # Show 10 articles per page
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)

    # Render the appropriate template with the articles
    return render(request, template_name, {'articles': articles})

def home(request):
    return render(request, 'main/home.html')

def africa(request):
    return render(request, 'main/africa.html')

def legal(request):
    return render(request, 'main/legal.html')

def business(request):
    return render(request, 'main/business.html')

# Missing view stubs for legal section
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

# Add stubs for any remaining views referenced in your urls.py (e.g., agriculture, mining_energy, etc.)
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

def security(request):
    return render(request, 'main/security.html')

def services(request):
    return render(request, 'main/services.html')

def scholarship(request):
    return render(request, 'main/scholarship.html')

def register(request):
    return render(request, 'main/register.html')

