# server/models.py

from pydantic import BaseModel
from datetime import datetime

class ClipboardEntry(BaseModel):
    content: str

class ClipboardEntryOut(BaseModel):
    id: int
    content: str
    timestamp: datetime