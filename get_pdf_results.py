import os
import sys
import requests
import dotenv
from pathlib import Path

pdf_id = sys.argv[1]

dotenv.load_dotenv()

APP_ID = os.environ['APP_ID']
APP_KEY = os.environ['APP_KEY']

mmd_file = pdf_id + '.mmd'

r = requests.get(
  f"https://api.mathpix.com/v3/pdf/{mmd_file}",
  headers={"app_id": APP_ID, "app_key": APP_KEY,})

Path(mmd_file).write_text(r.text)

