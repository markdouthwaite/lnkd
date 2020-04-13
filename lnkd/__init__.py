"""
LNKD - A simple utility adding custom tags to YAML.
"""

from functools import partial

from .base import CustomTag
from .tag import LinkedTag
from .loader import LinkedLoader
from .dumper import LinkedDumper


__all__ = ["LinkedTag", "CustomTag", "LinkedLoader", "LinkedDumper"]
