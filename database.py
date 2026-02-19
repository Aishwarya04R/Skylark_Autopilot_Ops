import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def get_data(worksheet_name):
    # This line tells the app to look at the "Secrets" box you just filled
    creds_dict = st.secrets["gcp_service_account"]
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # We use from_json_keyfile_dict instead of from_json_keyfile_name
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    
    sheet = client.open("drone").worksheet(worksheet_name)
    data = sheet.get_all_records()
    return pd.DataFrame(data)

def update_pilot_status(pilot_id, new_status):
    creds_dict = st.secrets["gcp_service_account"]
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    
    sheet = client.open("drone").worksheet("pilot_roster")
    
    # Find the row for the pilot and update
    cell = sheet.find(pilot_id)
    sheet.update_cell(cell.row, 3, new_status) # Assuming column 3 is Status
    return f"Status updated to {new_status} in Google Sheets!"
