from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Message
from .serializers import MessageSerializer
# Create your views here.

class AddOrGet(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class EditOrDel(RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
