from django.urls import path
from .views import player, team, match

urlpatterns = [
    path('players/', player.get_players, name='get_players'),
    path('add_player/', player.add_player, name='add_player'),
    path('remove_player/<int:player_id>/', player.remove_player, name='remove_player'),
    path('get_teams/', team.get_teams, name='get_teams'),
    path('add_team/', team.add_team, name='add_team'),
    path('get_matches_results/', match.get_matches_results, name='get_matches_results'),
] 