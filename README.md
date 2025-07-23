# Network Ping Scan

This Python script fetches IP addresses and hostnames from a SharePoint list and performs ping tests to check their availability.  
It logs the results with timestamps to a log file.

The project uses `Office365-REST-Python-Client` for SharePoint access and `ping3` for pinging IPs.  
Configuration is done via environment variables stored in a `.env` file.

---
