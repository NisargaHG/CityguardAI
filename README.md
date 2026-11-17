# CityGuard AI – Intelligent Urban Traffic Disruption Management System

**Smarter Decisions. Safer Cities. Better Mobility.**

CityGuard AI is a data-driven urban traffic disruption management and decision-support platform designed to help analyze planned and unexpected traffic incidents.

The project uses structured Bengaluru traffic event data, incident prioritization and an Urban Disruption Score (UDS) to provide insights into traffic disruptions, identify vulnerable zones and support better operational planning.

## Project Overview

Urban traffic networks face several disruptions that affect mobility, public safety and emergency response.

Examples include:

- Road accidents
- Vehicle breakdowns
- Waterlogging
- Road construction
- Tree falls
- Public events and rallies
- Processions and protests
- VIP movements
- Unexpected traffic congestion

Traditional traffic management often depends on manual monitoring and delayed incident reporting.

CityGuard AI explores a data-driven approach to analyzing these disruptions through an interactive dashboard and risk assessment mechanisms.

## Key Features

### 1. Interactive Traffic Management Dashboard

- Centralized visualization of traffic incidents.
- Total incident statistics.
- Planned and unplanned event monitoring.
- Active incident tracking.
- Operational Key Performance Indicators (KPIs).

### 2. Urban Disruption Score (UDS)

The Urban Disruption Score is used to evaluate and prioritize traffic incidents.

The current implementation calculates UDS using:

- Incident priority.
- Road closure requirement.
- Event type (planned or unplanned).

The score supports incident prioritization and traffic disruption analysis.

### 3. Traffic Incident Analysis

The dashboard provides visual analysis of:

- Most frequently occurring incident types.
- Distribution of incidents across traffic zones.
- Average Urban Disruption Score.
- Maximum Urban Disruption Score.
- Critical incidents based on the configured UDS threshold.

### 4. Zone Vulnerability Analysis

The system groups incidents by traffic zone and calculates average UDS to generate a zone vulnerability ranking.

This helps identify areas with higher incident-related disruption scores.

### 5. Data Visualization

Interactive dashboard elements provide:

- Incident distribution charts.
- Top traffic-zone charts.
- UDS statistical metrics.
- Zone vulnerability rankings.

## System Workflow

```text
      Bengaluru Traffic Events Dataset
                    |
                    v
             Data Processing
                 Pandas
                    |
                    v
           Incident Classification
                    |
                    v
          Urban Disruption Score
                    |
                    v
           Risk Analysis & Metrics
                    |
             +------+------+
             |             |
             v             v
        Incident       Zone-Level
        Analysis       Analysis
             |             |
             +------+------+
                    |
                    v
          Streamlit Dashboard
                    |
                    v
       Traffic Decision Support
```

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Dashboard | Streamlit |
| Data Processing | Pandas |
| Data Storage | CSV |
| Risk Assessment | Urban Disruption Score |
| Visualization | Streamlit Charts |
| Development Environment | VS Code |
| Version Control | Git and GitHub |

## Dataset – Bengaluru Traffic Events

The project uses a structured Bengaluru traffic events dataset for analyzing urban disruptions.

The dataset includes information such as:

- Event type.
- Incident cause.
- Incident priority.
- Incident status.
- Road closure requirement.
- Traffic zone information.
- Geographic location information, where available.

### Supported Incident Categories

1. Vehicle Breakdown
2. Road Accident
3. Waterlogging
4. Construction
5. Tree Fall
6. Public Event
7. Procession
8. Protest
9. VIP Movement
10. Traffic Congestion

## Project Structure

```text
CityguardAI/
│
├── data/
│   └── events.csv
│
├── models/
│
├── notebooks/
│
├── pages/
│
├── utils/
│   └── uds.py
│
├── Dashboard.py
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10 or later (use a version compatible with the project dependencies).
- pip package manager.
- Git.
- VS Code or another Python IDE.

### 1. Clone the Repository

```bash
git clone https://github.com/NisargaHG/CityguardAI.git

cd CityguardAI
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Dashboard

```bash
streamlit run Dashboard.py
```

The dashboard will open in your browser, usually at:

```text
http://localhost:8501
```

## Sample Dashboard Analytics

The dashboard calculates and displays:

| Metric | Description |
|---|---|
| Total Incidents | Total records in the dataset |
| Planned Events | Number of planned events |
| Unplanned Events | Number of unplanned events |
| Active Incidents | Number of active incidents |
| Average UDS | Mean Urban Disruption Score |
| Maximum UDS | Highest calculated UDS |
| Critical Incidents | Incidents with UDS greater than or equal to 90 |
| Zone Vulnerability | Ranking based on average UDS per zone |

## Future Enhancements

The project can be extended with:

- Live traffic data integration.
- Automated incident detection using CCTV feeds.
- Advanced traffic congestion prediction.
- Geospatial risk heatmaps.
- Emergency resource allocation recommendations.
- Digital twin-based traffic intervention simulation.
- AI-assisted traffic management recommendations.
- Emergency vehicle tracking.
- Smart traffic signal coordination.
- Historical incident analysis and model improvement.

## Project Objective

CityGuard AI aims to support smarter urban traffic management by transforming structured traffic event data into meaningful insights.

Through incident analysis, risk scoring and interactive visualization, the project explores how data-driven decision support can improve urban mobility planning and emergency response coordination.


---

*CityGuard AI – Smarter Decisions. Safer Cities. Better Mobility.*
