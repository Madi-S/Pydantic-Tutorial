from pydantic import BaseModel, validator


def normalize(name: str) -> str:
    return ' '.join((word.capitalize()) for word in name.split(' '))


class Producer(BaseModel):
    name: str

    # validators
    _normalize_name = validator('name', allow_reuse=True)(normalize)


class Consumer(BaseModel):
    name: str

    # validators
    _normalize_name = validator('name', allow_reuse=True)(normalize)


jeremy = Producer(name='JEremY dArliNg')
bark = Consumer(name='bark antonY')
print(jeremy.name, bark.name)
# Jeremy Darling Bark Antony
