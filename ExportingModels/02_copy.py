from pydantic import BaseModel


class BarModel(BaseModel):
    whatever: int


class FooBarModel(BaseModel):
    banana: float
    foo: str
    bar: BarModel


m = FooBarModel(banana=3.14, foo='hello', bar={'whatever': 123})

print(m.copy(include={'foo', 'bar'}))
# foo='hello' bar=BarModel(whatever=123)
print(m.copy(exclude={'foo', 'bar'}))
# banana=3.14
print(m.copy(update={'banana': 0}))
# banana=0 foo='hello' bar=BarModel(whatever=123)
print(id(m.bar), id(m.copy().bar))
# 140151785612288 140151785612288
# normal copy gives the same object reference for `bar`
print(id(m.bar), id(m.copy(deep=True).bar))
# 140151785612288 140151787189152
# deep copy gives a new object reference for `bar`

'''
Args for .copy methdo:

include: fields to include in the returned dictionary

exclude: fields to exclude from the returned dictionary

update: a dictionary of values to change when creating the copied model

deep: whether to make a deep copy of the new model; default False
'''
