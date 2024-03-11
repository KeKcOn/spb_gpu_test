from django.core.exceptions import ValidationError

from .constants import (
    FIRST_SYMBOL_CODE_ERROR,
    LENGTH_PHONE_NUMBER,
    PHONE_NUMBER_SYMBOL_ERROR,
)


def validate_phone_number(value: str = None) -> None:
    '''Валидатор номера телефона.'''
    if value[0] != '7':
        raise ValidationError(FIRST_SYMBOL_CODE_ERROR)
    if len(value) != 11:
        raise ValidationError(LENGTH_PHONE_NUMBER)
    if not value.isdigit():
        raise ValidationError(PHONE_NUMBER_SYMBOL_ERROR)
