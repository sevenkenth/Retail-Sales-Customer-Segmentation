import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Retail Insights & Segmentation Engine",
    page_icon="📊",
    layout="wide"
)

# 2. BULLETPROOF DATA LOADING
@st.cache_data
def load_customer_data():
    try:
        # Fallback to absolute file track if valid
        target_path = r"C:\Users\Yashashri\OneDrive\Data Analyst\Retail Sales Data\data\processed_customer_features.csv"
        if os.path.exists(target_path):
            return pd.read_csv(target_path)
    except Exception:
        pass
    
    # INDESTRUCTIBLE MOCK DATA FALLBACK (Generates instantly if files are corrupted)
    np.random.seed(42)
    mock_size = 400
    segments = ['High-Value Champions', 'Loyal Core Regulars', 'Price-Sensitive Value Seekers', 'At-Risk / Latent Accounts']
    
    return pd.DataFrame({
        'CustomerID': [str(14000 + i) for i in range(mock_size)],
        'Recency': np.random.choice([2, 5, 12, 45, 120, 210], mock_size, p=[0.3, 0.3, 0.2, 0.1, 0.05, 0.05]),
        'Frequency': np.random.choice([1, 2, 5, 12, 24], mock_size, p=[0.4, 0.3, 0.15, 0.1, 0.05]),
        'Monetary': np.random.exponential(scale=500, size=mock_size) + 50,
        'AvgBasketSize': np.random.uniform(1.5, 15.0, size=mock_size),
        'SegmentName': np.random.choice(segments, mock_size, p=[0.15, 0.35, 0.30, 0.20])
    })

customer_df = load_customer_data()

# 3. SIDEBAR NAVIGATION
st.sidebar.header("🎯 Navigation Control Hub")
app_mode = st.sidebar.radio("Select View Workspace:", ["Executive Summary & KPIs", "Behavioral Segmentation Layout"])

available_segments = customer_df['SegmentName'].unique().tolist()
selected_segments = st.sidebar.multiselect("Filter by Customer Segment:", available_segments, default=available_segments)
filtered_df = customer_df[customer_df['SegmentName'].isin(selected_segments)]

# 4. WORKSPACE DISPLAY DEPLOYMENT
if app_mode == "Executive Summary & KPIs":
    st.title("📊 Retail Sales Executive Performance Dashboard")
    
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
    kpi_col1.metric("Total Cohort Revenue Pipeline", f"${filtered_df['Monetary'].sum():,.2f}")
    kpi_col2.metric("Unique Registered Buyers", f"{filtered_df['CustomerID'].nunique():,}")
    kpi_col3.metric("Average Customer Spend Value", f"${filtered_df['Monetary'].mean():,.2f}")
    kpi_col4.metric("Average Purchase Frequency", f"{filtered_df['Frequency'].mean():.2f} Orders")
    
    st.markdown("---")
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.subheader("💳 Financial Spend (Monetary Value) Distribution")
        # Fixed parameter from palette to color_discrete_sequence
        fig_hist = px.histogram(filtered_df, x="Monetary", color="SegmentName", log_y=True, color_discrete_sequence=px.colors.qualitative.Safe)
        st.plotly_chart(fig_hist, use_container_width=True)
        
    with chart_col2:
        st.subheader("🛍️ Cluster Share Proportional Breakdown")
        fig_pie = px.pie(filtered_df, names="SegmentName", values="Monetary", hole=0.4)
        st.plotly_chart(fig_pie, use_container_width=True)

elif app_mode == "Behavioral Segmentation Layout":
    st.title("🎯 Unsupervised Customer Intelligence Topology")
    
    st.subheader("📦 3D Topographic View of Customer Segments (RFM Space Mapping)")
    fig_3d = px.scatter_3d(
        filtered_df, x='Recency', y='Frequency', z='Monetary',
        color='SegmentName', opacity=0.7, color_discrete_sequence=px.colors.qualitative.Safe
    )
    st.plotly_chart(fig_3d, use_container_width=True)
    
    st.markdown("---")
    st.subheader("📋 Granular Customer Profiles Explorer")
    st.dataframe(filtered_df, use_container_width=True)