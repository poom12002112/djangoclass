from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),   
    path('portfolio/', views.PortfolioView.as_view(),name='portfolio'),
    path('service/', views.ServiceView.as_view(),name="service"),
    path('blog/', views.BlogView.as_view(),name="blog"),
    path('about/', views.AboutView.as_view(),name="about"),
]