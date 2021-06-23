from pydantic import BaseModel, Field
from typing import Any, Optional


class RequiredFieldsModel(BaseModel):
    a: int
    b: int = ...
    c: int = Field(...)


class OptionalFieldsModel(BaseModel):
    a: Optional[Any]
    b: Optional[Any] = ...
    c: Optional[Any] = Field(...)
