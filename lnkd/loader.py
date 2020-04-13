from typing import TextIO, List
from yaml import SafeLoader, YAMLObject

from .tag import LinkedTag
from .utils import _CustomScalarNode


class LinkedLoader(SafeLoader):

    yaml_constructors = {
        **SafeLoader.yaml_constructors.copy(),
        "!@": LinkedTag.from_yaml,
        "": _CustomScalarNode.from_yaml,
    }
