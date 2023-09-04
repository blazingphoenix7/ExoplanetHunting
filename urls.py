from django.urls import path
from django.urls.resolvers import URLPattern
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('home/',views.home, name='home'),
    path('upload/',views.upload, name='upload'),
    path('home/upload',views.upload, name='home'),
    path('upload/predictExoplanet', views.predictExoplanet,name="predictExoplanet"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)