import asyncio, telnetlib3

@asyncio.coroutine
def shell(reader, writer):
    writer.write('\r\nEnter login : ')
    login = yield from reader.read(1)

    writer.write('\r\nEnter password : ')
    password = yield from reader.read(1)
    if login == 'admin' and password == '12345':
        writer.echo('bienvenu ' + login)
        writer.write('\r\nThey say the only way to win '
                     'is to not play at all.')
        yield from writer.drain()
    writer.close()

loop = asyncio.get_event_loop()
coro = telnetlib3.create_server(port=6023, shell=shell)
server = loop.run_until_complete(coro)
loop.run_until_complete(server.wait_closed())