from pathlib import Path

import typer
from pydantic_yaml import parse_yaml_file_as

from cordstrap.discord import DiscordClient
from cordstrap.template import Template


def main_command(template_path: Path = Path("server.cordstrap.yaml")) -> None:
    template = parse_yaml_file_as(Template, template_path)
    client = DiscordClient("ABC")
    for channel in template.channels:
        client.create_channel(123, channel)


def main() -> None:
    typer.run(main_command)


if __name__ == "__main__":
    main()
