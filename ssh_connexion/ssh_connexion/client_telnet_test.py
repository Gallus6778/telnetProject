import asyncio, telnetlib3

@asyncio.coroutine
def shell(reader, writer):
    while True:
        # read stream until '?' mark is found
        outp = yield from reader.read(1024)
        if not outp:
            # End of File
            break
        elif '?' in outp:
            # reply all questions with 'y'.
            writer.write('admin')
            # writer.write('12345')

        # display all server output
        print(outp, flush=True)

    # EOF
    print()

loop = asyncio.get_event_loop()
coro = telnetlib3.open_connection('localhost', 6026, shell=shell)
reader, writer = loop.run_until_complete(coro)
loop.run_until_complete(writer.protocol.waiter_closed)

# tn = telnetlib3.TelnetWriter()