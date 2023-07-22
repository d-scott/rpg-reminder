from discord import Message

from .command_abs import CommandAbs


class CommandPrint(CommandAbs):
    """Test"""

    command_name = "print"

    def __init__(self) -> None:
        self.fstring = "Printing from CommandPrint: {message}"

    def execute(self, message: Message) -> None:
        print(self.fstring.format(message=self._strip_command(message.content)))

    @staticmethod
    def _strip_command(content: str) -> str:
        return content[len("!print ") :]
