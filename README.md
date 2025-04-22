# SparkClimate Pakistan

SparkClimate Pakistan is a scalable, automated data pipeline for processing and analyzing weather and climate data specific to Pakistan. Leveraging Apache Spark on AWS EMR and Amazon S3, this project streamlines the ingestion, transformation, and storage of large-scale NOAA datasets, enabling robust climate analytics and visualization.

---

## Key Features

- **Automated ETL Pipeline:**  
  Ingests raw NOAA weather data, cleans and transforms it using PySpark, and stores the results in efficient Parquet format on Amazon S3.

- **Scalable Cloud Architecture:**  
  Built on AWS EMR for distributed processing, supporting large datasets and parallel computation.

- **Data Visualization:**  
  Seamless integration with Tableau for interactive dashboards and climate insights.

- **Reproducible & Modular:**  
  Easily configurable for new data sources, regions, or analytics requirements.

---

## Pipeline Overview

![pipeline](https://raw.githubusercontent.com/hassandsriaz/SparkClimate-Pakistan/refs/heads/main/Pipeline.png)

1. **Data Source:**  
   NOAA (Pakistan-specific) weather data.

2. **Storage:**  
   Raw and processed data stored in Amazon S3 (`input/` and `output/` folders).

3. **Processing:**  
   Apache Spark jobs run on AWS EMR clusters to transform and aggregate the data.

4. **Visualization:**  
   Tableau dashboards connect directly to processed S3 data for analysis.

---

## 🛠️ Technologies Used

- **Apache Spark 3.5.2** (PySpark)
- **AWS EMR 7.5.0**
- **Amazon S3**
- **Tableau**
- **Python**

---

## 🏗️ Architecture

![emr](https://raw.githubusercontent.com/hassandsriaz/SparkClimate-Pakistan/refs/heads/main/EMR.png)
![s3](https://github.com/hassandsriaz/SparkClimate-Pakistan/blob/main/S3.png?raw=true)

- **S3 Buckets:**  
  - `input/` for raw CSV data  
  - `output/` for processed Parquet data

- **EMR Cluster:**  
  - Spark, Hadoop, Hive, JupyterHub, and other big data tools pre-installed  
  - Example configuration:
    ![EMR Cluster Config](https://github.com/hassandsriaz/SparkClimate-Pakistan/blob/main/EMR_Cluster_Config.png?raw=true)

---

## ⚡ Quick Start

1. **Upload Data:**  
   Place raw NOAA CSV files in your S3 bucket's `input/` folder.

2. **Run ETL Job:**  
   Submit the Spark job to your EMR cluster:
   ```bash
   spark-submit EMR_ETL.py s3://<your-bucket>/input/ s3://<your-bucket>/output/
   ```

3. **Connect Tableau:**  
   - Use Tableau's Amazon S3 connector to connect to the processed Parquet files in `output/`.
   - Explore and visualize climate trends, rainfall, temperature, and more.

---

## 📁 Project Structure

```
.
├── data/
│   ├── input/               # Local sample/raw data (for dev/testing)
│   └── output/              # Local processed data (for dev/testing)
├── scripts/
│   └── EMR_ETL.py           # PySpark ETL script
├── dashboards/
│   └── dashboard_final.twb  # Tableau dashboard file
├── images/
│   ├── Pipeline.png         # Pipeline architecture image
│   ├── EMR.png              # EMR architecture image
│   └── S3.png               # S3 architecture image
├── README.md
├── LICENSE
```

---

## 📈 Example Dashboards

- **Average Temperature Trends (1957–2024)**
- **Rainfall Analysis by Station**
- **Temperature vs. Elevation**
- **Top 10 Hottest/Coldest Stations**

---

## 📜 License

Licensed under the [Apache 2.0 License](./LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.

---

## 📬 Contact

For questions or collaboration, please contact [Hassan D. S. Riaz](https://github.com/hassandsriaz).
