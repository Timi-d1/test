from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional
from catalogue.domain import repo, service

router = APIRouter()

@router.get("/search")
def search(q: Optional[str] = Query(default=None)):
    items = repo.search_active(q)
    return [service.derive_item_out(it, current_price=it.start_price) for it in items]

@router.get("/items/{item_id}")
def get_item(item_id: str):
    it = repo.get_item(item_id)
    if not it:
        raise HTTPException(404, "Item not found")
    return service.derive_item_out(it, current_price=it.start_price)
