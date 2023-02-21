#!/usr/bin/env python

import asyncio
import websockets
import json

async def hello():
    async with websockets.connect("ws://localhost:5555") as websocket:
        await websocket.send(json.dumps({'message': 'send', 'finger': [f'22111757', f'Andhika Candra Wijaya', f'Masuk', f'2023-02-13 16:00:00', f'1']}))
        result = await websocket.recv()
        print('Result: {}'.format(result))

asyncio.run(hello())
