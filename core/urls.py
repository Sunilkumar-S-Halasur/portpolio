from django.urls import path
from .views import HomeTemplateView,saveEnquiry

urlpatterns = [
    path('', HomeTemplateView.as_view()),
    path('save_enquiry/', saveEnquiry,name='' ),
]
