from datetime import datetime

def get_month_and_year():
    month = datetime.now().strftime('%B').capitalize().lower()
    year = datetime.now().year
    return f'{month}_{year}'