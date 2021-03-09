import argparse
import asyncio
from asyncio.streams import StreamReader, StreamWriter

async def handle(reader: StreamReader, writer: StreamWriter):
    exit = False
    while not exit:
        data = await reader.read(100)
        msg = data.decode()
        addr = writer.get_extra_info('peername')
        print(f'{addr!r}: {data}->{msg!r}')
        
        if msg == 'exit':
            exit = True
            out_msg = 'cy@'
        else:
            out_msg = 'Imagine ' + msg

        writer.write(out_msg.encode())
        await writer.drain()

    print(f'Closing {addr!r}...')


async def sock_server(host, port):
    server = await asyncio.start_server(handle, host, port)
    addr = server.sockets[0].getsockname()
    print(f'[!] Serving on {addr}')
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--port', type=int, default=42069)
    args = parser.parse_args()

    asyncio.run(sock_server(args.host, args.port))