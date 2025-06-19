# 🚀 Data API Service – FastAPI + BigQuery

A lightweight, production-ready Data API built with **FastAPI** that serves optimized data from **Google BigQuery**. Designed to support internal analytics dashboards, automation tools, and monitoring systems by exposing clean, query-efficient endpoints.

---

## 📆 Project Overview

This API service is part of a broader data pipeline optimization initiative where legacy ETL workflows were migrated to **dbt + BigQuery**, reducing query costs by over 90%. The API layer enables real-time data access to these optimized tables for internal applications.

---

## ✨ Key Features

- 🔍 `GET /metrics`: Returns daily user metrics from dbt models.
- 📈 `GET /pipeline-status`: Fetches the last successful dbt pipeline run timestamp.
- 💰 `GET /cost-savings`: Shows monthly cost reduction after optimization.
- ⚙️ Built using FastAPI with built-in OpenAPI docs (`/docs`)
- ☁️ Deployed on **Google Cloud Run** using Docker and GitLab CI/CD

---

## 🧱 Tech Stack

- **Python 3.10**
- **FastAPI**
- **Google BigQuery**
- **Docker**
- **Google Cloud Run**
- **GitLab CI/CD**
- **Pandas** (for dataframe handling)

---

## 📂 Project Structure

```
data-api-service/
├── main.py                 # FastAPI routes
├── services/
│   └── bigquery_service.py # BigQuery query logic
├── models/
│   └── schemas.py          # Pydantic schemas
├── config.py               # GCP config
├── requirements.txt
├── Dockerfile
└── .gitlab-ci.yml
```

---

## 🚀 How to Run Locally

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Set Environment Variable

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service_account.json
export GCP_PROJECT_ID=your-gcp-project-id
```

### 3. Start Server

```bash
uvicorn main:app --reload
```

Visit the docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ☁️ Deploying to Google Cloud Run

```bash
gcloud builds submit --tag asia-southeast2-docker.pkg.dev/YOUR_PROJECT_ID/data-api-repo/data-api-service

gcloud run deploy data-api-service \
  --image asia-southeast2-docker.pkg.dev/YOUR_PROJECT_ID/data-api-repo/data-api-service \
  --region asia-southeast2 \
  --platform managed \
  --allow-unauthenticated \
  --set-env-vars GCP_PROJECT_ID=your-gcp-project-id
```

> Ensure you use a service account with `BigQuery Data Viewer` role for Cloud Run.

---

## 📈 Example API Response

### `/cost-savings`

```json
{
  "before_cost": 512.89,
  "after_cost": 47.23,
  "savings_pct": 90.79
}
```

---

## 📚 Use Cases

- Serve data to **internal dashboards** (Streamlit, Grafana, etc.)
- Enable **automated monitoring** of pipeline status and data health
- Provide **lightweight data access layer** without exposing BigQuery directly

---

## 🧠 Lessons Learned

- FastAPI is excellent for quickly exposing structured, documented data APIs.
- Partitioned and clustered BigQuery tables are essential for cost-effective access.
- Cloud Run provides an ideal environment for scalable, serverless deployment.

---
