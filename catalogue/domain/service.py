from datetime import datetime, timezone
from catalogue.domain.models import Item
from catalogue.domain.schemas import ItemOut

def derive_item_out(item: Item, current_price: int) -> ItemOut:
    now = datetime.now(timezone.utc)
    remaining = int((item.end_at - now).total_seconds())
    if remaining < 0:
        remaining = 0
    return ItemOut(
        id=item.id,
        title=item.title,
        current_price=current_price,
        type=item.type,
        remaining_seconds=remaining,
    )
