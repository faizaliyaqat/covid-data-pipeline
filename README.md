# covid-data-pipeline
Serverless AWS-based COVID-19 data pipeline using Python, S3, Athena.
# COVID-19 Cloud Data Pipeline Using AWS (Serverless)

This project demonstrates how to build a complete, scalable, and serverless cloud data pipeline for COVID-19 data using AWS services and Python.

The pipeline fetches data from [Our World in Data](https://ourworldindata.org/coronavirus-source-data), processes it using Pandas, stores it in Amazon S3, and enables querying via Amazon Athena. The data was also visualized using Amazon QuickSight (dashboard trial used temporarily, then safely terminated).

---

## Dashboard Preview

### Full Dashboard Overview
![Dashboard](screenshots/dashboard_overview.png)

### Daily New Cases in India
![Line Chart](screenshots/line_chart_india.png)

### Total COVID Cases by Country
![Bar Chart](screenshots/bar_chart_world.png)

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

##  𝐖𝐡𝐚𝐭 𝐈 𝐋𝐞𝐚𝐫𝐧𝐞𝐝
1.Setting up S3-Athena integration

2.Writing clean ETL scripts using Python and Pandas

3.Casting and handling data types in Athena SQL

4.Designing effective data visualizations with QuickSight (cloud BI tools)

5.Managing cloud resources responsibly (avoiding billing)





