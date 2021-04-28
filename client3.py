import getpass
import telnetlib2
import time

HOST = "10.124.206.68"
PORT = 23

user = "CHATBO".encode('ascii')
print(type(user))
print('User enter ok')

password = b"1234567890"

print("password enter ok")

tn = telnetlib2.telnet()

tn.login(HOST, user, password, 23,3)

# tn.write(user)
# tn.write(b'\n')
print('something')

# tn.write(password)
# tn.write(b'\n')
# print('password enter ok')

time.sleep(5)
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