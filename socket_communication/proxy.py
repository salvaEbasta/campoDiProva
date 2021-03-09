import asyncio

async def handle(reader, writer):
    while True:
        data = await reader.read(60)
        addr = writer.get_extra_info('peername')
        print(f'{addr!r}: {data!r}')
    #req = Request('http://www.google.com')
    #response = urlopen(req)
    #writer.write(response.read())
    #await writer.drain()
    print(f'Closing {addr!r}...')

class Proxy:
    def __init__(self, host, port, handler):
        self.host = host
        self.port = port
        self.handler = handler
    
    def run(self):
        asyncio.run(self.__start_server())

    async def __start_server(self):
        self.server = await asyncio.start_server(self.handler, self.host, self.port)
        addr = self.server.sockets[0].getsockname()
        print(f'[!] Serving on {addr}')
        async with self.server:
            await self.server.serve_forever()


if __name__ == '__main__':
    p = Proxy('localhost', 42069, handle)
    p.run()