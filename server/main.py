# server/main.py

from fastapi import FastAPI
from database import init_db, DB_PATH
from models import ClipboardEntry, ClipboardEntryOut
import aiosqlite

app = FastAPI()

# run init_db() once when the server starts + 
@app.on_event("startup")
async def startup():
    await init_db()

@app.get("/")
async def root():
    return {"message": "Clipboard Sync Backend Running"}

@app.post("/save")
async def save_clipboard(entry: ClipboardEntry):
    print(f"Received clipboard content: {entry.content}")
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(                                   # will auto insert the ID and timestamp
            "INSERT INTO clipboard (content) VALUES (?)", 
            (entry.content,)
        )
        await db.commit()
    return {"status": "saved"}

@app.get("/latest", response_model=ClipboardEntryOut)
async def get_latest():
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "SELECT id, content, timestamp FROM clipboard ORDER BY id DESC LIMIT 1"
        )
        row = await cursor.fetchone()

    if row:
        return ClipboardEntryOut(id=row[0], content=row[1], timestamp=row[2])
    else:
        return ClipboardEntryOut(id=0, content="", timestamp=None)

