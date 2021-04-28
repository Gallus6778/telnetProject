import getpass
import telnetlib
import time

HOST = input('Enter BSC IP : ')
PORT = 23
user = input('Enter username : ')
user = user.encode('ascii')

# print('User enter ok')

password = input('Enter password : ')
password = password.encode('ascii')

print("password enter ok \n")

print('connexion ...')
tn = telnetlib.Telnet(HOST, port= PORT)

tn.read_until(b" USERNAME < ")
tn.write(user)
tn.write(b'\n')

tn.write(password)
tn.write(b'\n')
print('connexion established.')

time.sleep(2)

command = input('Enter your command : ')
command = command.encode('ascii')

print("\n Command entering ...")

tn.write(command)
tn.write(b"\n")
print("\n Command entered")
output = tn.read_very_eager().decode('utf8')
# output = tn.read_all().decode('utf8')

print(output)

print("command executed.")
time.sleep(3)
tn.close()

# tn.read_until(b"login: ")
# tn.write(user.encode('ascii') + b"\n")
# print(tn)
# if password:
#     tn.read_until(b"Password: ")
#     tn.write(password.encode('ascii') + b"\n")
#
# tn.write(b"ls\n")
# tn.write(b"exit\n")
#
# print(tn.read_all().decode('ascii'))