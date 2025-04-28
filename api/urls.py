from django.urls import path
from .views import player, team, match, social_media, news

urlpatterns = [
    path('players/', player.get_players, name='get_players'),
    path('players/add/', player.add_player, name='add_player'),
    path('players/remove/<int:player_id>/', player.remove_player, name='remove_player'),
    path('teams/', team.get_teams, name='get_teams'),
    path('teams/add/', team.add_team, name='add_team'),
    path('matches_results/', match.get_matches_results, name='get_matches_results'),
    path('next_matches/', match.get_next_matches, name='get_next_matches'),
    path('medias/', social_media.get_medias, name='get_medias'),
    path('medias/add/', social_media.add_media, name='add_media'),
    path('medias/remove/<int:media_id>/', social_media.remove_media, name='remove_media'),
    path('news/', news.get_news, name='get_news'),
    path('news/add/', news.add_news, name='add_news'),
    path('news/remove/<int:news_id>/', news.remove_news, name='remove_news'),
] 