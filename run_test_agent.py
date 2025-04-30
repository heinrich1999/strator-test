# run_test_agent.py
import os
import requests
from notion_client import Client
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Load creds
OPENAI_API_KEY     = os.getenv("OPENAI_API_KEY")
NOTION_TOKEN       = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
ZAPIER_WEBHOOK_URL = os.getenv("ZAPIER_WEBHOOK_URL")
RUNPOD_API_KEY     = os.getenv("RUNPOD_API_KEY")

# 1. Call OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)
resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":"List 3 emerging AI trends."}],
)
summary = resp.choices[0].message.content.strip()
print("AI Summary:\n", summary)

# 2. Write to Notion
notion = Client(auth=NOTION_TOKEN)
new_page = notion.pages.create(
  parent={"database_id": NOTION_DATABASE_ID},
  properties={
    "Name":    {"title":[{"text":{"content":"Trend Report"}}]},
    "Summary": {"rich_text":[{"text":{"content":summary}}]}
  }
)
print("Notion page created:", new_page["url"])

# 3. Fire the Zap
zap = requests.post(ZAPIER_WEBHOOK_URL, json={"summary": summary})
print("Zapier response code:", zap.status_code)
