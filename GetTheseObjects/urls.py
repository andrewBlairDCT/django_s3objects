from django.urls import path
from .views import s3_event_webhook

urlpatterns = [
    path('s3-webhook/', s3_event_webhook, name='s3_event_webhook'),
]