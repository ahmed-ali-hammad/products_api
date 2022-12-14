from api.serializers import SessionCreateSerializer
from celery import shared_task


@shared_task
def save_session_data(data):
    serializer = SessionCreateSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return
