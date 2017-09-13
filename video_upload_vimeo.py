import os
import shutil
import tempfile
import vimeo
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class VideoUpload(APIView):

    def handle_uploaded_file(self, source):
        dir_name = getattr(settings, 'FILE_UPLOAD_DIR')
        fd, filepath = tempfile.mkstemp(suffix=source.name, dir=dir_name)
        with open(filepath, 'wb') as dest:
            shutil.copyfileobj(source, dest)
        return filepath

    def post(self, request):
        key = getattr(settings, 'VIMEO_CLIENT_ID', '')
        secret = getattr(settings, 'VIMEO_CLIENT_SECRET_ID', '')
        token = getattr(settings, 'VIMEO_TOKEN', '')
        v = vimeo.VimeoClient(key=key, secret=secret, token=token)
        file_path = self.handle_uploaded_file(request.data['video'])
        try:
            video_uri = v.upload(file_path)
            if video_uri:
                a = video_uri.split('/')
                dt.sleep(5)
                return Response('https://vimeo.com/{}'.format(a[-1]))
            else:
                return Response(False)
        except OSError:
            pass
        finally:
            os.remove(file_path)
