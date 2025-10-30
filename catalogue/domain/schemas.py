from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class ItemCreate(BaseModel):
    title: str
    description: str
    start_price: int
    shipping_days: int
    expedited_cost: int = 0
    start_at: datetime
    end_at: datetime
    keywords: List[str] = []

class ItemOut(BaseModel):
    id: str
    title: str
    current_price: int
    type: str
    remaining_seconds: int
