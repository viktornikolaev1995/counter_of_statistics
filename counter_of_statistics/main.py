from datetime import date
import uvicorn
from fastapi import FastAPI, Depends
from typing import List, Optional
from sqlalchemy.orm import Session
import database
import schemas
import crud


database.Base.metadata.create_all(bind=database.engine)
app = FastAPI(title='Counter_of_statistics')


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post(
    path='/statistics/',
    response_model=schemas.StatisticListSchema,
    tags=['statistics'],
    operation_id='statistic_create'
)
def create_statistic(statistic: schemas.StatisticCreateSchema, db: Session = Depends(get_db)):
    return crud.create_statistic(db=db, statistic=statistic)


@app.get(
    path='/statistics/',
    response_model=List[schemas.StatisticListSchema],
    tags=['statistics'],
    operation_id='statistic_list'
)
def retrieve_statistic_list(from_: Optional[date] = None, to: Optional[date] = None,
                            sort_at_date_field: bool = False, sort_at_views_field: bool = False,
                            sort_at_clicks_field: bool = False, sort_at_cost_field: bool = False,
                            db: Session = Depends(get_db)):
    statistic_list = crud.get_statistic_list(
        db=db, from_=from_, to=to, sort_at_date_field=sort_at_date_field, sort_at_views_field=sort_at_views_field,
        sort_at_clicks_field=sort_at_clicks_field, sort_at_cost_field=sort_at_cost_field
    )
    return statistic_list
