import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Image  

@csrf_exempt
def s3_event_webhook(request):
    if request.method == 'POST':
        try:
         
            payload = json.loads(request.body)
      
            for record in payload.get('Records', []):
                if record.get('eventName') == 'ObjectCreated:Put':
                    s3_object_key = record['s3']['object']['key']
                    bucket_name = record['s3']['bucket']['name']
        
                    file_url = f"https://{bucket_name}.s3.amazonaws.com/{s3_object_key}"

           
                    Image.objects.create(image_url=file_url)

            return JsonResponse({"status": "success"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)
