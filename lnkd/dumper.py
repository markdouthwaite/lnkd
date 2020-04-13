from typing import Optional, List, Any

from yaml import SafeDumper

from .tag import LinkedTag
from .utils import _CustomScalarNode


class LinkedDumper(SafeDumper):

    yaml_multi_representers = {
        **SafeDumper.yaml_multi_representers.copy(),
        LinkedTag: LinkedTag.to_yaml,
        _CustomScalarNode: _CustomScalarNode.to_yaml,
    }
