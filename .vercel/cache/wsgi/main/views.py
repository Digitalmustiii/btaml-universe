from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Scholarship
from django.db.models import Q
from .models import SecurityNews
from .models import RegionalArticle
from .models import BusinessArticle
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.conf import settings

# Mapping between region codes and template names
REGION_TEMPLATES = {
    'east': 'main/eastern_african.html',
    'west': 'main/western_african.html',
    'north': 'main/northern_african.html',
    'central': 'main/central_african.html',
    'south': 'main/southern_african.html',
}

def regional_news(request, region):
    if region not in REGION_TEMPLATES:
        raise Http404("Region not found")
    articles = RegionalArticle.objects.filter(region=region).order_by('-published_date')
    return render(request, REGION_TEMPLATES[region], {'regional_news': articles})

def article_detail(request, pk):
    article = get_object_or_404(RegionalArticle, pk=pk)
    related = article.related.exclude(pk=pk)[:3]
    return render(request, 'main/regional_detail.html', {
        'article': article,
        'related_articles': related
    })

def home(request):
    return render(request, 'main/home.html')

# Missing view stubs for legal section
def terms(request):
    return render(request, 'main/terms.html')

def privacy(request):
    return render(request, 'main/privacy.html')

def investment(request):
    return render(request, 'main/investment.html')

def compliance(request):
    return render(request, 'main/compliance.html')

# Mapping between business categories and their templates
BUSINESS_TEMPLATES = {
    'agriculture': ('main/agriculture.html',
                    'Agriculture & Agribusiness',
                    'Discover insights into agriculture and agribusiness across Africa.'),
    'mining_energy': ('main/mining_energy.html',
                       'Mining & Energy',
                       'Explore developments and opportunities in the mining and energy industries.'),
    'technology': ('main/technology.html',
                   'Technology & Fintech',
                   'Stay updated on technology and fintech innovations shaping African markets.'),
    'infrastructure': ('main/infrastructure.html',
                       'Infrastructure & Logistics',
                       'Learn about infrastructure projects and logistics advancements.'),
    'sustainable': ('main/sustainable.html',
                     'Sustainable Business Practices',
                     'Understand sustainable business practices and green initiatives.'),
    'market_entry': ('main/market_entry.html',
                      'Market Entry Strategies',
                      'Find strategies for entering and thriving in new markets.'),
    'risk_management': ('main/risk_management.html',
                         'Risk Management',
                         'Get expert advice on managing risks in business operations.'),
    'market_trends': ('main/market_trends.html',
                       'Market Trends & Analysis',
                       'Analyze the latest market trends and economic data.'),
    'emerging_industries': ('main/emerging_industries.html',
                             'Emerging Industries',
                             'Discover emerging industries and investment opportunities.'),
    'case_studies': ('main/case_studies.html',
                       'Case Studies',
                       'Read case studies showcasing successful business models.'),
}

def business_category(request, category):
    # Ensure valid category
    if category not in BUSINESS_TEMPLATES:
        raise Http404("Category not found")
    template, display, description = BUSINESS_TEMPLATES[category]
    articles = BusinessArticle.objects.filter(category=category).order_by('-published_date')
    return render(request, template, {
        'business_news': articles,
        'category_display': display,
        'category_description': description,
    })

def business_detail(request, pk):
    article = get_object_or_404(BusinessArticle, pk=pk)
    related = article.related.exclude(pk=pk)[:3]
    return render(request, 'main/business_detail.html', {
        'article': article,
        'related_articles': related})

def services(request):
    return render(request, 'main/services.html')

def show_region_news(request, region):
    region_templates = {
        'east': 'main/eastern_african.html',
        'west': 'main/western_african.html',
        'north': 'main/northern_african.html',
        'south': 'main/southern_african.html',
        'central': 'main/central_african.html',
    }

    if region not in region_templates:
        raise Http404("Region not found")

    template_name = region_templates[region]
    return render(request, template_name)

def scholarship_list(request):
    scholarships = Scholarship.objects.all().order_by('-published_date')
    return render(request, 'main/scholarship_list.html', {
        'scholarships': scholarships
    })

def scholarship_detail(request, pk):
    scholarship = get_object_or_404(Scholarship, pk=pk)
    related = scholarship.related.exclude(pk=pk)[:3]
    return render(request, 'main/scholarship_detail.html', {
        'scholarship': scholarship,
        'related_scholarships': related
    })

# Security
def security_list(request):
    security_news = SecurityNews.objects.order_by('-published_date')
    return render(request, 'main/security.html', {'security_news': security_news})

def security_details(request, pk):
    item = get_object_or_404(SecurityNews, pk=pk)
    return render(request, 'main/security_details.html', {'item': item})

# For Newsletter subscription
def newsletter_subscribe(request):
    if request.method == 'POST':
        subscriber = request.POST.get('email')
        
        # Send confirmation email to the recipient
        send_mail(
            subject='📰 New Newsletter Signup',
            message=f'Please add {subscriber} to the BTAML mailing list.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['consultbtaml@gmail.com'],
            fail_silently=False,
        )
        
        # Redirect to the thank you page
        return redirect('subscribe_thanks')
    
    # In case of GET or other methods, redirect to home page
    return redirect('home')

# For the "Thank You" page after subscribing
def thanks_view(request):
    return render(request, 'main/thanks.html')

# Search bar view
def search_results(request):
    query = request.GET.get('q', '').strip()
    results = {
        'regional_articles': [],
        'business_articles': [],
        'scholarships': [],
        'security': [],
        'static_pages': []
    }

    if query:
        # Search Regional Articles
        results['regional_articles'] = RegionalArticle.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query)  # Searching in the 'body' field
        ).order_by('-published_date')

        # Search Business Articles
        results['business_articles'] = BusinessArticle.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query)  # Searching in the 'body' field
        ).order_by('-published_date')

        # Search Scholarships
        results['scholarships'] = Scholarship.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query)  # Searching in the 'body' field instead of 'description'
        ).order_by('-published_date')

        # Search Security News
        results['security'] = SecurityNews.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query)  # Searching in the 'body' field
        ).order_by('-published_date')

        # Static Page Keywords
        static_keywords = {
            'terms': ('Terms of Service', 'terms'),
            'privacy': ('Privacy Policy', 'privacy'),
            'investment': ('Investment Strategy', 'investment'),
            'compliance': ('Compliance Information', 'compliance'),
            'services': ('Our Services', 'services'),
        }

        for key, (title, url_name) in static_keywords.items():
            if query.lower() in key or query.lower() in title.lower():
                results['static_pages'].append({
                    'title': title,
                    'url': url_name
                })

    return render(request, 'main/search_results.html', {
        'query': query,
        'results': results
    })