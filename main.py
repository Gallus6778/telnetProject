# from telnetlib import Telnet
#
# with Telnet('localhost', 23) as tn:
#     tn.interact()

# import getpass
# import telnetlib

# HOST = "localhost"
# HOST = "10.124.206.68"
# user = input("Enter your remote account: ")
# password = getpass.getpass()

# tn = telnetlib.Telnet(HOST)

# tn.read_until(b"login: ")
# tn.write(user.encode('ascii') + b"\n")
# if password:
#     tn.read_until(b"Password: ")
#     tn.write(password.encode('ascii') + b"\n")

# tn.write(b"ls\n")
# tn.write(b"exit\n")

# print(tn.read_all().decode('ascii'))

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
import sys
import telnetlib

HOST = "10.124.206.68"
PORT = "23"

telnetObj = telnetlib.Telnet(HOST,PORT)

telnetObj.interact()

# print(dir(telnetObj))
# print(dir(telnetObj))
# message = ("GET /index.html HTTP/1.1\nHost:"+HOST+"\n\n").encode('ascii')

# telnetObj.write(message)

# output = telnetObj.read_all()
#
# print(output)
#
# telnetObj.close()

# print(help(telnetObj))
# telnetObj.open(HOST,PORT)