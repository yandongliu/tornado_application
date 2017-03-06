from models.base import session


class BaseRepository(object):

    @classmethod
    def read_one(cls, uuid):
        # assert cls.Table
        # assert cls.Mapper
        query = cls.Table.select().where(cls.Table.c.uuid == uuid)
        rows = session.execute(query)
        if rows:
            entities = map(cls.Mapper.to_entity_from_obj, list(rows))
            return entities[0]

    @classmethod
    def read_all(cls):
        # assert cls.Table
        # assert cls.Mapper
        query = cls.Table.select()
        rows = session.execute(query)
        if rows:
            entities = map(cls.Mapper.to_entity_from_obj, list(rows))
            return entities

    @classmethod
    def write_one(cls, entity):
        # assert cls.Table
        # assert cls.Mapper
        entity.validate()
        query = cls.Table.insert().values(cls.Mapper.to_record(entity))
        session.execute(query)
