from pydantic import BaseModel


class ConfigSchema(BaseModel):
    class Config:
        arbitrary_types_allowed = True


class Config(ConfigSchema):
    telegram_id: str
    name: str
    file: str


class ConfigCreate(ConfigSchema):
    telegram_id: str
    file: str
