import httpx
import asyncio

async def fetch_latest():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/latest")
        if response.status_code == 200:
            data = response.json()
            print("🧾 Latest clipboard on server:", data)
        else:
            print("❌ Error fetching clipboard:", response.status_code)


if __name__ == "__main__":
    asyncio.run(fetch_latest())
