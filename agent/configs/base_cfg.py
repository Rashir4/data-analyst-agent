from pydantic import BaseModel

class BaseConfig(BaseModel):
    model_config = {
        "extra":"forbid",
        "validate_assignment": True,
    }