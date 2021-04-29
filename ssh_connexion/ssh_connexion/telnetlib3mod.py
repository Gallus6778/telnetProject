import asyncio, telnetlib3, time

port = 23
server_ip = "10.124.206.68"
user = "CHATBO"
password = "1234567890"
command = "ZMMI:MSISDN=237663064317:;"


class telnetlib3mod:
    def __init__(self, server_ip, user, password, command):
        self.server_ip = server_ip
        self.user = user
        self.password = password
        self.command = command

    # @asyncio.coroutine
    def shell(self, reader, writer):
        inc = 1
        while inc <= 4:
            # read stream until '?' mark is found
            outp = yield from reader.read(1024)
            if not outp:
                # End of File
                break
            elif 'ENTER USERNAME' in outp and inc == 1:
                writer.write(user)
                writer.write('\n\r' + password + '\n\r' + command + '\n\r')
                print(inc)
            inc += 1
            print(outp)

        print(outp)
        f = open("data_info_user.txt", "w")
        f.write(outp)
        f.close()
        time.sleep(0.5)
        # EOF
        # print()

    def main(self):
        # TELNET CONNEXION
        loop = asyncio.get_event_loop()
        coro = telnetlib3.open_connection(server_ip, port, shell=shell())

        # SENDING COMMAND
        reader, writer = loop.run_until_complete(coro)

        # CLOSE CONNEXION
        loop.run_until_complete(writer.protocol.waiter_closed)

    # loop = asyncio.get_event_loop()
    # coro = telnetlib3.open_connection(server_ip, port, shell=shell)
    # reader, writer = loop.run_until_complete(coro)
    # loop.run_until_complete(writer.protocol.waiter_closed)
    # Press the green button in the gutter to run the script.

if __name__ == '__main__':
    tot = telnetlib3mod()
    tot.main()