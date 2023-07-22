import os
from typing import List

import discord

from .command_abs import CommandAbs
from .command_parser import CommandParser
from .dotenv import load_env

load_env()


class BotError(Exception):
    """Error raised by the bot"""


class Bot(discord.Client):
    """Class representing the bot"""

    def __init__(self, command_list: List[CommandAbs]) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        self._command_parser = CommandParser(command_list)
        super().__init__(intents=intents)

    def run(self) -> None:
        token = os.getenv("DISCORD_TOKEN")
        if token is not None:
            super().run(token=token)
        else:
            raise BotError("No Token!")

    async def on_message(self, message: discord.Message) -> None:
        print(f"Got message event: {message.content}")
        if message.author == self.user:
            return
        if message.content.startswith("!"):
            command = self._command_parser.parse(message.content)
            if command is not None:
                command.execute(message)
