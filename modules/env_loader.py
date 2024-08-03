from os import getenv
from os.path import exists
from dotenv import load_dotenv
if exists(".env"):
    load_dotenv()


BOT_TOKEN = getenv('BOT_TOKEN')
BOT_USERNAME = getenv('BOT_USERNAME')
TARGET_CHAT_ID = getenv('TARGET_CHAT_ID')
