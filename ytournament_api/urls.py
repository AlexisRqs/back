from rest_framework import routers

from .views import TournamentViewSet

api_router = routers.DefaultRouter()
api_router.register('tournaments', TournamentViewSet)