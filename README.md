# Data-Driven Retail Sales Analytics & Customer Segmentation Engine

## Project Overview & Objective
This repository contains a production-grade, end-to-end data analytics and consumer intelligence pipeline. The system converts raw, transactional retail logs into interactive dashboards and automated machine learning outputs. 

By applying an **RFM (Recency, Frequency, Monetary) behavioral framework** alongside unsupervised learning models (**K-Means Clustering**), this project bridges the gap between raw backend sales infrastructure and data-backed marketing strategies. This allows retail managers to move away from generic blast promotions and move toward high-conversion, personalized workflows.

---

## 🛠️ Tech Stack & Dependencies
* **Core Language:** Python 3.11
* **Data Engineering & EDA:** Pandas, NumPy
* **Machine Learning Pipeline:** Scikit-Learn (StandardScaler, KMeans Optimization)
* **Interactive Dashboards:** Streamlit, Plotly Express

---

## Project Architecture
```text
Retail Sales Data/
│
├── data/
│   ├── raw_transactions.csv              # Processed sales metrics ledger
│   └── processed_customer_features.csv   # Aggregated algorithmic profiles 
│
├── Dashboards/
│   └── app.py                            # Streamlit live web application script
│
└── requirements.txt                      # Project dependency manifest
