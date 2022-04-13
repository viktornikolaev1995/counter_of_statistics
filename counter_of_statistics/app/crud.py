from sqlalchemy import desc
from sqlalchemy.orm import Session
from . import schemas, models


def create_statistic(db: Session, statistic: schemas.StatisticCreateSchema):
    statistic = models.Statistic(**statistic.dict())
    db.add(statistic)
    db.commit()
    db.refresh(statistic)
    return statistic


def get_statistic_list(db: Session, from_, to, sort_at_date_field, sort_at_views_field, sort_at_clicks_field,
                       sort_at_cost_field):
    fields = {
        'date': sort_at_date_field,
        'views': sort_at_views_field,
        'clicks': sort_at_clicks_field,
        'cost': sort_at_cost_field
    }
    sort_by_fields = [field for field, boolean in fields.items() if boolean]
    if from_ and to:
        return db.query(models.Statistic).filter(models.Statistic.date.between(from_, to)).order_by(
            *[desc(sort_by_field) for sort_by_field in sort_by_fields]).all()
    return db.query(models.Statistic).order_by(*[desc(sort_by_field) for sort_by_field in sort_by_fields]).all()


def delete_statistic(db: Session):
    db.query(models.Statistic).delete()
    db.commit()
    return {'204': 'Successful Response'}