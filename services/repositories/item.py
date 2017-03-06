from models.base import session
from models import Item
from mappers.item import ItemMapper as Mapper


class ItemRepository(object):

    Table = Item.__table__

    @classmethod
    def read_one(cls, uuid):
        query = cls.Table.select().where(cls.Table.c.uuid == uuid)
        rows = session.execute(query)
        if rows:
            entities = map(ItemMapper.to_entity_from_obj, list(rows))
            return entities[0]

    @classmethod
    def read_all(cls):
        query = cls.Table.select()
        rows = session.execute(query)
        if rows:
            entities = map(ItemMapper.to_entity_from_obj, list(rows))
            return entities

    @classmethod
    def write_one(cls, entity):
        entity.validate()
        query = cls.Table.insert().values(Mapper.to_record(entity))
        session.execute(query)
