from ..models import Player, Team
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def get_players(request):
    players = Player.objects.all()
    players_data = []
    for player in players:
        player_data = {
            'name': player.name,
            'nickname': player.nickname,
            'team': {
                'id': player.team.id,
                'name': player.team.name
            },
            'social_media': {
                'instagram': player.instagram,
                'twitch': player.twitch
            },
        }
        players_data.append(player_data)
    return JsonResponse(players_data, safe=False)

@csrf_exempt
def add_player(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            nickname = data.get('nickname')
            team_id = data.get('team')
            
            social_media = data.get('social_media', {})
            instagram = social_media.get('instagram')
            twitch = social_media.get('twitch')
  
            if team_id:
                try:
                    team = Team.objects.get(id=team_id)
                except Team.DoesNotExist:
                    return JsonResponse({'status': 'error', 'message': 'Team not found.'})
            else:
                team = None

            player = Player.objects.create(name=name, nickname=nickname, team=team, instagram=instagram, twitch=twitch)

            return JsonResponse({'status': 'success', 'player_id': player.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

def remove_player(request, player_id):
    if request.method == 'POST':
        try:
            player = Player.objects.get(id=player_id)
            player.delete()
            return JsonResponse({'status': 'success'})
        except Player.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Player not found.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
