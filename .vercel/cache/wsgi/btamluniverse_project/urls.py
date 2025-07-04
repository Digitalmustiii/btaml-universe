# btamluniverse_project/urls.py
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
 path('admin/', admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls')),  # CKEditor 5 upload URLs
    path('', include('main.urls')),                        # your app
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

