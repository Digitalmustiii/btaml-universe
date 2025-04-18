from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # News detail view
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),

    # Africa home page (if you have one)
    path('africa/', views.africa, name='africa_home'),

    # Dedicated regional pages that reuse the generic regional_news view.
    # The generic view expects region codes as: east, west, north, south, and central.
    path('africa/eastern/',   views.regional_news, {'region': 'east'},    name='eastern_african'),
    path('africa/western/',   views.regional_news, {'region': 'west'},    name='western_african'),
    path('africa/northern/',  views.regional_news, {'region': 'north'},   name='northern_african'),
    path('africa/southern/',  views.regional_news, {'region': 'south'},   name='southern_african'),
    path('africa/central/',   views.regional_news, {'region': 'central'}, name='central_african'),

   
    # Legal pages
    path('legal/', views.legal, name='legal'),
    path('legal/terms/', views.terms, name='terms'),
    path('legal/privacy/', views.privacy, name='privacy'),
    path('legal/investment/', views.investment, name='investment'),
    path('legal/compliance/', views.compliance, name='compliance'),
    path('legal/contact/', views.contact_legal, name='contact_legal'),

    # Business pages
    path('business/', views.business, name='business'),
    path('business/agriculture/', views.agriculture, name='agriculture'),
    path('business/mining_energy/', views.mining_energy, name='mining_energy'),
    path('business/technology/', views.technology, name='technology'),
    path('business/infrastructure/', views.infrastructure, name='infrastructure'),
    path('business/sustainable/', views.sustainable, name='sustainable'),
    path('business/market_entry/', views.market_entry, name='market_entry'),
    path('business/risk_management/', views.risk_management, name='risk_management'),
    path('business/market_trends/', views.market_trends, name='market_trends'),
    path('business/emerging_industries/', views.emerging_industries, name='emerging_industries'),
    path('business/case_studies/', views.case_studies, name='case_studies'),

    # Additional pages
    path('security/', views.security, name='security'),
    path('services/', views.services, name='services'),
    path('scholarship/', views.scholarship, name='scholarship'),

    # Authentication pages
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),

    
]
