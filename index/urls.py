# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from index.views import IndexView, AboutView, ServiceListView, Contact, PortfolioListView, PortfolioDetailView, PortfolioAll, ServiceDetailView

urlpatterns = [
    path('', IndexView, name='home' ),
    path('about/', AboutView, name ='about'),
    path('service/<slug:slug>/', ServiceDetailView, name='service_detail'),
    path('service/', ServiceListView.as_view(), name='services'),
    path('contact/', Contact, name='contact'),
    path('portfolio/', PortfolioListView, name='portfolio'),
    path('portfolio/all/', PortfolioAll, name='portfolio_all'),
    path('portfolio/<slug:slug>/', PortfolioDetailView, name='portfolio_detail'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
