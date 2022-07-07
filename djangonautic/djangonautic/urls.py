from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from articles import views as article_views

urlpatterns = [
    path('articles/',include('articles.urls')),
    path('accounts/',include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('', article_views.article_list, name='home'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)