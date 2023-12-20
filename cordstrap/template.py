from pydantic import BaseModel

from cordstrap.channel import Channel


class Template(BaseModel):
    guild_id: int
    channels: list[Channel]
