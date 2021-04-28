import telnetlib
import time

port = 23
server_ip = "10.124.206.68"
# server_ip = '192.168.1.68'

password = "1234567890"
username = "CHATBO"

tn = telnetlib.Telnet(server_ip, port)

print('connexion en cours 1 ...')
# tn.read_until(b"Username: ")

tn.write(username + "\n")

print('connexion en cours 2 ...')

# tn.read_until(b"Password: ")

tn.write(password + "\n")

print('connexion en cours 3 ...')

print("Successfully connected to %s" % server_ip)
tn.write(b"ZMMI:MSISDN=237662165358:;\n")

# time.sleep(1)

# output = tn.read_very_eager()

output = tn.read_all()
# output = output.decode('')
print(output)
print("done")