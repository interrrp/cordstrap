from pydantic import BaseModel

from cordstrap.channel import Channel


class Template(BaseModel):
    channels: list[Channel]
