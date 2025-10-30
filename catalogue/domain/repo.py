from typing import List, Optional
from datetime import datetime, timezone
from catalogue.db.firestore import get_db
from catalogue.domain.models import Item

COLL = "items"

def _to_item(doc) -> Item:
    d = doc.to_dict()
    return Item(id=doc.id, **d)

def create_item(seller_id: str, data: dict) -> str:
    db = get_db()
    doc = db.collection(COLL).document()
    
    payload = {
        **data,
        "seller_id": seller_id,
        "status": "scheduled",
        "type": data.get("type", "Forward"),
        "keywords": [k.lower() for k in (data.get("keywords") or [])],
    }
    if payload["end_at"] <= payload["start_at"]:
        raise ValueError("end_at must be after start_at")
    
    print("WRITE PAYLOAD:", {**payload, "start_at": str(payload["start_at"]), "end_at": str(payload["end_at"])})

    doc.set(payload)   
    return doc.id

def get_item(item_id: str) -> Optional[Item]:
    db = get_db()
    snap = db.collection(COLL).document(item_id).get()
    return _to_item(snap) if snap.exists else None
