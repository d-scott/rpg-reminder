import os
from pathlib import Path

ENV_FILE = Path(__file__).parents[1] / ".env"


def load_env() -> None:
    contents = ENV_FILE.read_text(encoding="utf-8")
    variable_list = contents.splitlines()
    for variable in variable_list:
        key, value = variable.split("=", maxsplit=1)
        os.environ[key] = value
