
from sqlalchemy import (
    create_engine,
)

from sqlalchemy_litesync import litesync

from sqlalchemy.dialects import registry

def test_register():
    registry.register("sqlite.litesync", "sqlalchemy_litesync.litesync", "dialect")
    engine = create_engine('litesync:///test.db?node=primary&bind=tcp://0.0.0.0:1234')
    engine.dispose()
