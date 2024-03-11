import base64
import time

from celery import shared_task
from django.core.files.base import ContentFile

from .models import Event


@shared_task()
def create_event_with_sleep(data):
    image_content = None
    if data.get('image'):
        image_content = base64.b64decode(data.get('image'))
    time.sleep(60)
    event = Event(
        title=data.get('title'),
        description=data.get('description'),
        date=data.get('date'),
    )
    event.save()
    event.organizations.set(data.get('organizations'))
    if image_content:
        event.image.save('image.png', ContentFile(image_content), save=True)
