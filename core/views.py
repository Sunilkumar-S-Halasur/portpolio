from django.shortcuts import render,redirect
#from django.contrib.auth.models import User, auth
#from django.contrib import messages
from.models import Contact
from django.http import HttpResponse
#from contact.models import contact
from django.core.exceptions import ValidationError


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
        # context['contact'] = Contact.objects.create(name = 'name', email='email',message='message')
        return context



def saveEnquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Validate the data (you can create a form for this)
        if not name or not email or not message:
            return HttpResponse("Invalid data submitted.")

        # Save the data to the database
        try:
            en = Contact.objects.create(name=name, email=email, message=message)
            en.save()
            success_message = "Your message has been sent successfully."

            return render(request, 'home.html', {'success_message': success_message})
        #     return render(request, "home.html")
        except ValidationError as e:
            return HttpResponse("Error saving data to the database.")