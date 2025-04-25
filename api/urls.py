from django.urls import path
from . import views 

urlpatterns = [
    path('players/', views.get_players, name='get_players'),
    path('add_player/', views.add_player, name='add_player'),
    path('get_teams/', views.get_teams, name='get_teams'),
    path('add_team/', views.add_team, name='add_team'),
    path('remove_player/<int:player_id>/', views.remove_player, name='remove_player'),
] 