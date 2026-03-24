from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class GraphQLResponseModel(BaseModel):
    # Allow schema drift in GraphQL responses while keeping core fields typed.
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class TongjiIdObject(GraphQLResponseModel):
    id_: str = Field(alias="_id")
    title: str
    isRepeat: bool
    fixedNo: bool
    isRemove: bool
    noName: str | None = None


class BaomingRecord(GraphQLResponseModel):
    id_: str = Field(alias="_id")
    tongjiId: str
    no: int
    noLabel: str
    tongjiIdObject: TongjiIdObject
    infoKey: list[str]
    infoVal: list[str]


class BaomingsResponse(GraphQLResponseModel):
    baomings: list[BaomingRecord]


class TongjiLocationInfo(GraphQLResponseModel):
    name: str
    latitude: float
    longtitude: float


class TongjiLocation(GraphQLResponseModel):
    name: str
    longtitude: float
    latitude: float
    distance: float | int


class AllowSubmitTimeRule(GraphQLResponseModel):
    id_: int | str = Field(alias="_id")
    startTime: str | None = None
    endTime: str | None = None
    notifyTime: str | None = None
    notifyTitle: str | None = None


class Tongji(GraphQLResponseModel):
    id_: str = Field(alias="_id")
    title: str
    content: str | None = None
    noName: str | None = None
    nameLabel: str | None = None
    count: int | None = None
    isRepeat: bool | None = None
    needLocation: bool | None = None
    locationInfos: list[TongjiLocationInfo] = Field(default_factory=list)
    locations: list[TongjiLocation] = Field(default_factory=list)
    allowSubmitTimeRules: list[AllowSubmitTimeRule] = Field(default_factory=list)


class TongjiResponse(GraphQLResponseModel):
    tongji: Tongji


class LocationInfo(BaseModel):
    name: str
    longtitude: float
    lattitude: float


class InfoOption(BaseModel):
    title: Optional[str] = None
    isImage: Optional[bool] = None
    imageUrl: Optional[str] = None
    score: Optional[float] = None


class QuestionOption(BaseModel):
    title: Optional[str] = None


class GroupInfoForm(BaseModel):
    id: Optional[str] = None
    isRemove: Optional[bool] = None
    type: Optional[str] = None
    title: Optional[str] = None
    desc: Optional[str] = None
    order: Optional[int] = None
    required: Optional[bool] = None
    options: Optional[List[str]] = None
    maxSelect: Optional[int] = None
    minSelect: Optional[int] = None
    mediaSourceType: Optional[str] = None
    textareaRow: Optional[int] = None
    limitCharGt: Optional[int] = None
    limitCharlt: Optional[int] = None
    allowOther: Optional[bool] = None
    isOriginal: Optional[bool] = None
    isDownloadOriginal: Optional[bool] = None
    banUpdate: Optional[bool] = None
    privateResult: Optional[bool] = None
    collectAddressType: Optional[str] = None


class FormValGroupFormVal(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    title: Optional[str] = None
    options: Optional[List[str]] = None
    value: Optional[str] = None
    markedValue: Optional[str] = None
    order: Optional[int] = None
    isInfoOption: Optional[bool] = None
    infoOptions: Optional[List[InfoOption]] = None
    isScoreOption: Optional[bool] = None
    questionOptions: Optional[List[QuestionOption]] = None


class FormValGroup(BaseModel):
    id: Optional[str] = None
    formVal: Optional[FormValGroupFormVal] = None


class FormVal(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    title: Optional[str] = None
    options: Optional[List[str]] = None
    value: Optional[str] = None
    markedValue: Optional[str] = None
    order: Optional[int] = None
    isInfoOption: Optional[bool] = None
    infoOptions: Optional[List[InfoOption]] = None
    isScoreOption: Optional[bool] = None
    questionOptions: Optional[List[QuestionOption]] = None
    groupInfoForms: Optional[List[GroupInfoForm]] = None
    collectAddressType: Optional[str] = None
    formValGroups: Optional[List[FormValGroup]] = None


class ShopProductVal(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    price: Optional[float] = None
    count: Optional[int] = None
    tags: Optional[List[str]] = None


class CreatedByUser(BaseModel):
    avatar: Optional[str] = None


class CreateBaomingResponse(BaseModel):
    _id: Optional[str] = None
