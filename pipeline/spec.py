from typing import Literal
from pydantic import BaseModel

class Palette (BaseModel):
    bg: str = "#111111"
    fg: str = "#f5f5f5"
    accent: str = "#ff4d2e"

class DesignSpec(BaseModel):
    format: Literal["poster", "flyer", "invitation"]
    orientation: Literal["portrait", "landscape"] = "portrait"
    title: str
    subtitle: str | None=None
    body: str | None=None
    date: str | None=None
    place: str | None=None
    palette: Palette = Palette()
