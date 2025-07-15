from rest_framework import generics
from core.models import Feedback
from .serializers import FeedbackSerializer

class FeedbackListCreateAPIView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer