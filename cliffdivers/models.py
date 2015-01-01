# -*- coding: utf-8 -*-
import datetime as dt

from cliffdivers.extensions import bcrypt
from cliffdivers.database import (
    Column,
    db,
    Model,
    ReferenceCol,
    relationship,
    SurrogatePK,
)


class Entity(Model):
    __tablename__ = 'entity'

    # name = Column(db.String(80), unique=True, nullable=False)

    id = Column(db.Integer, primary_key=True)
    entity_name = Column(db.String(200), unique=True, nullable=False)
    entity_type = Column(db.String(50), nullable=False)
    entity_status = Column(db.String(50), nullable=False)
    created = Column(db.DateTime, nullable=False)
    created_user_id = Column(db.Integer, nullable=False)
    modified = Column(db.DateTime, nullable=False)
    modified_user_id = Column(db.Integer, nullable=False)
    # user_id = ReferenceCol('users', nullable=True)
    # user = relationship('User', backref='entity')

    # def __init__(self, name, **kwargs):
    #     db.Model.__init__(self, name=name, **kwargs)

    # def __repr__(self):
    #     return '<Role({name})>'.format(name=self.name)
