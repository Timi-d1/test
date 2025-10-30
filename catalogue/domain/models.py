from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class Item(BaseModel):
    id: str
    seller_id: str
    title: str
    description: str
    type: str = "Forward"
    start_price: int
    shipping_days: int
    expedited_cost: int = 0
    start_at: datetime
    end_at: datetime
    status: str 
    keywords: List[str] = Field(default_factory=list)
