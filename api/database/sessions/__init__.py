import datetime
import pickle
from pathlib import Path

from utility import time_it


def _filename(customer_id: str) -> Path:
    return Path(__file__).parents[0] / f"{customer_id}.pickle"


def _stripindent(value: str) -> str:
    stripped_lines = [l.strip() for l in value.split("\n")]
    stripped_lines = [l for l in stripped_lines if l]
    return " ".join(stripped_lines)


def system_prompt(customer_id: str) -> dict:
    return {
        'role': 'model',
        'parts': [{
            'text': _stripindent(f"""
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
    }


@time_it
def load_session(customer_id: str) -> list:
    try:
        with open(_filename(customer_id), "rb") as infile:
            return pickle.load(infile)
    except FileNotFoundError:
        return [system_prompt(customer_id)]


@time_it
def save_session(customer_id: str, messages: list):
    with open(_filename(customer_id), "wb") as outfile:
        pickle.dump(messages, outfile)
