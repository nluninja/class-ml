# Dataset Directory

This directory contains synthetic clinical diagnosis datasets for testing the machine learning models.

## Files

### `dataset.csv`
- **Format**: Comma-separated values
- **Samples**: 1,000 patients
- **Features**: 42 clinical features
- **Target**: Binary classification (1=Syndrome, 2=Control)
- **Missing Data**: ~5% missing values to simulate real-world conditions

### `dataset.xlsx`
- **Format**: Excel XML format
- **Content**: Same data as CSV but in Excel-compatible format
- **Usage**: Can be opened directly in Microsoft Excel or LibreOffice Calc

## Dataset Structure

### Target Variable
- **1**: Syndrome patients (494 samples, ~49.4%)
- **2**: Control subjects (506 samples, ~50.6%)

### Feature Categories

1. **Clinical Diagnosis** (6 features)
   - Binary indicators (0/1) for various clinical diagnoses
   - Higher prevalence in syndrome patients

2. **Demographics** (3 features)
   - `sex`, `ethnicity`, `race`
   - Categorical values (1, 2, 3)

3. **Symptoms** (5 features)
   - Binary indicators for various symptoms
   - More common in syndrome patients

4. **Joint Features** (3 features)
   - Arthropathy and joint involvement indicators
   - Ordinal scale (0, 1, 2)

5. **Muscle Features** (5 features)
   - Muscle weakness and related symptoms
   - Mixed binary and ordinal scales

6. **Lung Features** (2 features)
   - Pulmonary involvement indicators
   - Ordinal scale (0, 1, 2)

7. **Skin Features** (6 features)
   - Dermatological manifestations
   - Binary and ordinal scales

8. **Antibody Tests** (12 features)
   - Various autoantibody test results
   - Scale (1.0, 2.0, 3.0) representing negative/borderline/positive
   - Syndrome patients more likely to have positive results

## Data Generation

The dataset was synthetically generated using the following approach:
- **Base Structure**: Mimics the original clinical dataset structure
- **Signal Creation**: Target-dependent feature generation
- **Realistic Patterns**: Syndrome patients have higher probability of positive findings
- **Missing Data**: Random 5% missing values across features
- **Class Balance**: Approximately balanced with slight control majority

## Usage in Notebook

To use this dataset in the Jupyter notebook, simply update the data loading path:

```python
# Replace the original data loading line with:
df = pd.read_excel("data/dataset.xlsx")
# or
df = pd.read_csv("data/dataset.csv")
```

## Notes

- This is synthetic data created for testing and demonstration purposes
- The patterns and relationships are artificially generated
- Real clinical data would have more complex relationships and domain-specific constraints
- Missing values are represented as empty cells in Excel and empty strings in CSV