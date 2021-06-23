from typing import Literal

from pydantic import BaseModel, ValidationError


class Pie(BaseModel):
    flavor: Literal['apple', 'pumpkin']


Pie(flavor='apple')
Pie(flavor='pumpkin')
try:
    Pie(flavor='cherry')
except ValidationError as e:
    print(str(e))
    '''
    1 validation error for Pie
    flavor
      unexpected value; permitted: 'apple', 'pumpkin'
    (type=value_error.const; given=cherry; permitted=('apple', 'pumpkin'))
    '''