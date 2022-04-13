from datetime import date
from typing import Optional
from pydantic import BaseModel


class StatisticCreateSchema(BaseModel):
    date: Optional[date]
    views: Optional[int]
    clicks: Optional[int]
    cost: Optional[float]

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                'date': '2022-04-13',
                'views': 10000,
                'clicks': 3000,
                'cost': 12088.99,
            }
        }


class StatisticListSchema(BaseModel):
    date: date
    views: Optional[int]
    clicks: Optional[int]
    cost: Optional[float]
    cpc: Optional[float]
    cpm: Optional[float]

    class Config:
        orm_mode = True
