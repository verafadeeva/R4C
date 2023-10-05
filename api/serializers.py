from collections import defaultdict
from typing import Union

from django.core.exceptions import ValidationError

ALLOWED_FIELDS = ('model', 'version', 'created')


def serialize_robot_data(data: dict) -> dict:
    errors = defaultdict(list)
    errors.update(validated_name_fields(data))
    try:
        validated_field(data.get('model'), 'model')
    except ValidationError as e:
        for key in e.message_dict.keys():
            errors[key].extend(e.message_dict[key])
    try:
        validated_field(data.get('version'), 'version')
    except ValidationError as e:
        for key in e.message_dict.keys():
            errors[key].extend(e.message_dict[key])

    return errors


def validated_name_fields(data: dict) -> dict:
    errors = {}
    for field in ALLOWED_FIELDS:
        if field not in data.keys():
            errors[field] = ["Обязательное поле"]
    return errors


def validated_field(value: Union[str, None], name_field: str) -> None:
    if not isinstance(value, str):
        raise ValidationError(
            {name_field: "Значение поля должно быть строкой"}
        )
    if len(value) != 2:
        raise ValidationError(
            {name_field: f"Поле '{name_field}' должно содержать 2 символа"}
        )
