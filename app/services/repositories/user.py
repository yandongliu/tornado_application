from app.mappers.user import UserMapper
from app.models import User
from app.services.repositories.base import BaseRepository


class UserRepository(BaseRepository):

    Table = User.__table__
    Mapper = UserMapper
