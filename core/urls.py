from django.urls import path
from . import views#, api_views


urlpatterns = [
    path('feedback/', views.feedback_form, name='feedback_form'),
    path('thanks/', views.feedback_thanks, name='feedback_thanks'),
    path('feedback/list/', views.feedback_list, name='feedback_list'),
]