import telnetlib

HOST = "10.124.206.68"
PORT = 23

print("connecting...")
tn = telnetlib.Telnet(HOST, PORT)
tn.read_until(b"250")
print("connection established!\n sending ehlo...")
tn.write(b"CHATBO")

print('Bien ...')
tn.read_until(b"250")
print("response received")