from typing import Text

from yaml import ScalarNode, SafeDumper, SafeLoader


class _CustomScalarNode(ScalarNode):

    id = "_custom_scalar"

    def __init__(self, value, tag, style=None):
        super().__init__(value=value, tag=tag, style=style)

    @classmethod
    def from_yaml(cls, loader: SafeLoader, suffix, node: ScalarNode):
        if isinstance(node, ScalarNode):
            return _CustomScalarNode(node.value, suffix, style=node.style)
        else:
            raise NotImplementedError("Node: " + str(type(node)))

    @classmethod
    def to_yaml(cls, dumper: SafeDumper, node: ScalarNode) -> Text:
        return dumper.represent_scalar(node.tag, node.value, style=node.style)
