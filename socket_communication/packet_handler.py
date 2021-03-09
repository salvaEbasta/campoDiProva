import asyncio
import urllib
from urllib.request import urlopen, Request

async def handle(reader, writer):
    data = await reader.read()
    addr = writer.get_extra_info('peername')
    print(f'{addr!r}: {data!r}')
    #req = Request('http://www.google.com')
    #response = urlopen(req)
    #writer.write(response.read())
    #await writer.drain()
    print(f'Closing {addr!r}...')