# Error Handling Guide

This guide documents common errors you may encounter when using Community Pulse and their solutions.

---

## Common Errors

### FileNotFoundError: 'data/messy_club_data.csv'

**Cause:** No data has been generated yet, or the data file was deleted.

**Solution:**

1. Navigate to the sidebar in the application
2. Click **"Generate New Data"** button
3. Adjust the number of records and messiness level if needed
4. The data file will be created automatically

**Prevention:** Always generate data before attempting to run cleaning operations.

---

### ValueError: Invalid messiness level

**Cause:** Incorrect parameter passed to the data generator function.

**Solution:** Use only the following valid messiness levels:

- `'low'` - Minimal data quality issues
- `'medium'` - Moderate data quality issues (recommended)
- `'high'` - Severe data quality issues

**Example:**

```python
from utils.data_generator import generate_messy_data

# Correct usage
generate_messy_data(500, "data/sample.csv", "medium")

# Incorrect usage (will raise ValueError)
generate_messy_data(500, "data/sample.csv", "extreme")  # ❌
```

---

### MemoryError: Cannot allocate memory

**Cause:** Dataset is too large for available system RAM, or insufficient memory for data processing.

**Solution:**

1. **Reduce dataset size:** Lower the number of records (try 100-500 instead of 1000)
2. **Close other applications:** Free up system memory
3. **Restart the application:** Clear any cached data

**System Requirements:**

- **Minimum RAM:** 2GB available
- **Recommended RAM:** 4GB+ for smooth operation
- **Maximum records:** 1000 (enforced by application)

---

### KeyError: 'ColumnName' not found

**Cause:** Required column is missing from the dataset, or column name mismatch.

**Solution:**

1. Regenerate the data using the built-in data generator
2. Verify that imported CSV files have the expected columns:
   - `Name`, `Email`, `JoinDate`, `AttendanceCount`, `Role`, `Status`

**For custom data:** Ensure your CSV matches the expected schema before importing.

---

### StreamlitAPIException: Widget outside of form

**Cause:** Internal Streamlit state management issue, typically due to rapid interactions.

**Solution:**

1. Refresh the browser page
2. Restart the Streamlit application: `streamlit run app.py`

---

### ModuleNotFoundError: No module named 'package_name'

**Cause:** Required Python package is not installed in your environment.

**Solution:**

```bash
# Activate your virtual environment first
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install all required packages
pip install -r requirements.txt

# Or install specific missing package
pip install package_name
```

**Verify installation:**

```bash
python verify_setup.py
```

---

### plotly.exceptions.PlotlyError: Invalid figure

**Cause:** Insufficient data to generate visualization, or data type mismatch.

**Solution:**

1. Ensure dataset has at least 10 records for meaningful visualizations
2. Verify data has been cleaned before attempting advanced analytics
3. Check that date columns are properly formatted

---

## Testing-Specific Errors

### pytest: command not found

**Cause:** pytest is not installed or not in your PATH.

**Solution:**

```bash
pip install pytest pytest-cov
pytest --version  # Verify installation
```

---

### AssertionError in tests

**Cause:** Test expectations don't match actual behavior (likely due to code changes).

**Solution:**

1. Review the specific test that failed
2. Check if the test expectations are still valid
3. Update tests if functionality has intentionally changed
4. Run individual test for debugging: `pytest tests/test_file.py::test_function_name -v`

---

## Deployment Errors

### Streamlit Cloud: requirements.txt missing

**Cause:** Streamlit Cloud cannot find the dependencies file.

**Solution:**

1. Ensure `requirements.txt` is in the repository root
2. Commit and push the file to GitHub
3. Redeploy the application

---

### Streamlit Cloud: Module import error

**Cause:** Package version mismatch or missing system dependencies.

**Solution:**

1. Pin exact versions in `requirements.txt`:
   ```
   streamlit==1.52.2
   pandas==2.2.2
   ```
2. Check Streamlit Cloud logs for specific error messages
3. Ensure Python version compatibility (3.9+)

---

## Getting Help

If you encounter an error not listed here:

1. **Check the logs:** Review terminal output or Streamlit Cloud logs
2. **Search Issues:** Check the [GitHub Issues](https://github.com/hilliersmmain/community_pulse/issues) page
3. **Create an Issue:** Provide:
   - Error message (full traceback)
   - Steps to reproduce
   - Your environment (OS, Python version)
   - Expected vs. actual behavior

---

## Debug Mode

Enable verbose logging for troubleshooting:

```bash
# Set environment variable before running
export LOG_LEVEL=DEBUG  # On Windows: set LOG_LEVEL=DEBUG
streamlit run app.py
```

This will provide detailed information about application operations and data transformations.

---

## Prevention Best Practices

1. **Always use virtual environments:** Prevents package conflicts
2. **Verify setup after installation:** Run `python verify_setup.py`
3. **Generate data before cleaning:** Follow the workflow order
4. **Keep dependencies updated:** Regularly run `pip install --upgrade -r requirements.txt`
5. **Run tests before deployment:** `pytest` to catch issues early
