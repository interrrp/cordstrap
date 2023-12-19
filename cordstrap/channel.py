from typing import Literal

from pydantic import BaseModel, Field


class Channel(BaseModel):
    name: str = Field(pattern="^[a-z0-9-]+$")
    kind: Literal["text", "voice"] = "text"
    topic: str = Field(default="", max_length=1024)
