# Problem — API Configuration Validator

# APP_NAME
# API_KEY
# DEBUG

# Write a program that reads them using os.getenv() and validates the configuration.

# Rules
# 1️-APP_NAME
# Must exist.
# If missing → "APP_NAME is missing"

# 2️-API_KEY
# Must exist.
# Must contain at least 10 characters.
# If missing → "API_KEY is missing"
# If shorter than 10 → "API_KEY is too short"

# 3️-DEBUG
# It should contain either:
# "True"
# or
# "False"
# If it contains anything else → "DEBUG must be True or False"


import os
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
api_key = os.getenv("API_KEY")
debug = os.getenv("DEBUG")


if app_name:
    print("APP_NAME is valid")
else:
    print("APP_NAME is missing")


if api_key:
    if len(api_key) < 10:
        print("API_KEY is too short")
    else:
        print("API_KEY is valid")
else:
    print("API_KEY is missing")


if debug is None:
    print("DEBUG is missing")
elif debug in ("True", "False"):
    print("DEBUG is valid")
else:
    print("DEBUG must be True or False")
