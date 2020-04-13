from io import StringIO
from typing import Text

import requests
from yaml import load, SafeLoader, ScalarNode, SafeDumper

from .base import CustomTag


class LinkedTag(CustomTag):

    symbol = "!@"

    def __init__(self, link: Text) -> None:
        self.link = link

    @staticmethod
    def fetch(url: Text) -> StringIO:
        response = requests.get(url)

        if response.ok:
            return StringIO(response.content.decode("utf-8"))
        else:
            raise requests.HTTPError(
                f"Failed to retrieve linked YAML document. "
                f"{response.status_code}: {response.content}"
            )

    @classmethod
    def from_yaml(cls, loader: SafeLoader, node: ScalarNode) -> Text:

        Loader = type(loader)

        if node.value.startswith("http"):
            with cls.fetch(node.value) as target:
                data = load(target, Loader=Loader)

        else:
            with open(node.value) as target:
                data = load(target, Loader=Loader)

        return data

    @classmethod
    def to_yaml(cls, dumper: SafeDumper, data: "LinkedTag") -> ScalarNode:
        return dumper.represent_scalar(cls.symbol, data.link)

    def __repr__(self) -> Text:
        return f"{self.symbol} {self.link}"
