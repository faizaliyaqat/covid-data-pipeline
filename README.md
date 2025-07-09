# COVID-19 Cloud Data Pipeline Using AWS (Serverless)

Serverless AWS-based COVID-19 data pipeline using Python, S3, Athena.

This project demonstrates how to build a complete, scalable, and serverless cloud data pipeline for COVID-19 data using AWS services and Python.

The pipeline fetches data from [Our World in Data](https://ourworldindata.org/coronavirus-source-data), processes it using Pandas, stores it in Amazon S3, and enables querying via Amazon Athena. The data was also visualized using Amazon QuickSight (dashboard trial used temporarily, then safely terminated).

---

### Daily New Cases in India

![Screenshot 2025-07-10 012126](https://github.com/user-attachments/assets/78016206-3f2b-40be-8f2c-a2e0bc3fc549)

### Total COVID Cases by Country

![Screenshot 2025-07-10 012114](https://github.com/user-attachments/assets/b84c00bb-3f61-4919-bf3f-ecbde71f61c8)

---

## Tools & Technologies Used

| Component        | Tool/Service      |
|------------------|-------------------|
| Ingestion        | Python (Anaconda) |
| Transformation   | Pandas            |
| Storage          | Amazon S3         |
| Query Engine     | Amazon Athena     |
| Visualization    | Amazon QuickSight |
| Repo Hosting     | GitHub            |

---

## Architecture

OWID Dataset → Python Script → Clean CSV → S3 Bucket → Athena Table → SQL Queries → [QuickSight Dashboard]

---

## Sample Athena Query

```sql
SELECT
  location,
  date,
  CAST(NULLIF(new_cases, '') AS DOUBLE) AS new_cases
FROM covid_data_csv
WHERE location = 'India'
ORDER BY date;
---





