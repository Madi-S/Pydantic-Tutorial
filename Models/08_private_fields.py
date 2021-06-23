from typing import ClassVar

from pydantic import BaseModel


class Model(BaseModel):
    _class_var: ClassVar[str] = 'class var value'
    _private_attr: str = 'private attr value'
    name: str

    class Config:
        underscore_attrs_are_private = True


print(Model._class_var)
# > class var value
print(Model._private_attr)
# > <member '_private_attr' of 'Model' objects>

m = Model.parse_raw('{"name": "Madi"}')
print(m.json())
# Only {"name": "Madi"}. Also can be done via exclude
