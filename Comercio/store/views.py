from django import views
from django.shortcuts import render
from django.views.generic.base import TemplateView


class Index(TemplateView):
    template_name = "store/index.html"