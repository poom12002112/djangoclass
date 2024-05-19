from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "products/home.html"

class PortfolioView(TemplateView):
    template_name = "products/portfolio.html"

class ServiceView(TemplateView):
    template_name = "products/service.html"

class BlogView(TemplateView):
    template_name = "products/blog.html"

class AboutView(TemplateView):
    template_name = "products/about.html"

