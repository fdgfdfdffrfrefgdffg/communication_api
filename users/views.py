from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import UserSerializer
# Create your views here.

class AddOrGet(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EditOrDel(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
