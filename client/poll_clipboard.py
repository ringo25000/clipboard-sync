import pyperclip
import httpx
import asyncio


SERVER_URL = "http://192.168.50.98/save"
POLL_INTERVAL = 0.7  # in seconds


async def poll_clipboard():
    last_clipboard = ""

    while True:
        current = pyperclip.paste()
        if current != last_clipboard:
            async with httpx.AsyncClient() as client:
                await client.post(SERVER_URL, json={"content": current})
            print("📋 New clipboard content sent:", current)
            last_clipboard = current
        await asyncio.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    asyncio.run(poll_clipboard())