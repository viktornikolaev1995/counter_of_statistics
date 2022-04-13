from datetime import date
from sqlalchemy import Column, Integer, Float, Date
from sqlalchemy.ext.hybrid import hybrid_property
from .database import Base


class Statistic(Base):
    __tablename__ = 'statistic'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    date = Column(Date, default=date.today())  # дата события
    views = Column(Integer, nullable=True)  # количество показов
    clicks = Column(Integer, nullable=True)  # количество кликов
    cost = Column(Float(decimal_return_scale=2), nullable=True)  # стоимость кликов (в рублях с точностью до копеек)

    @hybrid_property
    def cpc(self):
        if self.cost and self.clicks is not None:
            return round((self.cost / self.clicks), 2)  # средняя стоимость клика
        return None

    @hybrid_property
    def cpm(self):
        if self.cost and self.views is not None:
            return round(((self.cost / self.views) * 1000), 2)  # средняя стоимость 1000 показов
        return None