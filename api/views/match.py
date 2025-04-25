import requests
from django.core.cache import cache
from django.http import JsonResponse
from requests.exceptions import Timeout, RequestException
import httpx


def get_matches(request, url, cache_key):
    cached_data = cache.get(cache_key)

    if cached_data:
        return JsonResponse(cached_data)

    try:
        headers = {
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        } 
        response = httpx.get(url, headers=headers, timeout=5.0)

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

        cache.set(cache_key, result, timeout=300)  # cache de 5 minutos

        return JsonResponse(result)

    except Timeout:
        return JsonResponse({'error': 'API timeout'}, status=504)

    except RequestException as e:
        return JsonResponse({'error': f'API request failed: {str(e)}'}, status=500)


def get_matches_results(request):
    url = "https://api.draft5.gg/matches?page=1&amount=5&finished=1&featured=0&team=330&showHidden=0"
    return get_matches(request, url, cache_key="matches_results")


def get_next_matches(request):
    url = "https://api.draft5.gg/matches?page=1&amount=5&finished=0&featured=0&team=330&showHidden=0"
    return get_matches(request, url, cache_key="next_matches")
