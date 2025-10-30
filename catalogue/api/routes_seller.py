from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from catalogue.domain.schemas import ItemCreate
from catalogue.domain.models import Item
from catalogue.domain import repo, service

router = APIRouter()
bearer_scheme = HTTPBearer(auto_error=False)

def get_user_id(creds: HTTPAuthorizationCredentials = Depends(bearer_scheme)) -> str:
    if not creds or creds.scheme.lower() != "bearer" or not creds.credentials:
        raise HTTPException(401, "Missing auth. Click 'Authorize' and enter token: stub")
    return "stub-user-id"

@router.post("/items", status_code=201, summary="Create Item (UC7)")
def create_item(payload: ItemCreate, user_id: str = Depends(get_user_id)):
    # writing to Firestore
    item_id = repo.create_item(user_id, payload.model_dump())


    item = Item(
        id=item_id,
        seller_id=user_id,
        title=payload.title,
        description=payload.description,
        type="Forward",
        start_price=payload.start_price,
        shipping_days=payload.shipping_days,
        expedited_cost=payload.expedited_cost,
        start_at=payload.start_at,
        end_at=payload.end_at,
        status="scheduled",
        keywords=payload.keywords or [],
    )
    return service.derive_item_out(item, current_price=item.start_price)
