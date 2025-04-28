from ..models import SocialMedia
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def get_medias(request):
    medias = SocialMedia.objects.all()
    medias_data = []
    for media in medias:
        media_data = {
            'id': media.id,
            'name': media.name,
            'link': media.link
        }
        medias_data.append(media_data)
    return JsonResponse(medias_data, safe=False)

@csrf_exempt
def add_media(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            link = data.get('link')
            
            media = SocialMedia.objects.create(name=name, link=link)

            return JsonResponse({'status': 'success', 'media_id': media.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

def remove_media(request, media_id):
    if request.method == 'POST':
        try:
            media = SocialMedia.objects.get(id=media_id)
            media.delete()
            return JsonResponse({'status': 'success'})
        except SocialMedia.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Media not found.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})