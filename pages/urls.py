from django.urls import path
from .views import HomePageView, ContatoPageView

urlpatterns = [
    path('contato/', ContatoPageView.as_view(), name='contato'),
    path('', HomePageView.as_view(), name='home'),
]
