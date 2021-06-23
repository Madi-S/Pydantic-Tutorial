from pydantic import BaseModel, create_model, create_model_from_namedtuple, create_model_from_typeddict, validator, ValidationError

DynamicUserModel = create_model('DynamicUserModel', email=(
    str, ...), id=(int, ...), is_admin=False)
# create_model(model_name, ...fields, __validators__ = validators), where validators is a dictionary of 'validator_name' to 'valdiator' pairs


class StaticUserModel(BaseModel):
    email: str
    id: int
    is_admin: bool = False


user1 = DynamicUserModel(email='test@mail.ru', id=55)
user2 = StaticUserModel(email='test@mail.ru', id=55)

print(user1 == user2, DynamicUserModel == StaticUserModel)
# true, false

# Example with validators:


def username_alphanumeric(cls, v):
    assert v.isalnum(), 'must be alphanumeric'
    return v


validators = {
    'username_validator':
    validator('username')(username_alphanumeric)
}

UserModel = create_model(
    'UserModel',
    username=(str, ...),
    __validators__=validators
)

user = UserModel(username='scolvin')
print(user)
# > username='scolvin'

try:
    UserModel(username='scolvi%n')
except ValidationError as e:
    print(e)
    '''
    1 validation error for UserModel
    username
      must be alphanumeric (type=assertion_error)
    '''
