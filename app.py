import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Care Transition Analytics",
    layout="wide"
)

st.title("Care Transition Efficiency & Placement Outcome Analytics")

# Read dataset
data = pd.read_csv("data/dataset.csv")

# Convert date column
data["Date"] = pd.to_datetime(data["Date"])

# Clean HHS Care column
data["Children in HHS Care"] = (
    data["Children in HHS Care"]
    .astype(str)
    .str.replace(",", "")
    .astype(float)
)

# Sidebar Date Filter
st.sidebar.title("Select Date Range")

from_date = st.sidebar.date_input(
    "From Date",
    data["Date"].min()
)

to_date = st.sidebar.date_input(
    "To Date",
    data["Date"].max()
)

data = data[
    (data["Date"] >= pd.to_datetime(from_date)) &
    (data["Date"] <= pd.to_datetime(to_date))
]

# Transfer Efficiency
data["Transfer Ratio"] = (
    data["Children transferred out of CBP custody"] /
    data["Children in CBP custody"]
)

transfer_ratio = data["Transfer Ratio"].mean()

# Discharge Effectiveness
data["Discharge Ratio"] = (
    data["Children discharged from HHS Care"] /
    data["Children in HHS Care"]
)

discharge_ratio = data["Discharge Ratio"].mean()

# Backlog Calculation
# Pending children currently present in system

data["Backlog"] = (
    data["Children in CBP custody"] +
    data["Children in HHS Care"]
)

backlog = data["Backlog"].mean()

# Pipeline Throughput
total_input = data[
    "Children apprehended and placed in CBP custody*"
].sum()

total_output = data[
    "Children discharged from HHS Care"
].sum()

pipeline_rate = total_output / total_input

# Outcome Stability Score
stability_score = (
    1 - data["Discharge Ratio"].std()
)

if stability_score < 0:
    stability_score = 0

# Dataset Summary
st.subheader("Dataset Summary")

a, b, c = st.columns(3)

with a:
    st.metric(
        "Total Records",
        len(data)
    )

with b:
    st.metric(
        "Total Columns",
        len(data.columns)
    )

with c:
    st.metric(
        "Average Backlog (Children)",
        round(backlog)
    )

# KPI Section
st.subheader("Performance Metrics")

x, y, z, w = st.columns(4)

with x:
    st.metric(
        "Transfer Efficiency",
        f"{transfer_ratio*100:.1f}%"
    )

with y:
    st.metric(
        "Discharge Effectiveness",
        f"{discharge_ratio*100:.1f}%"
    )

with z:
    st.metric(
        "Pipeline Throughput",
        f"{pipeline_rate:.2f}"
    )

with w:
    st.metric(
        "Outcome Stability",
        f"{stability_score*100:.1f}%"
    )

# Pipeline Flow
st.subheader("Care Pipeline Flow")

p1, p2, p3 = st.columns(3)

with p1:
    st.info(
        f"CBP Custody\n\n{int(data['Children in CBP custody'].mean())}"
    )

with p2:
    st.info(
        f"HHS Care\n\n{int(data['Children in HHS Care'].mean())}"
    )

with p3:
    st.info(
        f"Sponsor Placement\n\n{int(data['Children discharged from HHS Care'].mean())}"
    )

# Alert

st.subheader("Backlog Status")

if backlog > 5000:
    st.warning(
        "High backlog detected in care pipeline"
    )
else:
    st.success(
        "Backlog level is under control"
    )

# Dataset Preview
st.subheader("Sample Data")

st.dataframe(
    data.head(10)
)

# Trend Chart
st.subheader("Care Transition Trend")

movement = data[
    [
        "Date",
        "Children apprehended and placed in CBP custody*",
        "Children transferred out of CBP custody",
        "Children discharged from HHS Care"
    ]
]

movement = movement.set_index("Date")

st.line_chart(movement)

# Backlog Chart
st.subheader("Pending Cases Trend")

st.line_chart(
    data.set_index("Date")["Backlog"]
)

# Bottleneck Detection
st.subheader("Top Bottleneck Periods")

top_backlog = data.nlargest(
    10,
    "Backlog"
)[["Date", "Backlog"]]

st.dataframe(top_backlog)

# Monthly Placement Trend
st.subheader("Monthly Placement Trend")

data["Month"] = data["Date"].dt.to_period("M")

monthly = (
    data.groupby("Month")
    ["Children discharged from HHS Care"]
    .sum()
)

monthly.index = monthly.index.astype(str)

st.bar_chart(monthly)

# Weekday vs Weekend Analysis

st.subheader("Weekday vs Weekend Analysis")

data["Day Type"] = data["Date"].dt.dayofweek.apply(
    lambda x: "Weekend" if x >= 5 else "Weekday"
)

day_analysis = (
    data.groupby("Day Type")
    ["Children transferred out of CBP custody"]
    .mean()
)

st.bar_chart(day_analysis)


# Metric Selection

st.sidebar.subheader("Select Metric")

selected_metric = st.sidebar.selectbox(
    "Choose Analysis",
    [
        "Transfer Ratio",
        "Discharge Ratio",
        "Backlog"
    ]
)


# Selected Metric Analysis

st.subheader("Selected Metric Analysis")

metric_chart = data[
    ["Date", selected_metric]
]

metric_chart = metric_chart.set_index("Date")

st.line_chart(metric_chart)

# Outcome Stability Trend

st.subheader("Outcome Stability Trend")

st.line_chart(
    data.set_index("Date")["Discharge Ratio"]
)

# Monthly Transfer Efficiency Trend

st.subheader("Monthly Transfer Efficiency Trend")

monthly_transfer = (
    data.groupby(
        data["Date"].dt.to_period("M")
    )["Transfer Ratio"]
    .mean()
)

monthly_transfer.index = (
    monthly_transfer.index.astype(str)
)

st.line_chart(
    monthly_transfer
)

# Stagnation Detection

st.subheader("Stagnation Detection")

stagnation_data = data[
    data["Discharge Ratio"] < discharge_ratio
][
    ["Date", "Discharge Ratio"]
]

if len(stagnation_data) > 0:

    st.warning(
        f"{len(stagnation_data)} low-performance days detected."
    )

    st.dataframe(
        stagnation_data.tail(20)
    )

else:

    st.success(
        "No significant stagnation periods detected."
    )

# Sudden Drop Detection

st.subheader("Sudden Drop Detection")

drop_threshold = (
    data["Discharge Ratio"].mean()
    -
    data["Discharge Ratio"].std()
)

sudden_drops = data[
    data["Discharge Ratio"] < drop_threshold
][
    ["Date", "Discharge Ratio"]
]

if len(sudden_drops) > 0:

    st.error(
        f"{len(sudden_drops)} sudden drop events detected."
    )

    st.dataframe(
        sudden_drops.tail(20)
    )

else:

    st.success(
        "No sudden drops detected."
    )