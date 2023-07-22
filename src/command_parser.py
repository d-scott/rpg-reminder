from typing import Dict, List

from .command_abs import CommandAbs


class CommandParser:
    """Class that parses commands sent to the bot"""

    def __init__(self, command_list: List[CommandAbs]) -> None:
        self.command_dict: Dict[str, CommandAbs] = {}
        for command in command_list:
            self.command_dict.update({command.command_name: command})

    @staticmethod
    def _get_command_name(message: str) -> str:
        message_stripped_bang = message[1:]
        try:
            command = message_stripped_bang.split(" ", maxsplit=1)[0]
        except IndexError:
            command = ""
        return command

    def parse(self, message: str) -> None | CommandAbs:
        print("Running parser...")
        command_name = self._get_command_name(message)
        print(f"Got command: {command_name}")
        if command_name in self.command_dict:
            return self.command_dict[command_name]
        return None
