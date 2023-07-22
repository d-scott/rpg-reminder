from typing import Callable, Dict

from discord import Message


class CommandParser:
    """Class that parses commands sent to the bot"""

    def __init__(self) -> None:
        self.command_dict: Dict[str, Callable[[Message], None]] = {
            "print": lambda message: print(message.content)
        }

    @staticmethod
    def _get_command(message: str) -> str:
        message_stripped_bang = message[1:]
        try:
            command = message_stripped_bang.split(" ", maxsplit=1)[0]
        except IndexError:
            command = ""
        return command

    def parse(self, message: str) -> None | Callable[[Message], None]:
        print("Running parser...")
        command = self._get_command(message)
        print(f"Got command: {command}")
        if command in self.command_dict:
            return self.command_dict[command]
        return None
