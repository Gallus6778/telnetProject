from scrapli import Scrapli

device = {
   "host": "10.124.206.68",
   "auth_username": "CHATBO",
   "auth_password": "1234567890",
   "auth_strict_key": False,
   "platform": "cisco_iosxe"
}

conn = Scrapli(**device)
conn.open()
print(conn.get_prompt())
