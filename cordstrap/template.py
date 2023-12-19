import attrs

from cordstrap.channel import Channel


@attrs.define
class Template:
    channels: list[Channel]
