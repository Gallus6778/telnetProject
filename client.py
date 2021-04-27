import telnetlib
import time

server_ip = '10.124.206.68'
# server_ip = '192.168.1.68'
port = 23
# password = 'admin'
password = 1234567890
username = 'CHATBO'
# username = 'admin'

tn = telnetlib.Telnet(server_ip, port)

print('connexion en cours 1 ...')

tn.read_until(b"Username: ")
tn.write(username.encode() +b"\n")

print('connexion en cours 2 ...')

tn.read_until(b"Password: ")
tn.write(password.encode() +b"\n")

print('connexion en cours 3 ...')

print("Successfully connected to %s" % server_ip)
tn.write(b"ZMMI:MSISDN=237662165358:;\n")
# tn.write(b"ls\n")

time.sleep(1)
# print (type("output"))
# output = tn.read_very_eager()

output = tn.read_all()
# print(output)

output_formatted = output.decode('')
print(output_formatted)
print("done")