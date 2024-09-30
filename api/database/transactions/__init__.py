import csv
import datetime
from decimal import Decimal
from pathlib import Path

from utility import time_it


@time_it
def get_customer_transactions(customer_id: str):
    """Mock API call to gather customer transactions."""
    try:
        with (open(Path(__file__).parents[0] / f"{customer_id}.csv")) as infile:
            reader = csv.DictReader(infile)
            transactions = [row for row in reader]
    except FileNotFoundError:
        return "No transactions found for customer"
    response = f"Customer transactions for {customer_id}:\n"
    response += "-" * 5
    response += "\n"
    for t in transactions:
        response += f"Date: {datetime.date.fromisoformat(t['date']).strftime('%m/%d/%Y')}, "
        response += f"Type: {t['type']}, "
        response += f"Amount: ${(t['amount'])}, "
        response += f"Description: {(t['description'])}\n"
    response += "-" * 5
    response += "\n"
    current_balance = sum([Decimal(t['amount']) for t in transactions])
    response += f"Current Balance: ${current_balance}\n"
    response += "Payment terms: all outstanding balances are due within 30 days of the last purchase.\n"
    return response


def create_customer_transactions_tool(customer_id):
    def customer_transactions():
        """Get information about a customer's financial transactions (purchases, orders, returns, balance, etc.)"""
        return get_customer_transactions(customer_id)

    return customer_transactions
