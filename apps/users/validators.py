from django.core import validators
from django.utils.deconstruct import deconstructible


@deconstructible
class PhoneNumberValidator(validators.RegexValidator):
    regex = r"^\+998\d{9}$"
    message = "Pleace enter you phone number in +998xxxxxxxxx format."
    flags = 0
