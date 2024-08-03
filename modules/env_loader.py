from os import getenv
from os.path import exists
from dotenv import load_dotenv
if exists(".env"):
    load_dotenv()


BOT_TOKEN = getenv('BOT_TOKEN')

