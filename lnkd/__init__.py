"""
LNKD - A simple utility adding custom tags to YAML.
"""

from typing import Text

import yaml

from .base import CustomTag
from .tag import LinkedTag
from .loader import LinkedLoader
from .dumper import LinkedDumper


def link(root: Text, output: Text) -> None:
    with open(root, "r") as inputs:
        data = yaml.load(inputs, Loader=LinkedLoader)

    with open(output, "w") as outputs:
        yaml.dump(data, outputs, Dumper=yaml.SafeDumper)


__all__ = ["LinkedTag", "CustomTag", "LinkedLoader", "LinkedDumper"]
