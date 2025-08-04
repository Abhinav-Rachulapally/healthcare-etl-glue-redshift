# Healthcare ETL Pipeline with AWS Glue & Redshift

This project demonstrates an end-to-end ETL pipeline for healthcare records using AWS Glue, PySpark, and Redshift.

## ⚙️ Tech Stack

- AWS Glue (serverless ETL)
- PySpark
- Amazon S3
- Amazon Redshift
- AWS IAM

## 🔄 Pipeline Flow

1. Raw patient records uploaded to S3
2. Glue job cleans & validates health data (missing age, diagnosis)
3. Data written to Redshift table for querying and reporting

## 🧪 Use Case

- Real-time ingestion of health checkup records
- Alerts generation for critical conditions based on diagnosis fields

## 📁 Folder Structure

healthcare-etl-glue-redshift/
│
├── scripts/
│   └── healthcare_glue_job.py      ← Glue job to clean patient health records
│
├── data/
│   └── sample_health_data.csv      ← Sample CSV with health records (optional)
│
├── dashboard/
│   └── patient_dashboard.png       ← BI report screenshot (optional)
│
└── README.md                       ← Clear documentation of the pipeline & tools used
