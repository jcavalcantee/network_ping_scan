from ping3 import ping
from sp_data_operations import get_data
from datetime import datetime
import time 
import logging

log_filename = f'logs/pings_at_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'

# Logger config
logging.basicConfig(
    filename=log_filename,
    filemode='a',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def verify_ips():
    issues = []

    ips = get_data()

    for name, ip in ips:
        response = ping(ip, timeout=1)
        time.sleep(.5)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if response is None:
            msg = f'[ISSUE] {name} ({ip} is down)'
            logging.warning(msg)
            issues.append((name, ip))
        else:
            msg = f'[OK] {name} ({ip}) in {round(response * 1000, 2)} ms'
            logging.info(msg)
    
    return issues

if __name__ == '__main__':
    issues = verify_ips()

    if issues:
        print('\nIPs with detected issues:')
        for name, ip in issues:
            print(f'\n- {name} ({ip})')
    else: 
        print('\nAll the IPs are online!')