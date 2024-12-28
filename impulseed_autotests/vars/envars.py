from dotenv import load_dotenv
import os

import platform

load_dotenv()

SERVICE_ENDPOINT = os.environ.get('SERVICE_ENDPOINT', platform.node())