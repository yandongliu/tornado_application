from __future__ import absolute_import

from tornado import gen
from tornado.web import RequestHandler

from app.lib import cache
from app.services.repositories.item import ItemRepository


class DatabaseHandler(RequestHandler):

    @cache.local_memoize
    @gen.coroutine
    def get(self):
        items = ItemRepository.read_all()
        self.write({'data': [r.to_primitive() for r in items]})
