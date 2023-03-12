from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        # context['contact'] = Contact.objects.create(name='name',email='email',message='message')
        # context['contact'].save()
        return context

def ContactView(request):
    if request.mothod == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['messahe']
        data=Contact.objects.create(name=name,email=email,message=message)
        data.save() 
        print("contacted")       