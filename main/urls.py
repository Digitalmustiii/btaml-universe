from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('africa/', views.africa, name='africa_home'),
    path('africa/eastern/', views.eastern_african, name='eastern_african'),
    path('africa/western/', views.western_african, name='western_african'),
    path('africa/northern/', views.northern_african, name='northern_african'),
    path('africa/southern/', views.southern_african, name='southern_african'),
    path('africa/central/', views.central_african, name='central_african'),
    path('legal/', views.legal, name='legal'),
    path('business/', views.business, name='business'),
    # Business dropdown pages
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
    path('security/', views.security, name='security'),
    path('services/', views.services, name='services'),
    path('scholarship/', views.scholarship, name='scholarship'),
    path('legal/', views.legal, name='legal'),  # You might still have a legal home page.
    # New legal section URLs:
    path('legal/terms/', views.terms, name='terms'),
    path('legal/privacy/', views.privacy, name='privacy'),
    path('legal/investment/', views.investment, name='investment'),
    path('legal/compliance/', views.compliance, name='compliance'),
    path('legal/contact/', views.contact_legal, name='contact_legal'),
    
    # Login and Logout using Django's built-in views:
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # Registration view (custom):
    path('register/', views.register, name='register'),
]
