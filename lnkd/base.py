from abc import abstractmethod
from typing import Text
from yaml import YAMLObject


class CustomTag(YAMLObject):
    @property
    @abstractmethod
    def symbol(self) -> Text:
        pass
