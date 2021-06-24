from pydantic import BaseModel, ValidationError, validator
from typing import List


class User(BaseModel):
    first_name: str
    second_name: str
    email: str
    data: List[str]

    @validator('first_name', 'second_name', pre=True)
    def strip_name(cls, v):
        return v.strip()

    @validator('*')
    def check_all(cls, v):
        if len(v) >= 60:
            raise ValueError(f'{v} should be 60 characters or less')
        return v

    @validator('data', each_item=True)
    def check_letter(cls, v):
        assert not 'x' in v
        return v + ' checked'


user = User(first_name='Jack', second_name='Denmo',
            email='test@mail.ru', data=['55', 'bebebe', 'jjjj'])
print(user.json())

try:
    other_user = User(first_name='lkasdjfl;kasdjfl;asdsadflkjsadflkjsadl;fkjads;flkdjsafl;kdjsaf;ldksajfl;sdakjf;dlsakfjkjfl;', second_name='baba',
                      email='lkasdjfl;ksadjf;lkjadsfl;kjsadl;dlsakfjlaksdfjladskfjlsadkffkjsad;flkjdsl;fkjsad;lfkjsdal;fkjsad;lfkjsadl;fkjsad;lfk', data=['xander ', 'jaxson', 'xraxula'])
except ValidationError as e:
    print(e.errors())

# if * argument applied, every field will undergo the validator
# you can also specify as many fields to validate as you wish: *args
# pre=True means that this validator will be applied in the first place
# each_item=True will take individual values of sequences (list, tuple, dict etc), rather than taking whole sequence as an argument
