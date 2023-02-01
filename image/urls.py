from django.urls import path
from .views import GeneratingImage, LandingPage


urlpatterns = [

    path('', LandingPage.as_view()),
    path('image/', GeneratingImage.as_view(), name='image-generation'),

]