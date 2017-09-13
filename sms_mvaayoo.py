import urllib.request
from django.conf import settings


def send_sms(recipient_no, msg_txt):
    user = getattr(settings, 'SMS_USER', '')
    password = getattr(settings, 'SMS_PASSWORD', '')
    senderID = getattr(settings, 'SMS_SENDER_ID', '')
    url = 'http://api.mvaayoo.com/mvaayooapi/MessageCompose?user={0}:{1}' \
          '&senderID={2} SMS&receipientno={3}&dcs=0&msgtxt={4}&state=4'\
        .format(user, password, senderID, recipient_no, msg_txt).replace(" ", "%20")
    with urllib.request.urlopen(url) as response:
        html = response.read().decode("utf-8").replace("\r\n", "")
        status = html.split(',')
        status, result = status[0].split('=')
        return True if result == str(0) else False