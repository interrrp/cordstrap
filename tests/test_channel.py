import pytest

from cordstrap.channel import Channel


def test_name_validation() -> None:
    assert Channel(name="general").name == "general"

    with pytest.raises(ValueError, match="must match regex"):
        Channel(name="General!")


def test_kind_validation() -> None:
    assert Channel(name="general", kind="text").kind == "text"

    with pytest.raises(ValueError, match="must be in"):
        Channel(name="general", kind="invalid")  # type: ignore[arg-type]


def test_topic_validation() -> None:
    assert Channel(name="general", topic="Talk about stuff").topic == "Talk about stuff"

    with pytest.raises(ValueError, match="must be <= 1024"):
        Channel(name="general", topic="x" * 1025)
