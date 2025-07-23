from sp_auth import get_sharepoint_context
import os

list_name = os.getenv("SHAREPOINT_LIST_NAME")

# Query
def get_data():
        ctx = get_sharepoint_context()
        sp_list = ctx.web.lists.get_by_title(list_name)

        items = sp_list.items.get().execute_query()

        ips = []
        for item in items:
            name = item.properties.get('host_name')
            ip = item.properties.get('ip_address')

            ips.append((name, ip))
            
        return ips