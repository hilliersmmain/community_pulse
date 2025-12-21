# Community Pulse: Intelligent Data Dashboard

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-Portfolio%20Ready-green)
![Tests](https://img.shields.io/badge/Tests-46%20Passing-success)
![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen)

**Transforming messy, raw member data into actionable insights.**

Community Pulse is a production-ready demonstration of Python data engineering and dashboarding. It takes simulated "dirty" CRM data—riddled with duplicates, typos, and missing values—and passes it through an automated cleaning pipeline to power a live interactive dashboard.

Developed using AI-assisted workflows with GitHub Copilot and modern development practices.

## 🎯 What It Does

1.  **Generates Entropy:** Creates a highly realistic "messy" dataset (simulating a nonprofit's exported CSV).
2.  **Cleans Automatically:** Uses a custom `DataCleaner` class to fix emails, merge duplicates (including fuzzy matching), and standardize dates.
3.  **Calculates Real Metrics:** Data Health Score formula: `100 - (duplicate_rate + invalid_email_rate + missing_rate)`.
4.  **Predicts Trends:** 3-month moving average for attendance forecasting.
5.  **Visualizes Impacts:** Shows immediate "Before vs. After" metrics and interactive Plotly charts of the cleaned data.

## ✨ Key Features

### Data Quality & Cleaning
- **Automated Data Cleaning Pipeline:** Handles duplicates, fuzzy string matching (names), and type coercion
- **Fuzzy Name Matching:** Detects near-duplicates using Levenshtein distance (e.g., "John Smith" vs "Jon Smith")
- **Email Validation:** Regex pattern matching with automatic correction
- **Date Standardization:** Parses multiple formats, detects future dates as quality issues
- **Schema Validation:** Ensures required columns exist before processing

### Analytics & Visualization
- **Interactive Analytics:** Real-time Plotly charts for attendance trends, role distribution, and engagement
- **Real Predictive Analytics:** 3-month moving average calculation for attendance forecasting
- **Dynamic KPIs:** Data health score, email validity rate, duplicate percentage, missing values
- **Role-Based Filtering:** Segment dashboard by member type

### Security & Reliability
- **CSV File Upload:** Users can upload their own data (max 50MB)
- **CSV Injection Protection:** Sanitizes dangerous formula patterns
- **File Size Limits:** Prevents resource exhaustion
- **Error Boundaries:** Comprehensive try-catch blocks prevent crashes
- **Input Validation:** Schema and type checking

### Code Quality
- **Type Hints:** 100% coverage on public functions
- **Logging:** Python logging module instead of print statements
- **Configuration Management:** Centralized config.py for all settings
- **46 Automated Tests:** Edge cases, empty data, malformed inputs
- **CI/CD Pipeline:** GitHub Actions workflow for automated testing

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Data Processing:** Pandas, NumPy
- **Visualization:** Plotly Express
- **Data Generation:** Faker
- **Fuzzy Matching:** python-Levenshtein
- **Testing:** pytest
- **CI/CD:** GitHub Actions

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip package manager
- Git (for cloning)

### Installation by Operating System

#### **Windows**

1.  Clone the repository:
    ```cmd
    git clone https://github.com/hilliersmmain/community_pulse.git
    cd community_pulse
    ```

2.  Create a virtual environment:
    ```cmd
    python -m venv venv
    venv\Scripts\activate
    ```

3.  Install dependencies:
    ```cmd
    pip install -r requirements.txt
    ```

4.  Run the application:
    ```cmd
    streamlit run app.py
    ```

5.  Open your browser to `http://localhost:8501`

#### **macOS**

1.  Clone the repository:
    ```bash
    git clone https://github.com/hilliersmmain/community_pulse.git
    cd community_pulse
    ```

2.  Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  Run the application:
    ```bash
    streamlit run app.py
    ```

5.  Open your browser to `http://localhost:8501`

#### **Linux (Ubuntu/Debian)**

1.  Install Python 3.9+ if not already installed:
    ```bash
    sudo apt update
    sudo apt install python3.9 python3.9-venv python3-pip
    ```

2.  Clone the repository:
    ```bash
    git clone https://github.com/hilliersmmain/community_pulse.git
    cd community_pulse
    ```

3.  Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5.  Run the application:
    ```bash
    streamlit run app.py
    ```

6.  Open your browser to `http://localhost:8501`

### Quick Start (Any OS)

After installation, you can:
1. Click **"Generate New Messy Data"** to create sample data
2. Navigate to the **"Data Cleaning Ops"** tab
3. Click **"Run Cleaning Algorithms"** to see the pipeline in action
4. Explore the **"Analytics Dashboard"** tab for insights
5. Download cleaned data as CSV

## 📊 Screenshots

### Dashboard Overview
![Dashboard Main View](docs/screenshots/dashboard_main.png)
*Main dashboard showing KPI metrics before cleaning*

### Data Cleaning Pipeline
![Cleaning Execution](docs/screenshots/cleaning_pipeline.png)
*Real-time execution log and data health score calculation*

### Analytics Visualizations
![Analytics Charts](docs/screenshots/analytics_charts.png)
*Interactive Plotly charts with attendance predictions*

### Before/After Comparison
![Data Quality Improvement](docs/screenshots/before_after.png)
*Demonstrating impact of cleaning pipeline on data quality metrics*

## 📂 Project Structure

```text
community_pulse/
├── app.py                     # Main Streamlit application
├── config.py                  # Configuration management
├── requirements.txt           # Pinned dependencies
├── data/                      # Local data storage (gitignored)
├── docs/
│   ├── ARCHITECTURE.md        # System architecture diagram
│   ├── SKILLS_MAPPING.md      # Job requirements mapping
│   ├── KPI_DEFINITIONS.md     # Metrics documentation
│   └── SOP_DATA_CLEANING.md   # Standard operating procedures
├── tests/
│   ├── test_cleaner.py        # Core cleaner tests
│   ├── test_cleaner_edge_cases.py  # Edge case tests
│   ├── test_data_generator.py # Generator tests
│   └── test_visualizer.py     # Visualization tests
└── utils/
    ├── data_generator.py      # Creates messy sample data
    ├── cleaner.py             # Core cleaning logic
    └── visualizer.py          # Plotly charting functions
```

## 🧪 Testing

Run the full test suite:

```bash
pytest tests/ -v
```

Run with coverage:

```bash
pytest tests/ --cov=utils --cov-report=html
```

All 46 tests pass with 100% coverage on core modules.

## 🐳 Docker Deployment

Build and run with Docker:

```bash
docker build -t community-pulse .
docker run -p 8501:8501 community-pulse
```

Or use Docker Compose for development:

```bash
docker-compose up
```

## ☁️ Live Demo

**Streamlit Cloud Deployment:** [community-pulse.streamlit.app](https://community-pulse.streamlit.app)

*Note: Demo may be in sleep mode. Click the link to wake it up.*

## 🎓 Portfolio Context

This project was designed to demonstrate specific competencies for Data Science roles:

- **Data Cleaning:** Handling real-world dirty data (Target: Autism Strong Foundation)
- **Dashboarding:** Building KPI visualizations (Target: Transfer Center)
- **App Development:** Creating functional software tools (Target: Pivot Point Analytics)

See [SKILLS_MAPPING.md](docs/SKILLS_MAPPING.md) for detailed job requirement alignment.

## 📚 Documentation

- **[Architecture Diagram](docs/ARCHITECTURE.md)** - System design and data flow
- **[Skills Mapping](docs/SKILLS_MAPPING.md)** - Job requirements alignment
- **[KPI Definitions](docs/KPI_DEFINITIONS.md)** - Metric calculations
- **[Data Cleaning SOP](docs/SOP_DATA_CLEANING.md)** - Standard procedures

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🔗 Links

- **GitHub Repository:** [github.com/hilliersmmain/community_pulse](https://github.com/hilliersmmain/community_pulse)
- **Live Demo:** [community-pulse.streamlit.app](https://community-pulse.streamlit.app)
- **Documentation:** [docs/](docs/)

## 👤 Author

**hilliersmmain**
- GitHub: [@hilliersmmain](https://github.com/hilliersmmain)
- Project: [Community Pulse](https://github.com/hilliersmmain/community_pulse)

---

*Built with ❤️ using AI-assisted development practices*
