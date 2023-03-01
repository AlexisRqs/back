from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import TournamentSerializer
from .models import Tournament


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer