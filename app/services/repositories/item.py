from app.mappers.item import ItemMapper
from app.models import Item
from app.services.repositories.base import BaseRepository


class ItemRepository(BaseRepository):

    Table = Item.__table__
    Mapper = ItemMapper
