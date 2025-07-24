from ping3 import ping
from sp_data_operations import get_data
from excel_operations import export_to_excel
from datetime import datetime
import time 

def ping_request():
    results = []
    data = get_data()

    for name, ip in data:
        response = ping(ip, timeout=1)
        time.sleep(.5)

        if response is not None:
            results.append({
                'ping_timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'ping_status': 'SUCCESS',
                'ping_host': name,
                'ip_address': ip,
                'ping_response(ms)': round(response * 1000, 2)
            })
        else:
            results.append({
                'ping_timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'ping_status': 'ERROR',
                'ping_host': name,
                'ip_address': ip,
                'ping_response(ms)': None
            })
    
    return results

if __name__ == '__main__':
    data = ping_request()
    export_to_excel(data)

    