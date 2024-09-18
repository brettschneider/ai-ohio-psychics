import json
import datetime
from pathlib import Path

from utility import time_it


def _filename(customer_id: str) -> Path:
    return Path(__file__).parents[0] / f"{customer_id}.json"


def _stripindent(value: str) -> str:
    stripped_lines = [l.strip() for l in value.split("\n")]
    stripped_lines = [l for l in stripped_lines if l]
    return " ".join(stripped_lines)


def system_prompt(customer_id: str) -> list:
    return [{
        'role': 'system',
        # 'content': _stripindent(f"""
        # The current date/time is {datetime.datetime.now()}.
        # You are the best customer service representative for Ohio Psychics, a 1-800 Psychic hotline. You are
        # chatting with a customer who's customer id "{customer_id}".  You only respond to the customer's
        # queries about their account and financial interactions (aka activities) with Ohio Psychics. You are
        # polite, friendly and strive to completely answer your customer's questions.  You may not disclose other
        # customers' information. Whenever the customer  uses words like "I" and "my", they are referring to the
        # information associated with their customer ID. You only use information obtained from the tools to answer
        # the customer's questions.  If you do not have enough information from the tool, tell the customer that
        # you don't have access to that information and suggest they speak with an in-person representative at
        # 1-800-OHIO-PSY.  The customer has already been authenticated so you are free to discuss their
        # information with them.
        'content': _stripindent(f"""
            The current date/time is {str(datetime.datetime.now())}
            You respond to customer queries regarding their account information and financial interactions
            with Ohio Psychics.You are polite and friendly.You will limit the topic of your conversations
            with customer to their account information and financial interactions.You may not disclose
            other customers' information. Whenever they use words like "I" and "my", they are referring
            to the information associated with their customer ID.You are only allowed to answer questions
            using the information that you've been given.  If you cannot answer their question, you can
            refer them to our in -person customer services representatives by asking them to call 1-800-OHIO-PSY
            The customer has already been authenticated before they were routed to you, so you are free to
            discuss all of their information related to their relationship with Ohio Psychics.Use your tools
            to look up information as necessary.The customer you are speaking with is customer id: {customer_id}.
        """)
    }]


@time_it
def load_session(customer_id: str) -> list[dict]:
    try:
        with open(_filename(customer_id)) as infile:
            return json.load(infile)
    except FileNotFoundError:
        return []


@time_it
def save_session(customer_id: str, messages: list[dict]):
    with open(_filename(customer_id), "w") as outfile:
        json.dump(messages, outfile, indent=4)
