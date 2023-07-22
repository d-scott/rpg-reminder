from abc import ABC, abstractmethod

from discord import Message


class CommandAbs(ABC):
    """Abstract represenation of a command"""

    command_name: str

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def execute(self, message: Message) -> None:
        pass
