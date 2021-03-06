from typing import List

from pydantic import BaseModel, parse_obj_as


class Item(BaseModel):
    id: int
    name: str


# `item_data` could come from an API call, eg., via something like:
# item_data = requests.get('https://my-api.com/items').json()
item_data = [{'id': 1, 'name': 'My Item'}, {'id': 11, 'name': 'My Other Item'}]

items = parse_obj_as(List[Item], item_data)
print(items)
# > [Item(id=1, name='My Item'), Item(id=11, name='My Other Item')]
