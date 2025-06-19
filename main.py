from fastapi import FastAPI
from services.bigquery_service import get_kpi_metrics, get_pipeline_status, get_cost_savings

app = FastAPI(title="Pipeline Optimization API")

@app.get("/metrics")
def metrics():
    return get_kpi_metrics()

@app.get("/pipeline-status")
def pipeline_status():
    return get_pipeline_status()

@app.get("/cost-savings")
def cost_savings():
    return get_cost_savings()