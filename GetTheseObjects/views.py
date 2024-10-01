from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Image
import json

class ImageView(View):
    
    def get(self, request):
        imageData = Image.objects.all().values("id", "name", "type", "created")
        image_list = list(imageData) 
        return JsonResponse(image_list_list, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)
            image = Image.objects.create(
                name=data.get("name"),
                type=data.get("type"),
                created=data.get("created")
            )
            return JsonResponse({
                "id": image.id,
                "name": image.name,
                "type": image.type,
                "created": image.created
            }, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

