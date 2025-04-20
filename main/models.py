from django_ckeditor_5.fields import CKEditor5Field
from django.db import models


class Scholarship(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='scholarships/thumbnails/', blank=True, null=True)
    body = CKEditor5Field('Text', config_name='default')

    related = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.title
        

    
#security:
SECURITY_CATEGORIES = [
    ('regional', 'Regional Security Alerts'),
    ('cyber', 'Cybersecurity Threats'),
    ('business_risk', 'Business Risk & Mitigation'),
    ('policy', 'Government & Policy Updates'),
    ('fraud', 'Fraud & Scams'),
    ('breach', 'Data Breaches & Privacy'),
    ('infra', 'Infrastructure & Critical Systems'),
    ('intel', 'Surveillance & Intelligence'),
    ('innovation', 'Tech & Security Innovations in Africa'),
    ('terror', 'Terrorism & Insurgency'),
    ('partners', 'Security Partnerships & Collaborations'),
    ('emergency', 'Emergency Response & Disaster Preparedness'),
    ('compliance', 'Regulatory Compliance & Legal Risks'),
]

class SecurityNews(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=SECURITY_CATEGORIES)
    published_date = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='security/thumbnails/', blank=True, null=True)
    body = CKEditor5Field('Text', config_name='default')
    related = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.title

    
    # models.py for regional news
REGION_CHOICES = [
    ('east', 'Eastern African Region'),
    ('west', 'Western African Region'),
    ('north', 'Northern African Region'),
    ('central', 'Central African Region'),
    ('south', 'Southern African Region'),
]

class RegionalArticle(models.Model):
    title = models.CharField(max_length=255)
    region = models.CharField(max_length=10, choices=REGION_CHOICES)
    published_date = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='regional/thumbnails/', blank=True, null=True)
    body = CKEditor5Field('Text', config_name='default')
    related = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return f"{self.get_region_display()}: {self.title}"
    
    #models for business
   # Define your business categories
BUSINESS_CATEGORIES = [
    ('agriculture', 'Agriculture & Agribusiness'),
    ('mining_energy', 'Mining & Energy'),
    ('technology', 'Technology & Fintech'),
    ('infrastructure', 'Infrastructure & Logistics'),
    ('sustainable', 'Sustainable Business Practices'),
    ('market_entry', 'Market Entry Strategies'),
    ('risk_management', 'Risk Management'),
    ('market_trends', 'Market Trends & Analysis'),
    ('emerging_industries', 'Emerging Industries'),
    ('case_studies', 'Case Studies'),
]

class BusinessArticle(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(
        max_length=20,
        choices=BUSINESS_CATEGORIES,
        help_text='Select the business category'
    )
    published_date = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(
        upload_to='business/thumbnails/',
        blank=True,
        null=True
    )
    body = CKEditor5Field('Text', config_name='default')
    related = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return f"{self.get_category_display()}: {self.title}"
    
    #models for search bar
    