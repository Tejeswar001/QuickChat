import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

SHEET_NAME = "QuickChatLogs"

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json",
    scope
)

client = gspread.authorize(creds)
#sheet = client.open("1abSNRgHKDWHAkBgCPMwsYEgLhI8UZGV34YJh9B2QYRQ").sheet1
sheet = client.open(SHEET_NAME).sheet1

def log_message(user_msg, bot_msg):
    timestamp = datetime.datetime.now().isoformat()
    sheet.append_row([timestamp, user_msg, bot_msg])
