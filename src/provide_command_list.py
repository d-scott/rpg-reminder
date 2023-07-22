from typing import List

from .command_abs import CommandAbs
from .command_print import CommandPrint


def provide_command_list() -> List[CommandAbs]:
    return [CommandPrint()]
