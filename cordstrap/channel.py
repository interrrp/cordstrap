from typing import Literal

from attrs import define, field, validators


@define(frozen=True)
class Channel:
    name: str = field(validator=validators.matches_re(r"[a-z0-9_-]+"))
    kind: Literal["text", "voice"] = field(
        default="text",
        validator=validators.in_({"text", "voice"}),
    )
    topic: str = field(default="", validator=validators.max_len(1024))
