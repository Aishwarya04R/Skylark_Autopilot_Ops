import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


# database.py

def get_data(worksheet_name):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    
    # Open the spreadsheet named 'drone'
    # Then access the specific worksheet tab
    sheet = client.open("drone").worksheet(worksheet_name)
    data = sheet.get_all_records()
    return pd.DataFrame(data)

def update_pilot_status(pilot_id, new_status):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("drone").worksheet("pilot_roster")
    
    # Find the row with the pilot_id and update the 'status' column (Col 6)
    cell = sheet.find(pilot_id)
    sheet.update_cell(cell.row, 6, new_status)
    return f"Successfully updated {pilot_id} to {new_status}"