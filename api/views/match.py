from django.core.cache import cache
from django.http import JsonResponse
import requests
from requests.exceptions import RequestException, Timeout

def get_matches_results(request):
    cached_data = cache.get("matches_results")

    if cached_data:
        return JsonResponse(cached_data)

    url = "https://api.draft5.gg/matches?page=1&amount=5&finished=1&featured=0&team=330&showHidden=0"

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MyBot/1.0)"
        }
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()

        data = response.json()
        matches = data['data']['list']

        result = {
            'matches': [
                {
                    'id': match['matchId'],
                    'teamA': match['teamA']['teamName'],
                    'teamB': match['teamB']['teamName'],
                    'tournament': match['tournament']['tournamentName'],
                    'teamA_score': match['seriesScoreA'],
                    'teamB_score': match['seriesScoreB'],
                }
                for match in matches
            ]
        }

        cache.set("matches_results", result, timeout=300)

        return JsonResponse(result)

    except Timeout:
        return JsonResponse({'error': 'API timeout'}, status=504)

    except RequestException as e:
        return JsonResponse({'error': f'API request failed: {str(e)}'}, status=500)
