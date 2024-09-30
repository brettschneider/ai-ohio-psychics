import os
import sys

import google.generativeai as genai

from google.generativeai import types

import database.account_info
import database.sessions
import database.transactions
from database.account_info import create_customer_info_tool
from database.transactions import create_customer_transactions_tool

DEFAULT_MODEL = "gemini-1.5-flash"


class ChatBot:
    messages = []

    def __init__(self, customer_id: str, model: str = None, api_key=None):
        if not model:
            model = DEFAULT_MODEL
        self.customer_id = customer_id
        self.model = model
        self.api_key = api_key or os.environ.get('GOOGLE_API_KEY')
        self.safety_settings = {
            types.HarmCategory.HARM_CATEGORY_HARASSMENT: types.HarmBlockThreshold.BLOCK_NONE,
            types.HarmCategory.HARM_CATEGORY_HATE_SPEECH: types.HarmBlockThreshold.BLOCK_NONE,
            types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: types.HarmBlockThreshold.BLOCK_NONE,
            types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: types.HarmBlockThreshold.BLOCK_NONE
        }

    def get_client(self, tools):
        genai.configure(api_key=self.api_key)
        model = genai.GenerativeModel(self.model, tools=tools)
        return model

    def load_messages(self):
        self.messages = database.sessions.load_session(self.customer_id)

    def save_messages(self):
        database.sessions.save_session(self.customer_id, self.messages)

    def ask(self, question_prompt: str):
        tools = [
            create_customer_info_tool(self.customer_id),
            create_customer_transactions_tool(self.customer_id)
        ]
        client = self.get_client(tools)
        self.load_messages()
        chat = client.start_chat(history=self.messages, enable_automatic_function_calling=True)
        response = chat.send_message(question_prompt, safety_settings=self.safety_settings)
        self.messages = chat.history
        yield response.text
        self.save_messages()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        username = input("Username: ")
    else:
        username = sys.argv[1]
    chatbot = ChatBot(username)
    while True:
        try:
            question = input("> ")
            if not question: continue
        except EOFError:
            break
        if question.strip().lower() in ['/quit', '/q']:
            break
        for token in chatbot.ask(question):
            sys.stdout.write(token)
            sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.flush()
