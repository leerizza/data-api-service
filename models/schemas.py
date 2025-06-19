from pydantic import BaseModel
from datetime import date

class KPIMetric(BaseModel):
    date: date
    total_users: int

class PipelineStatus(BaseModel):
    last_run: str

class CostSavings(BaseModel):
    before_cost: float
    after_cost: float
    savings_pct: float