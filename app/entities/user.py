from schematics.types import StringType

from app.entities.base import TimestampModel, UuidStringType


class User(TimestampModel):

    uuid = UuidStringType(required=True)
    email = StringType(required=True)
    passwd = StringType(required=True)
