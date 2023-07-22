from .bot import Bot
from .provide_command_list import provide_command_list

if __name__ == "__main__":
    command_list = provide_command_list()
    bot = Bot(command_list)
    bot.run()
