from django.conf import settings
from pyfcm import FCMNotification


def send_notification(registration_id, **kwargs):
    title = kwargs.get('title', '')
    body = kwargs.get('body', '')
    data_message = kwargs.get('data_message', {})
    api_key = getattr(settings, 'FCM_SERVER_KEY', '')
    push_service = FCMNotification(api_key=api_key)
    result = push_service.notify_single_device(registration_id=registration_id,
                                               message_title=title,
                                               message_body=body,
                                               data_message=data_message
                                               )
    return result
