from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'Jane Doe'

# id is mandatory
# name is not required by default is 'Jane Doe'


user = User(id='123')
print(user.dict())

# dict() - returns pythonic dictionary
# json() - returns JSON.stringify()
# copy() - returns user object, e.g., `id=123 name='Jane Doe'`
# schema() - returns a representation of a model
# schema_json() - returns a json representation of a model
# parse_raw() - returns object from JSON string
# parse_obj() - returns object from object
# parse_file() - returns object from file path
# from_orm() - returns object from arbitrary class

print(user.copy() == user)
print(user.schema_json())
