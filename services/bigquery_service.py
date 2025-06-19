from google.cloud import bigquery
from config import PROJECT_ID

client = bigquery.Client(project=PROJECT_ID)

def get_kpi_metrics():
    query = """
    SELECT CURRENT_DATE() AS date, COUNT(*) AS total_users
    FROM `your_project.your_dataset.optimized_user_table`
    """
    result = client.query(query).to_dataframe()
    return result.to_dict(orient="records")

def get_pipeline_status():
    query = """
    SELECT MAX(updated_at) AS last_run
    FROM `your_project.your_dataset.dbt_run_metadata`
    """
    result = client.query(query).to_dataframe()
    return result.to_dict(orient="records")[0]

def get_cost_savings():
    query = """
    SELECT before_cost, after_cost,
           ROUND((before_cost - after_cost) / before_cost * 100, 2) AS savings_pct
    FROM `your_project.your_dataset.cost_comparison`
    ORDER BY snapshot_date DESC
    LIMIT 1
    """
    result = client.query(query).to_dataframe()
    return result.to_dict(orient="records")[0]
