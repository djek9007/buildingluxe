# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView
from index.forms import EmailPostForm
from index.models import About, Service, Portfolio


def IndexView(request):
    about = About.objects.get(id=1)
    service = Service.objects.all().filter(status='published')
    usluga = About.objects.get(id=2)
    portfolio = Portfolio.objects.all().order_by('publish').filter(status='published')
    return render(request, 'index/index.html', {'about':about, 'service': service, 'usluga': usluga, 'portfolio':portfolio})


def AboutView(request):
    about = About.objects.get(id=1)
    return render(request, 'index/about.html', {'about':about})


def ServiceDetailView(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'index/detail_service.html', {'service':service})

class ServiceListView(ListView):
    queryset = Service.objects.all().filter(status='published')
    context_object_name = 'service'
    template_name = 'index/service_list.html'

def Contact(request):
    contact =About.objects.get(id=3)
    sent = False
    form = EmailPostForm(request.POST)
    subject=''
    message=''
    from_email='buildingluxe@mail.ru'
    to_email = 'buildingluxe@mail.ru'
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'Новый запрос от {} с сайта buildingluxe.kz '.format(cd['name'])
            message =  'Контактные данные потенциального заказчика \nИмя: {} \nТелефон: {}\nEmail: {} \nТекст запроса: {}'.format(cd['name'], cd['phone'], cd['email'], cd['message'])
        try:
            send_mail(subject, message, from_email, [to_email], fail_silently=False)
            sent = True
        except:
            send_mail(subject, message, from_email, [to_email], fail_silently=False)
    else:
        form = EmailPostForm()
    return render(request, 'index/contact.html', {'contact':contact, 'form': form, 'sent':sent})

def PortfolioListView(request):
    spisok = About.objects.get(id=4)
    portfolio = Portfolio.objects.all().filter(status='published')
    return render(request, 'index/portfolio_list.html', {'portfolio': portfolio, 'spisok': spisok})

def PortfolioDetailView(request, slug):
    portfolio = get_object_or_404(Portfolio, slug =slug)
    photoitem = portfolio.photoitems.all()
    return  render(request, 'index/portfolio_detail.html', {'portfolio': portfolio, 'photoitems': photoitem})

def PortfolioAll(request):
    spisok = About.objects.get(id=4)
    return render(request, 'index/spisok.html', {'spisok':spisok})