import argparse
import asyncio

async def client(host, port):
    print(f'Connecting to {host}:{port}')
    r, w = await asyncio.open_connection(host, port)
    exit = False
    while not exit:
        msg = input(f'{host}:{port}> ')
        w.write(msg.encode())

        if msg == 'exit':
            exit = True
        data = await r.read(100)
        print(f'{data.decode()!r}')
    w.close()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--port', type=int, default=42069)
    args = parser.parse_args()

    asyncio.run(client(args.host, args.port))