import pandas as pd
import os
from utils import get_month_and_year

def get_excel_filename():
    month_year = get_month_and_year()
    return f'exported_logs/logs_{month_year}.xlsx'

def export_to_excel(data):
    file_name = get_excel_filename()

    if os.path.exists(file_name):
        df_existing = pd.read_excel(file_name)
        df_new = pd.DataFrame(data)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)

        df_combined.to_excel(file_name, index=False)
        print(f'New logs added on file: {file_name}')
    else:
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
        print(f'Logs exported to file: {file_name}')

    


