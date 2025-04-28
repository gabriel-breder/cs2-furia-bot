from ..models import News
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def get_news(request):
    news = News.objects.all()
    news_data = []
    for item in news:
        item_data = {
            'title': item.title,
            'date': item.date.strftime('%Y-%m-%d'),
            'link': item.link,
        }
        news_data.append(item_data)
    return JsonResponse(news_data, safe=False)

@csrf_exempt
def add_news(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            date = data.get('date')
            link = data.get('link')

            news_item = News.objects.create(title=title, link=link, date=date)

            return JsonResponse({'status': 'success', 'news_id': news_item.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

def remove_news(request, news_id):
    if request.method == 'POST':
        try:
            news_item = News.objects.get(id=news_id)
            news_item.delete()
            return JsonResponse({'status': 'success'})
        except News.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'News item not found.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
