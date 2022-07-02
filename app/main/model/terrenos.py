# coding: utf-8
from sqlalchemy import Column, Float, Text
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()
metadata = Base.metadata

from app.main import db


class Terreno(db.Model):
    __tablename__ = 'terrenos'

    index = Column(BIGINT(20), primary_key=True, index=True)
    codigo_postal = Column(Text)
    superficie_terreno = Column(Float(asdecimal=True))
    superficie_construccion = Column(Float(asdecimal=True))
    uso_construccion = Column(Text)
    valor_suelo = Column(Float(asdecimal=True))
    subsidio = Column(Float(asdecimal=True))

    @hybrid_property
    def price_unit(self):
        return self.superficie_terreno / self.valor_suelo - self.subsidio

    @hybrid_property
    def price_unit_construction(self):
        return self.superficie_construccion / self.valor_suelo - self.subsidio
