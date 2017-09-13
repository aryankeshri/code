import json
import urllib.parse
import urllib.request
from django.conf import settings


def textlocal_sms(mobile_no, message):
    user = getattr(settings, 'TEXTLOCAL_USER', '')
    password = getattr(settings, 'TEXTLOCAL_HASH', '')
    senderID = getattr(settings, 'TEXTLOCAL_SENDER', 'SARVAM')
    message = urllib.parse.quote(message)
    data = urllib.parse.urlencode({'username': user, 'hash': password,
                                   'numbers': mobile_no, 'message': message,
                                   'sender': senderID})
    data = data.encode('utf-8')
    request = urllib.request.Request("http://api.textlocal.in/send/?")
    byte_response = urllib.request.urlopen(request, data).read().decode('utf-8')
    response = json.loads(byte_response)
    return True if response['status'] == 'success' else False