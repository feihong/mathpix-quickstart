import os
import requests
import dotenv
from pathlib import Path

dotenv.load_dotenv()

APP_ID = os.environ['APP_ID']
APP_KEY = os.environ['APP_KEY']

options = {
    "conversion_formats": {"docx": True, "tex.zip": True},
    "math_inline_delimiters": ["$", "$"],
    "rm_spaces": True
}

r = requests.post("https://api.mathpix.com/v3/pdf",
  headers={
    "app_id": APP_ID,
    "app_key": APP_KEY,
  },
  # data={
  #   "options_json": json.dumps(options)
  # },
  files={
    "file": open("problems.pdf", "rb")
  },
)

print(r.text)
Path('output.json').write_text(r.text)
