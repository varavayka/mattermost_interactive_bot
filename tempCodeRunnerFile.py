from flask import Flask
from dotenv import dotenv_values
import requests
import json

config = dotenv_values(".env")

print(config)