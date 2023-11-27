from pydantic import BaseModel, Field, Extra

class PredictRequestData(BaseModel):
    sepal_length: float = Field(title="sepal_length", description="the length of the sepal in cm")
    sepal_width: float = Field(title="sepal_width",   description="the width of the sepal in cm")

    class Config:
        extra = Extra.forbid
