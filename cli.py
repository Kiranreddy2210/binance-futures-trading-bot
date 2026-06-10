from bot import logging_config
import argparse

from bot.client import get_client
from bot.orders import place_order
from bot.validators import *

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--qty", required=True)
parser.add_argument("--price")

args = parser.parse_args()

validate_side(args.side)
validate_type(args.type)

client = get_client()

response = place_order(
    client,
    args.symbol,
    args.side,
    args.type,
    args.qty,
    args.price
)

print("\nORDER SUCCESSFUL\n")
print("Response Type:", type(response))
print("Response:", response)
client = get_client()

print(client.futures_ping())