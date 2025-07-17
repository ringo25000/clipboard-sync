import asyncio
import pyperclip
import json
from websockets import connect

SERVER_WS_URL = "ws://192.168.50.98:8000/ws"  # Replace with your actual server IP

async def receive_clipboard():
    async with connect(SERVER_WS_URL) as websocket:
        print("✅ Connected to WebSocket server")

        while True:
            try:
                message = await websocket.recv()
                data = json.loads(message)
                content = data.get("content")
                if content:
                    pyperclip.copy(content)
                    print("📋 Clipboard updated:", content)
            except Exception as e:
                print("⚠️ Error:", e)

if __name__ == "__main__":
    asyncio.run(receive_clipboard())
