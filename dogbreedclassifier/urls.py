from django.urls import path
from rest_framework.authtoken import views as rest_framework_views
from . import views

urlpatterns = [
    path('predictImage', views.ImagePrediction.as_view()),
]