from pydantic import BaseModel


class User_(BaseModel):
    id: int
    name: str

    class Config:
        title = 'User'  # Title for generated JSON schema

        # Strip leading and trailing whitespaces for str & byte types
        anystr_strip_whitespace = True

        anystr_lower = True  # Convert all str & byte to lowercase

        min_anystr_length = 5  # Min length for str & byte (0)

        max_anystr_length = 50  # Max length for str & byte (2 ** 16)

        validate_all = True  # Whether to validate field defautls


user = User_(id=55, name='  Daniel          ')
print(user.json(), user.dict(), user.copy())
# {"id": 55, "name": "daniel"} {'id': 55, 'name': 'daniel'} id=55 name='daniel'