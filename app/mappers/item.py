from __future__ import absolute_import

from app.entities.item import Item
from app.mappers.base import EntityMapper


class ItemMapper(EntityMapper):
    _entity = Item
