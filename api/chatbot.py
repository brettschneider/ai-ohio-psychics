import sys

import ollama

import database.account_info
import database.sessions
import database.transactions

DEFAULT_MODEL = "llama3.1"


class ChatBot:
    messages = []

    def __init__(self, customer_id: str, model: str = None):
        if not model:
            model = DEFAULT_MODEL
        self.customer_id = customer_id
        self.model = model
        self.client = ollama.Client()
        self.load_messages()
        self.tools = [
            database.account_info.TOOL_DEF,
            database.transactions.TOOL_DEF,
        ]

    def load_messages(self):
        self.messages = database.sessions.load_session(self.customer_id)

    def save_messages(self):
        database.sessions.save_session(self.customer_id, self.messages)

    def prepare_messages(self, question_prompt: str = None):
        if question_prompt:
            self.messages.append({
                'role': 'user',
                'content': question_prompt
            })
        return database.sessions.system_prompt(self.customer_id) + self.messages[-25:]

    def ask(self, question_prompt: str):
        messages = self.prepare_messages(question_prompt)
        initial_response = self.client.chat(
            model=self.model,
            messages=messages,
            tools=self.tools
        )
        self.messages.append(initial_response['message'])

        if not initial_response['message'].get('tool_calls'):
            yield initial_response['message']['content']
            return

        if initial_response['message'].get('tool_calls'):
            available_functions = {
                'get_customer_info': database.account_info.get_customer_info,
                'get_customer_transactions': database.transactions.get_customer_transactions,
            }
            for tool in initial_response['message']['tool_calls']:
                function_to_call = available_functions[tool['function']['name']]
                function_response = function_to_call(self.customer_id)
                self.messages.append({
                    'role': 'tool',
                    'content': function_response,
                })

        final_response = self.client.chat(model=self.model, messages=self.prepare_messages(), stream=True)
        message_to_add = ""
        for response_token in final_response:
            message_to_add += response_token['message']['content']
            yield response_token['message']['content']
        self.messages.append({
            'role': response_token['message']['role'],
            'content': message_to_add
        })
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
