import json
from pathlib import Path

from utility import time_it


@time_it
def authenticate(username: str, password: str) -> dict | None:
    try:
        with open(Path(__file__).parents[0] / f"{username}.json") as infile:
            account = json.load(infile)
            if password == account.get('password') and account.get('account_enabled'):
                return account
            else:
                return None
        pass
    except FileNotFoundError:
        return None
