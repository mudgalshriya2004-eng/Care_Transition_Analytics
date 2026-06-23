# Care Transition Efficiency & Placement Outcome Analytics

## Overview

The **Care Transition Efficiency & Placement Outcome Analytics** project analyzes the operational performance of the Unaccompanied Alien Children (UAC) care pipeline managed by the U.S. Department of Health and Human Services (HHS).

The project focuses on measuring how effectively children move through different stages of the care process, identifying bottlenecks, monitoring outcome stability, and evaluating overall system efficiency through interactive analytics and visualizations.

A Streamlit-based dashboard is developed to provide real-time insights into care transitions, discharge outcomes, backlog accumulation, and process performance trends.

---

# Problem Statement

The UAC care system operates as a multi-stage pipeline consisting of:

1. Apprehension and CBP Custody
2. Transfer to HHS Care
3. Medical Screening and Case Management
4. Sponsor Placement and Reunification

Although aggregate custody counts are monitored regularly, process efficiency metrics are often unavailable.

Key questions addressed by this project include:

* How efficiently are children transferred from CBP custody to HHS care?
* Are sponsor placements keeping pace with new arrivals?
* When do care backlogs accumulate?
* Are placement outcomes improving or deteriorating over time?
* Which stages of the process create bottlenecks?

---

# Project Objectives

## Primary Objectives

* Measure CBP → HHS transfer efficiency.
* Evaluate discharge and sponsor placement outcomes.
* Identify care pipeline delays and bottlenecks.
* Monitor operational performance using process analytics.

## Secondary Objectives

* Support faster reunification efforts.
* Improve case management visibility.
* Assist policy-level decision making.
* Enable data-driven monitoring of care transitions.

---

# Dataset Description

The dataset contains daily operational records related to the UAC care process.

| Column Name                                    | Description                   |
| ---------------------------------------------- | ----------------------------- |
| Date                                           | Reporting date                |
| Children apprehended and placed in CBP custody | Daily intake volume           |
| Children in CBP custody                        | Active CBP care load          |
| Children transferred out of CBP custody        | Transfers into HHS care       |
| Children in HHS Care                           | Active HHS care load          |
| Children discharged from HHS Care              | Successful sponsor placements |

---

# Analytical Methodology

## 1. Care Pipeline Modeling

The UAC process is modeled as a flow-based pipeline:

CBP Custody → HHS Care → Sponsor Placement

This enables monitoring of daily movement between stages and identification of process inefficiencies.

---

## 2. Transition Efficiency Analysis

The following metrics are used to evaluate system performance:

### Transfer Efficiency Ratio

Measures how effectively children move from CBP custody into HHS care.

Transfer Efficiency Ratio = Transfers ÷ CBP Custody

### Discharge Effectiveness

Measures sponsor placement performance.

Discharge Effectiveness = Discharges ÷ HHS Care

### Pipeline Throughput Rate

Measures overall movement through the care pipeline.

Pipeline Throughput = Total Exits ÷ Total Entries

---

## 3. Backlog Analysis

Backlog is used to identify unresolved cases and system pressure.

The project analyzes:

* Pending case trends
* Backlog accumulation
* High-pressure periods
* Bottleneck detection

---

## 4. Temporal Analysis

Performance trends are analyzed over time using:

* Daily trend monitoring
* Monthly transfer efficiency trends
* Monthly placement trends
* Weekday vs Weekend analysis

---

## 5. Outcome Stability Analysis

Outcome consistency is evaluated through:

* Outcome Stability Score
* Stability trend visualization
* Stagnation detection
* Sudden drop detection

---

# Key Performance Indicators (KPIs)

| KPI                       | Purpose                             |
| ------------------------- | ----------------------------------- |
| Transfer Efficiency Ratio | Measures CBP → HHS transition speed |
| Discharge Effectiveness   | Measures sponsor placement success  |
| Pipeline Throughput Rate  | Measures overall system movement    |
| Backlog Accumulation      | Indicates delay severity            |
| Outcome Stability Score   | Measures consistency of outcomes    |

---

# Dashboard Features

## Dataset Summary

* Total Records
* Total Columns
* Average Backlog

## Performance Metrics

* Transfer Efficiency
* Discharge Effectiveness
* Pipeline Throughput
* Outcome Stability

## Care Pipeline Flow

Visual representation of:

* CBP Custody
* HHS Care
* Sponsor Placement

## Trend Analysis

* Care Transition Trend
* Monthly Placement Trend
* Monthly Transfer Efficiency Trend

## Bottleneck Detection

* Pending Cases Trend
* Top Bottleneck Periods
* Backlog Monitoring

## Outcome Analysis

* Outcome Stability Trend
* Stagnation Detection
* Sudden Drop Detection

## Interactive Controls

* Date Range Selection
* Metric Selection Toggle
* Threshold-Based Alerts

---

# Technologies Used

* Python
* Pandas
* Streamlit

---

# Project Structure

Care_Transition_Analytics/

├── data/

│ └── dataset.csv

│

├── assets/

│ └── dashboard screenshots (optional)

│

├── app.py

├── README.md

├── requirements.txt

│

└── .gitignore (optional)

---

# Installation and Setup

## Clone Repository

git clone https://github.com/mudgalshriya2004-eng/Care_Transition_Analytics.git

cd Care_Transition_Analytics

## Install Dependencies

pip install -r requirements.txt

## Run Application

streamlit run app.py

After running the command, open the local URL displayed in the terminal.

---

# Key Findings

* Transfer efficiency remains relatively stable across the observed period.
* Large active care loads indicate sustained operational demand.
* Discharge effectiveness highlights opportunities to improve sponsor placement timelines.
* Backlog analysis helps identify periods of workflow pressure.
* Outcome stability analysis shows consistency of care transition outcomes.
* Bottleneck detection enables proactive intervention and resource planning.

---

# Recommendations

* Improve sponsor verification workflows to accelerate reunification.
* Allocate additional resources during high-backlog periods.
* Monitor transition efficiency continuously using dashboard analytics.
* Implement automated alerts for emerging bottlenecks.
* Use data-driven insights to support policy and operational decisions.

---

# Future Enhancements

* Predictive backlog forecasting using machine learning.
* Advanced trend prediction models.
* Geographic analysis of care facilities.
* Automated reporting and notification systems.
* Interactive policy simulation modules.

---

# Conclusion

This project transforms traditional capacity monitoring into a process-oriented analytics framework. By evaluating transfer efficiency, discharge performance, bottlenecks, backlog accumulation, and outcome stability, the dashboard provides actionable insights that support faster reunification, improved workflow management, and informed policy decisions.

---

# Author

**Shriya Mudgal**

AI & Machine Learning Enthusiast

Care Transition Efficiency & Placement Outcome Analytics Project
