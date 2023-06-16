import os
from environs import Env
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
class Settings:
    TOKEN = os.environ.get('TOKEN')
    DB_PATH = os.environ.get('DB_PATH')
    EXPORTS_PATH = os.environ.get('EXPORTS_PATH')
    IMAGES_PATH = os.environ.get('IMAGES_PATH')
    ADMINS = os.environ.get('ADMINS')
    env = Env()
    SUPER_ADMINS = env.list('SUPERADMINS')