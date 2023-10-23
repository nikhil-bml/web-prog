from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('product/<int:pk>/', views.ProductView.as_view(), name='product'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('terms/', views.TermsView.as_view(), name='terms'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)