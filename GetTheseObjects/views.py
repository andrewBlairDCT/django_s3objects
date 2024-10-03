import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Image  

@csrf_exempt
def s3_event_webhook(request):
    if request.method == 'POST':
        try:
         
            payload = json.loads(request.body)

            file_name = payload.get('file_name')
            file_url = payload.get('file_url')
            original_file_name = payload.get('original_file_name')
            date_last_modified = payload.get('date_last_modified')
            file_type = payload.get('file_type')

            Image.objects.create( file_name=file_name, 
                                        file_url=file_url, 
                                        original_file_name=original_file_name,
                                        date_last_modified=date_last_modified,
                                        file_type=file_type)

            return JsonResponse({"status": "success"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)
