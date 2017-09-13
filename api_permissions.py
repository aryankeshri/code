from rest_framework import exceptions

from accounts.models import GoUser
from .encryption import (jwt_decode_handler, crypto_decode)


def has_permission(request):
    if 'HTTP_AUTHORIZATION' in request.META:
        user_id = crypto_decode(
                jwt_decode_handler(
                    request.META['HTTP_AUTHORIZATION']
                )['id']
        )
        user = GoUser.objects.get(id=int(user_id))
        return user
    else:
        raise exceptions.NotAcceptable('Not allowed!!')
