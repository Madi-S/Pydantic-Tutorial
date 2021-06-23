from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, Field


class Model(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    updated: datetime = Field(default_factory=datetime.utcnow)


m1 = Model()
m2 = Model()
print(f'{m1.uid} != {m2.uid}')
#> ea4c0c90-2c4f-41cb-bd35-5d3e3400cf64 != 5df6224f-1ab5-48a0-bbeb-fb2453054496
print(f'{m1.updated} != {m2.updated}')
#> 2021-05-11 20:28:47.761447 != 2021-05-11 20:28:47.761469