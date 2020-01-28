from django.shortcuts import render

from rest_framework import viewsets      # add this
from .serializers import TodoSerializer  # add this
from .models import Channels


class TodoView(viewsets.ModelViewSet):   # add this
    serializer_class = TodoSerializer    # add this
    queryset = Channels.objects.all()
