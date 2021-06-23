from pydantic import BaseModel, ValidationError, EmailStr, validator, PydanticValueError
from typing import List, Any
from datetime import datetime


class PasswordHashError(PydanticValueError):
    code = 'password hash'
    msg_template = 'Got invalid password hash, got: {wrong_value}'


class User(BaseModel):
    id: int
    email: EmailStr
    password_hash: Any
    registered: datetime
    friend_ids: List[int] = None

    @validator('password_hash')
    def password_hash_contain_zero(cls, v):
        if not '0' in v:
            raise PasswordHashError(wrong_value=v)
            # raise ValueError('Password hash must contain a zero (0)')
        return v


json = '''
{
    "id": 25,
    "email": "khovansky99@gmail.com",
    "password_hash": "lkjlsadfasdklf21j3l4k",
    "registered": "2021-06-23 18:28:55.516874"
}
'''


try:
    user = User.parse_raw(json)
    print(user.json())

except ValidationError as e:
    print(e.errors())
    print(e.json())
    print(str(e))
