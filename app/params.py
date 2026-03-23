from typing import List

from pydantic import BaseModel, Field, ConfigDict

from app.models import LocationInfo


class GetAllBaomingRecordsVariables(BaseModel):
    uid: str
    limit: str


class GetTongjiVariables(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id_: str = Field(alias="_id", serialization_alias="_id")


class CreateBaomingVariables(BaseModel):
    userId: str = Field(..., alias="userId")
    tongjiId: str = Field(..., alias="tongjiId")
    infoKey: List[str] = Field(..., alias="infoKey")
    infoVal: List[str] = Field(..., alias="infoVal")
    signUrl: str = Field(..., alias="signUrl")
    locationInfo: LocationInfo = Field(..., alias="locationInfo")
    no: int
    noLabel: str = Field(..., alias="noLabel")

    class Config:
        populate_by_name = True