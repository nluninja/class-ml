# Test Scripts Directory

This directory contains Python scripts for generating synthetic datasets for testing the machine learning models.

## Scripts

### `create_simple_dataset.py`
**Main dataset generation script**
- Creates a synthetic clinical diagnosis dataset with 1,000 samples
- Generates 42 clinical features across multiple categories
- Outputs CSV format (`data/dataset.csv`)
- Uses only Python standard library (no external dependencies)
- Includes realistic missing data patterns (~5% missing values)

**Usage:**
```bash
python3 create_simple_dataset.py
```

### `convert_to_excel.py`
**CSV to Excel converter**
- Converts the generated CSV file to Excel XML format
- Creates `data/dataset.xlsx` compatible with Microsoft Excel
- Uses only standard library XML modules
- Handles different data types (numbers, strings, empty cells)

**Usage:**
```bash
python3 convert_to_excel.py
```

### `generate_dataset.py`
**Advanced dataset generator (requires external libraries)**
- More sophisticated dataset generation using scikit-learn
- Creates larger datasets with more realistic feature relationships
- Requires pandas, scikit-learn, and openpyxl
- Currently not functional due to system package restrictions

**Note:** This script requires additional packages that may not be available in all environments.

## Generated Data Structure

The scripts generate synthetic clinical data with the following structure:

### Features (42 total)
- **Clinical Diagnosis** (6): Binary indicators for various diagnoses
- **Demographics** (3): Sex, ethnicity, race (categorical 1-3)
- **Symptoms** (5): Binary symptom indicators
- **Joint Features** (3): Arthropathy and joint involvement (ordinal 0-2)
- **Muscle Features** (5): Muscle weakness and symptoms (mixed scales)
- **Lung Features** (2): Pulmonary involvement (ordinal 0-2)
- **Skin Features** (6): Dermatological manifestations (binary/ordinal)
- **Antibody Tests** (12): Autoantibody results (1.0-3.0 scale)

### Target Variable
- **1**: Syndrome patients (~49%)
- **2**: Control subjects (~51%)

## Data Characteristics

- **Realistic patterns**: Syndrome patients have higher probability of positive findings
- **Missing data**: Random 5% missing values to simulate real-world conditions
- **Balanced classes**: Approximately equal distribution of syndrome/control cases
- **Signal-rich**: Features contain meaningful patterns for ML model training

## Usage in Main Project

After running the generation scripts, update the notebook data loading path:

```python
# Load the synthetic dataset
df = pd.read_excel("data/dataset.xlsx")
# or
df = pd.read_csv("data/dataset.csv")
```

## Notes

- These are synthetic datasets created for testing and demonstration
- Real clinical data would have more complex relationships and constraints
- The generated patterns are simplified but sufficient for ML model validation
- Scripts are designed to work in environments with minimal Python dependencies