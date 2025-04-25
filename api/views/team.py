from ..models import Team
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def get_teams(request):
    teams = Team.objects.all()
    teams_data = []
    for team in teams:
        team_data = {
            'id': team.id,
            'name': team.name
        }
        teams_data.append(team_data)
    return JsonResponse(teams_data, safe=False)

@csrf_exempt
def add_team(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            
            team = Team.objects.create(name=name)

            

            return JsonResponse({'status': 'success', 'team_id': team.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
