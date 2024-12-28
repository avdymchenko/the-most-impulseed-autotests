from pydantic import BaseModel


class Style(BaseModel):
    fontSize: str | None = None
    padding: str | None = None
    width: str | None = None


class SXAttribute(BaseModel):
    margin: str | None = None
    display: str | None = None
    flexDirection: str | None = None


class Option(BaseModel):
    value: str | None = None
    label: str | None = None
    group: str | None = None
    color: str | None = None


class SpotOutputTextCardData(BaseModel):
    name: str | None = None
    text: str | None = None
    large: bool | None = None
    weight: bool | None = None
    fullWidth: bool | None = None
    href: str | None = None
    style: Style | None = None


class BestSelectCardData(BaseModel):
    name: str | None = None
    nopie: bool | None = None
    options: list[Option] | None = None
    isMulti: bool | None = None
    defaultValue: str | list[str] | None = None
    style: dict | None = None


class SpotInputTextCardData(BaseModel):
    name: str | None = None
    title: str | None = None
    defaultValue: str | None = None
    placeholder: str | None = None
    error: str | None = None
    hashed: bool | None = None
    onlyNumber: bool | None = None
    disabled: bool | None = None


class SpotButtonCardData(BaseModel):
    name: str | None = None
    text: str | None = None
    fullWidth: bool | None = None
    submitOnClick: bool | None = None
    redirectOnClick: str | None = None


class SpotOutputTableCardData(BaseModel):
    name: str | None = None
    headers: list[list[str]] | None = None
    nopie: bool | None = None
    use_socketio_support: bool | None = None
    rows: list[list[str]] | None = None
    rowUrls: list[str] | None = None


class CardContent(BaseModel):
    card: str | None = None
    data: (
        SpotOutputTextCardData
        | BestSelectCardData
        | SpotInputTextCardData
        | SpotButtonCardData
        | SpotOutputTableCardData
        | None
    ) = None
    sx: SXAttribute | None = None
    href: str | None = None


class RootContent(BaseModel):
    card: str | None = None
    content: list[CardContent] | None = None
    sx: SXAttribute | None = None
    href: str | None = None


class RootModel(BaseModel):
    card: str | None = None
    content: RootContent | None = None
    sx: SXAttribute | None = None
    href: str | None = None
