from django.urls import path
from .views import HomeTemplateView,ContactView

urlpatterns = [
    path('', HomeTemplateView.as_view()),
    path('',ContactView),
]
