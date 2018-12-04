from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_cantidad(value):
    if value <= 20:
        raise ValidationError(
            _('Error %(value)s es menor a 20'),
            params={'value': value},
        )