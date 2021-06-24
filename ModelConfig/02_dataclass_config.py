from datetime import datetime

from pydantic import ValidationError
from pydantic.dataclasses import dataclass


class MyConfig:
    max_anystr_length = 10
    validate_assignment = True
    error_msg_templates = {
        'value_error.any_str.max_length': 'max_length:{limit_value}',
    }


@dataclass(config=MyConfig)
class User:
    id: int
    name: str = 'John Doe'
    signup_ts: datetime = None


@dataclass(config=MyConfig)
class Animal:
    id: int
    name: str = 'Foo Bar'


try:
    user = User(id='42', name='Olexander Kostylev')
except ValidationError as e:
    print(e)

try:
    animal = Animal(id=21, name='Very Strong Bear')
except ValidationError as e:
    print(e)

# Both Animal and User have shared config ~ MyConfig
