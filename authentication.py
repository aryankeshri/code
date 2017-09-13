from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from accounts.models import GoUser


def is_authenticate(username, password, link=None):
    """
    Authenticate the user
    1. on the basis of email + password
    2. on the basis of username + password + company link
    :param username: required(email/username)
    :param password: required
    :param link: required
    :return: if success user object, otherwise pass
    """
    try:
        user = GoUser.objects.get(Q(email__iexact=username) |
                                  Q(username__iexact=username,
                                    company__link=link)
                                  )
        if user.check_password(password):
            return user
    except ObjectDoesNotExist:
        pass
