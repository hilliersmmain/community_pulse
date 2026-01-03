# Configuration Guide

This document describes all configuration options available for the Community Pulse application.

---

## Environment Variables

Community Pulse can be configured using environment variables. Copy `.env.example` to `.env` and customize as needed.

### Streamlit Configuration

```bash
# Server Settings
STREAMLIT_SERVER_PORT=8501          # Port for the application (default: 8501)
STREAMLIT_SERVER_ADDRESS=localhost  # Address to bind to (default: localhost)
STREAMLIT_THEME_BASE=light          # Theme: 'light' or 'dark' (default: light)
```

**Note:** Streamlit configurations can also be set in `.streamlit/config.toml` for more advanced options.

---

### Data Generation Defaults

```bash
DEFAULT_NUM_RECORDS=500     # Default number of records to generate (100-1000)
DEFAULT_MESSINESS=medium    # Default data quality level: 'low', 'medium', or 'high'
```

These values are used as initial settings in the UI sidebar. Users can override them during runtime.

---

### Logging Configuration

```bash
LOG_LEVEL=INFO              # Logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE=logs/app.log       # Path to log file (created automatically)
```

**Log Levels:**

- `DEBUG`: Detailed diagnostic information
- `INFO`: General informational messages (recommended for production)
- `WARNING`: Warning messages for potentially problematic situations
- `ERROR`: Error messages for serious problems
- `CRITICAL`: Critical errors that may cause application failure

---

### Feature Flags

```bash
ENABLE_TUTORIAL_MODE=true           # Show tutorial hints for first-time users
ENABLE_ADVANCED_ANALYTICS=false     # Enable experimental analytics features
```

Feature flags allow you to toggle specific functionality without code changes.

---

### Export Configuration

```bash
EXPORT_FORMAT=csv                   # Default export format: 'csv' or 'json'
EXPORT_INCLUDE_TIMESTAMP=true       # Add timestamp to exported filenames
```

---

## Streamlit Configuration File

Advanced Streamlit options can be configured in `.streamlit/config.toml`:

```toml
[server]
port = 8501
headless = true
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

Refer to the [Streamlit documentation](https://docs.streamlit.io/library/advanced-features/configuration) for all available options.

---

## Application Constants

Some configuration options are defined as constants in the code:

### Data Generator (`utils/data_generator.py`)

```python
MIN_RECORDS = 100        # Minimum number of records allowed
MAX_RECORDS = 1000       # Maximum number of records allowed
DEFAULT_SAVE_PATH = "data/messy_club_data.csv"
```

### Health Metrics (`utils/health_metrics.py`)

```python
# Health Score Weights
COMPLETENESS_WEIGHT = 0.40    # 40% weight for completeness
UNIQUENESS_WEIGHT = 0.30      # 30% weight for uniqueness
FORMATTING_WEIGHT = 0.30      # 30% weight for formatting
```

These weights determine how the overall health score is calculated.

---

## Data Schema

The application expects the following column structure:

```python
REQUIRED_COLUMNS = [
    'Name',              # Member name (text)
    'Email',             # Email address (text, validated format)
    'JoinDate',          # Date joined (YYYY-MM-DD format)
    'AttendanceCount',   # Number of events attended (integer)
    'Role',              # Member role (text: Member, Volunteer, Admin)
    'Status',            # Membership status (text: Active, Inactive)
]
```

**Custom Data Import:** If you're importing your own CSV files, ensure they match this schema.

---

## Cleaning Pipeline Configuration

### Default Cleaning Steps

The application runs these cleaning steps by default:

1. **standardize_names** - Capitalizes names, removes extra whitespace
2. **fix_emails** - Validates email format, removes invalid entries
3. **remove_duplicates** - Removes duplicate records based on email
4. **clean_dates** - Standardizes date format to YYYY-MM-DD
5. **handle_missing_values** - Fills or removes missing values

### Configurable in UI

Users can toggle individual cleaning steps via the sidebar:

- ☑️ Check to enable a step
- ☐ Uncheck to skip a step

---

## Testing Configuration

### pytest Configuration

Tests can be configured via command-line arguments:

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=utils --cov=community_pulse --cov-report=term

# Run specific test file
pytest tests/test_cleaner.py

# Run with verbose output
pytest -v

# Run tests matching a pattern
pytest -k "test_email"
```

### Test Data

Tests use controlled datasets defined in test files. No external data files are required.

---

## Performance Tuning

### Memory Optimization

For large datasets (close to 1000 records):

```python
# Reduce memory usage by processing in chunks
CHUNK_SIZE = 100  # Process 100 records at a time
```

**Note:** The current implementation loads all data into memory. For datasets larger than 1000 records, consider implementing chunked processing.

---

### Chart Rendering

Plotly charts can be optimized:

```python
# In .streamlit/config.toml
[runner]
fastReruns = true  # Faster chart updates (may reduce stability)
```

---

## Deployment Configuration

### Streamlit Cloud

Required files for Streamlit Cloud deployment:

- `requirements.txt` - Python dependencies
- `.streamlit/config.toml` - Streamlit configuration (optional)
- No environment variables needed (uses defaults)

### Docker Deployment

See `Dockerfile` in repository root for Docker configuration.

Required environment variables for Docker:

```bash
docker run -p 8501:8501 \
  -e STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
  -e LOG_LEVEL=INFO \
  community-pulse
```

---

## Security Configuration

### Secrets Management

Never commit sensitive information to the repository. Use Streamlit secrets:

Create `.streamlit/secrets.toml` (git-ignored):

```toml
[database]
connection_string = "postgresql://user:pass@host:5432/db"

[api]
api_key = "your-secret-api-key"
```

Access in code:

```python
import streamlit as st
db_connection = st.secrets["database"]["connection_string"]
```

---

## Troubleshooting Configuration Issues

### Configuration Not Loading

1. Verify file paths are correct
2. Ensure proper file permissions (`chmod 644 .env`)
3. Restart the application after configuration changes
4. Check for syntax errors in TOML files

### Environment Variables Not Working

```bash
# Verify environment variable is set
echo $LOG_LEVEL  # Unix/Linux
echo %LOG_LEVEL%  # Windows

# Set temporarily for current session
export LOG_LEVEL=DEBUG  # Unix/Linux
set LOG_LEVEL=DEBUG     # Windows
```

---

## Default vs. Custom Configuration

**Default Configuration:**

- Located in code constants
- Works out of the box
- Suitable for most users

**Custom Configuration:**

- Use `.env` file for environment variables
- Use `.streamlit/config.toml` for Streamlit settings
- Recommended for advanced users and production deployments

---

## Configuration Precedence

When multiple configuration sources exist, they are applied in this order (later overrides earlier):

1. Code constants (lowest priority)
2. `.streamlit/config.toml`
3. Environment variables
4. Command-line arguments (highest priority)

Example:

```bash
# This will override .env and config.toml settings
STREAMLIT_SERVER_PORT=9000 streamlit run app.py
```

---

## Further Reading

- [Streamlit Configuration Documentation](https://docs.streamlit.io/library/advanced-features/configuration)
- [Python Environment Variables](https://docs.python.org/3/using/cmdline.html#environment-variables)
- [python-dotenv Documentation](https://github.com/theskumar/python-dotenv)

For questions or issues, refer to the [ERROR_HANDLING.md](./ERROR_HANDLING.md) guide.
