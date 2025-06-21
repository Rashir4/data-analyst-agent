from pydantic import BaseModel

class BaseConfig(BaseModel):
    class Config:
        extra = "forbid"
        validate_assignment = True
    