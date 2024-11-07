from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name= 'core/home.html'
    
    def get(self, request, *args, **keargs):
        return render(request, self.template_name, {'title':'Oposiciones'})

class SamplePageView(TemplateView):
    template_name= 'core/sample.html'