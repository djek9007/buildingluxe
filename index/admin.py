# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

# Register your models here.
from index.models import About, Service, PhotoItem, Portfolio

class ServiceAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    body = forms.CharField(required=False, label="Контент страницы", widget=CKEditorUploadingWidget())


    class Meta:
        model = Service
        fields = '__all__'

class PortfolioAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    body = forms.CharField(required=False, label="Контент страницы", widget=CKEditorUploadingWidget())


    class Meta:
        model = Portfolio
        fields = '__all__'

class AboutAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    body = forms.CharField(required=False, label="Контент страницы", widget=CKEditorUploadingWidget())


    class Meta:
        model = About
        fields = '__all__'

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',  'publish', 'status')
    form = AboutAdminForm
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',  'publish', 'status')
    form = ServiceAdminForm
    prepopulated_fields = {"slug": ("title",)}
class PhotoItemInline(admin.TabularInline):
    model = PhotoItem


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):

    list_display = ('title',  'publish', 'status')
    inlines = [PhotoItemInline]
    prepopulated_fields = {"slug": ("title", )}
    form = PortfolioAdminForm


