#!/usr/bin/env python
import datetime
import json
from pathlib import Path

from pydantic import BaseModel

from utility import time_it


class AccountInfo(BaseModel):
    customer_id: str
    name: str
    email: str
    title: str
    address_1: str
    address_2: str
    city: str
    state: str
    zip_code: str
    membership_level: str
    member_since: str

    def _append_if(self, lst: list[str], label: str, value: str):
        if value:
            lst.append(f"{label}: {value}")

    def human_readable(self) -> str:
        account_lines = []
        self._append_if(account_lines, "Customer ID", self.customer_id)
        self._append_if(account_lines, "Name", self.name)
        self._append_if(account_lines, "Title", self.title)
        self._append_if(account_lines, "Email address", self.email)
        self._append_if(account_lines, "Membership level", self.membership_level)
        self._append_if(account_lines, "Member since",
                        datetime.date.fromisoformat(self.member_since).strftime("%m/%d/%Y"))
        account_lines.append("Postal Addresss:")
        account_lines.append(self.address_1)
        if self.address_2:
            account_lines.append(self.address_2)
        account_lines.append(f"{self.city}, {self.state} {self.zip_code}")
        return "\n".join(account_lines)


def _load_account(customer_id: str):
    try:
        with (open(Path(__file__).parents[0] / f"{customer_id}.json")) as infile:
            return AccountInfo(customer_id=customer_id, **json.load(infile))
    except FileNotFoundError:
        return "Customer not found"


@time_it
def get_user_name(customer_id: str):
    """Mocks a name lookup from the database."""
    return _load_account(customer_id).name


@time_it
def get_customer_info(customer_id: str):
    """Mock API call to gather customer info."""
    return _load_account(customer_id).human_readable()


def create_customer_info_tool(customer_id):
    def customer_info():
        """Get information about a customer's account (aka profile), including their email and postal addresses"""
        return get_customer_info(customer_id)

    return customer_info
