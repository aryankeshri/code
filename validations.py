import os
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


def image_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extension = ['.jpg', '.png', '.jpeg', '.gif', '.JPG', '.PNG', '.JPEG', '.GIF']
    if not ext.lower() in valid_extension:
        raise ValidationError(_('Unsupported image extension.'))


mobile_regex = RegexValidator(regex=r'^\d{10,13}$',
                              message=_("Please Enter correct Contact no.")
                              )

username_validator = RegexValidator(r'^[a-zA-Z0-9_-]+$',
                                    message=_('Only alphanumric characters are allowed.')
                                    )