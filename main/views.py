from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "main/index.html"
    
class SettingView(TemplateView):
    template_name = "main/setting.html"

