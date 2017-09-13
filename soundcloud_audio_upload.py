import datetime
import os
import shutil
import soundcloud
import tempfile
from requests import HTTPError

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class AudioUpload(APIView):

    def handle_uploaded_file(self, source):
        dir_name = getattr(settings, 'FILE_UPLOAD_DIR')
        fd, filepath = tempfile.mkstemp(suffix=source.name, dir=dir_name)
        with open(filepath, 'wb') as dest:
            shutil.copyfileobj(source, dest)
        return filepath

    def post(self, request):
        user_id = request.user.id
        user_name = request.user.username
        file_path = self.handle_uploaded_file(request.data['audio'])
        time = datetime.datetime.now()
        client = soundcloud.Client(client_id=getattr(settings, 'SOUNDCLOUD_API_KEY', ''),
                                   client_secret=getattr(settings, 'SOUNDCLOUD_CLIENT_SECRET', ''),
                                   username=getattr(settings, 'SOUNDCLOUD_USERNAME', ''),
                                   password=getattr(settings, 'SOUNDCLOUD_PASSWORD', '')
                                   )
        token = client.access_token
        client = soundcloud.Client(access_token=token)
        try:
            track = client.post('/tracks', track={
                'title': '%d-%s-%s' % (user_id, user_name, time),
                'sharing': 'public',
                'asset_data': open(file_path, 'rb')
            })
            context = {
                'data': track.permalink_url + '/'
            }
            dt.sleep(5)
            return Response(context)
        except HTTPError:
            return Response({'message': 'Error uploading audio'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        finally:
            os.remove(file_path)