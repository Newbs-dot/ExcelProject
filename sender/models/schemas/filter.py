from pydantic import BaseModel


class FilterSchema(BaseModel):
    class Config:
        arbitrary_types_allowed = True


class Filter(FilterSchema):
    name: str


class FilterCreate(Filter):
    pass
