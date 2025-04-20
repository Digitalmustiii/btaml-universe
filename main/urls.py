from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import search_results

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    # Regional pages
# Regional listing by code
    path('africa/eastern/', views.regional_news, {'region': 'east'}, name='eastern_african'),
    path('africa/western/', views.regional_news, {'region': 'west'}, name='western_african'),
    path('africa/northern/', views.regional_news, {'region': 'north'}, name='northern_african'),
    path('africa/central/', views.regional_news, {'region': 'central'}, name='central_african'),
    path('africa/southern/', views.regional_news, {'region': 'south'}, name='southern_african'),
    # Detail page for a regional article
    path('africa/article/<int:pk>/', views.article_detail, name='regional_article_detail'),
    
    # this is the one the form will reverse()
    path('search/', views.search_results, name='search_results'),

    # Legal pages
    path('legal/terms/', views.terms, name='terms'),
    path('legal/privacy/', views.privacy, name='privacy'),
    path('legal/investment/', views.investment, name='investment'),
    path('legal/compliance/', views.compliance, name='compliance'),

     # Business category pages
  path('business/agriculture/', views.business_category, {'category': 'agriculture'}, name='agriculture'),
    path('business/mining_energy/', views.business_category, {'category': 'mining_energy'}, name='mining_energy'),
    path('business/technology/', views.business_category, {'category': 'technology'}, name='technology'),
    path('business/infrastructure/', views.business_category, {'category': 'infrastructure'}, name='infrastructure'),
    path('business/sustainable/', views.business_category, {'category': 'sustainable'}, name='sustainable'),
    path('business/market_entry/', views.business_category, {'category': 'market_entry'}, name='market_entry'),
    path('business/risk_management/', views.business_category, {'category': 'risk_management'}, name='risk_management'),
    path('business/market_trends/', views.business_category, {'category': 'market_trends'}, name='market_trends'),
    path('business/emerging_industries/', views.business_category, {'category': 'emerging_industries'}, name='emerging_industries'),
    path('business/case_studies/', views.business_category, {'category': 'case_studies'}, name='case_studies'),
    path('business/article/<int:pk>/', views.business_detail, name='business_detail'),

    # Additional pages
    path('services/', views.services, name='services'),
    path('scholarship/', views.scholarship_list, name='scholarship'),
    
    
# Correct scholarship URLs (remove duplicates)
    path('scholarships/', views.scholarship_list,  name='scholarship_list'),
    path('scholarships/<int:pk>/', views.scholarship_detail, name='scholarship_detail'),

    path('ckeditor/', include('ckeditor_uploader.urls')),

  # URL for the newsletter subscription
    path('subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    
    # URL for the "Thank You" page
    path('thanks/', views.thanks_view, name='subscribe_thanks'),

    path('article/<int:pk>/', views.article_detail, name='article_detail'),

    path('security/', views.security_list, name='security'),
    path('security/<int:pk>/', views.security_details, name='security_details'),

    #searchbar url
    path('search/', search_results, name='search_results'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
