# main/admin.py
from django.contrib import admin
from .models import Scholarship
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms
from .models import models
from .models import SecurityNews
from django.db import models as djmodels
from .models import RegionalArticle
from .models import BusinessArticle

class ScholarshipAdminForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = '__all__'
        formfield_overrides = {
    models.TextField: {'widget': CKEditor5Widget(config_name='default')},
}

class ScholarshipAdmin(admin.ModelAdmin):
    form = ScholarshipAdminForm
    list_display = ('title', 'published_date')
    search_fields = ('title',)

admin.site.register(Scholarship, ScholarshipAdmin)

#security
class SecurityNewsAdminForm(forms.ModelForm):
    class Meta:
        model = SecurityNews
        fields = '__all__'
        formfield_overrides = {
            models.TextField: {'widget': CKEditor5Widget(config_name='default')},
        }

class SecurityNewsAdmin(admin.ModelAdmin):
    form = SecurityNewsAdminForm
    list_display = ('title', 'category', 'published_date')
    search_fields = ('title',)
    list_filter = ('category', 'published_date')

admin.site.register(SecurityNews, SecurityNewsAdmin)

#regional news: 
class RegionalArticleAdminForm(forms.ModelForm):
    class Meta:
        model = RegionalArticle
        fields = '__all__'
        widgets = {
            'body': CKEditor5Widget(config_name='default'),
        }

class RegionalArticleAdmin(admin.ModelAdmin):
    form = RegionalArticleAdminForm
    list_display = ('title', 'region', 'published_date')
    list_filter = ('region', 'published_date')
    search_fields = ('title',)

admin.site.register(RegionalArticle, RegionalArticleAdmin)

#business
# admin.py
from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import BusinessArticle

class BusinessArticleAdminForm(forms.ModelForm):
    class Meta:
        model = BusinessArticle
        fields = '__all__'
        widgets = {
            'body': CKEditor5Widget(config_name='default'),
        }

class BusinessArticleAdmin(admin.ModelAdmin):
    form = BusinessArticleAdminForm
    list_display = ('title', 'category', 'published_date')
    list_filter = ('category', 'published_date')
    search_fields = ('title',)

admin.site.register(BusinessArticle, BusinessArticleAdmin)

