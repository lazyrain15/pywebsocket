#!/usr/bin/env python

import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://localhost:5555") as websocket:
        await websocket.send(input())
        await websocket.recv()

asyncio.run(hello())
