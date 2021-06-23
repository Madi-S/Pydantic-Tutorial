# Falsy values: False, 0, 'off' ,'f', 'no', 'n'
# True values: True, 1, 'on', 't', 'yes', 'y'
# a bytes which is valid (per the previous rule) when decoded to str
# To define a stricter Boolean model use `StrictBool`

from pydantic import BaseModel


class User(BaseModel):
    is_admin: bool


user1 = User.parse_raw('{"is_admin": "yes"}')
print(user1)

user2 = User.parse_raw('{"is_admin": "y"}')
print(user2)

user3 = User.parse_raw('{"is_admin": true}')
print(user3)

user4 = User.parse_raw('{"is_admin": 1}')
print(user4)
