import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    NODE_ENV = os.getenv('NODE_ENV')
    LOGLEVEL = os.getenv('LOGLEVEL')
    HTTP_PORT = int(os.getenv('HTTP_PORT', 3000))
    JAMBONZ_ACCOUNT_SID = os.getenv('JAMBONZ_ACCOUNT_SID')
    JAMBONZ_API_KEY = os.getenv('JAMBONZ_API_KEY')
    JAMBONZ_REST_API_BASE_URL = os.getenv('JAMBONZ_REST_API_BASE_URL')
    WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET')
    HTTP_USERNAME = os.getenv('HTTP_USERNAME')
    HTTP_PASSWORD = os.getenv('HTTP_PASSWORD')
