import os
import json
import requests
import dotenv

dotenv.load_dotenv()

APP_ID = os.environ['APP_ID']
APP_KEY = os.environ['APP_KEY']

# print(APP_ID)
# print(APP_KEY)

r = requests.post("https://api.mathpix.com/v3/text",
  files={"file": open("problem-2.jpg", "rb")},
  data={
    "options_json": json.dumps({
      "rm_spaces": True
    })
  },
  headers={
    "app_id": APP_ID,
    "app_key": APP_KEY,
  }
)
result = r.json()
print(json.dumps(result, indent=2, sort_keys=True))
print(result['text'])
