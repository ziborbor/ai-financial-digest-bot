import gspread
from google.oauth2.service_account import Credentials

spreadsheetURL="https://docs.google.com/spreadsheets/d/1oXf0Ki6JNqpHsCbtk6sjJBzgo_86yFcVOSR1pJ9NmXA/edit?gid=0#gid=0"
worksheet_Name="RAW_SCHEMA"
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES
)


def load_sheet():
    """
    Load raw data from Google Sheets.

    INPUT:
        creds - Google service account credentials
        sheet_url - full Google Sheets URL
        worksheet_name - tab name in the sheet

    OUTPUT:
        list of dicts (raw rows)
    """

    # Step 1: authenticate client
    client = gspread.authorize(creds)

    # Step 2: open spreadsheet using URL
    spreadsheet = client.open_by_url(spreadsheetURL)

    # Step 3: select worksheet (tab inside sheet)
    sheet = spreadsheet.worksheet(worksheet_Name)

    # Step 4: convert sheet into Python list of dictionaries
    data = sheet.get_all_records()

    return data