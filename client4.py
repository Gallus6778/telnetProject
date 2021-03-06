
import telnetlib , socket


class TELNET(object):

    def __init__(self):
        self.tn = None
        self.username = "CHATBO"
        self.password = "1234567890"
        self.host = "10.124.206.68"
        self.port = 23
        self.timeout = 1
        self.login_prompt = b"login: "
        self.password_prompt = b"Password: "

    def connect(self):
        try :
            self.tn = telnetlib.Telnet(self.host,self.port,self.timeout)
        except socket.timeout :
            print("TELNET.connect() socket.timeout")

        self.tn.read_until(self.login_prompt, self.timeout)
        self.tn.write(self.username.encode('ascii') + b"\n")

        if self.password :
            self.tn.read_until(self.password_prompt,self.timeout)
            self.tn.write(self.password.encode('ascii') + b"\n")

    def write(self,msg):
        self.tn.write(msg.encode('ascii') + b"\n")
        return True


    def read_until(self,value):
        return self.tn.read_until(value)


    def read_all(self):
        try :
            return self.tn.read_all().decode('ascii')
        except socket.timeout :
            print("read_all socket.timeout")
            return False

    def close(self):
        self.tn.close()
        return True


    def request(self,msg):
        self.__init__()
        self.connect()
        if self.write(msg) == True :
            self.close()
            resp = self.read_all()
            return resp
        else :
            return False

telnet = TELNET()

#call request function

resp = telnet.request('ZMMI:MSISDN=237662165358:;') # it will be return ps output
print(resp)