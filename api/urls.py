from django.urls import path
from .views import FeedbackListCreateAPIView

urlpatterns = [
    path('feedback/', FeedbackListCreateAPIView.as_view(), name='api_feedback'),
]
