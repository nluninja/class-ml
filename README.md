# Clinical Diagnosis Classification Project

This project contains a Jupyter notebook for machine learning classification of clinical diagnosis data, specifically focused on differentiating between syndrome patients and control subjects.

## Dataset Overview

The notebook analyzes a clinical dataset (`dataset.xlsx`) with:
- **4,048 patients** total
- **273 features** including clinical diagnoses, symptoms, biomarkers, and test results
- **Target variable**: Binary classification (1 = Syndrome, 2 = Control)
- **Class distribution**: ~48% Syndrome patients, ~52% Control subjects

## Data Processing

### Data Validation
The notebook includes comprehensive data validation with 37 conditional rules that ensure data integrity across different feature groups. All validation checks pass successfully (✅).

### Feature Engineering
- **Missing data handling**: Analysis of NaN patterns and removal of features with >70% missing values
- **Feature removal**: Eliminated 3 columns with no informative values:
  - `primary_skin_disease___2`
  - `primary_skin_disease___3` 
  - `specify_primary_skin_condi`
- **Encoding**: Applied OrdinalEncoder for categorical variables

## Machine Learning Models

### 1. Random Forest Classifier
- **Cross-validation accuracy**: 95.6%
- **Test set performance**: 95.7%
- Uses 100 estimators with default hyperparameters
- Handles missing values naturally

### 2. CatBoost Classifier
- **Cross-validation accuracy**: 99.6%
- **Test set performance**: 99.1%
- Superior performance with 300 iterations
- Excellent handling of categorical features and missing values

### 3. Feed-Forward Neural Network (FFNN)
- **Architecture**: 128 → BatchNorm → Dropout(0.3) → 64 → BatchNorm → Dropout(0.3) → 1
- **Regularization**: BatchNormalization, Dropout, EarlyStopping
- **Cross-validation accuracy**: ~99.6%
- Uses data imputation (mean) and standardization
- Includes permutation feature importance analysis

## Key Features

### Feature Importance Analysis
- Top predictive features identified across all models
- Permutation importance calculated for neural network interpretability
- Visualization of most important clinical indicators

### Model Validation
- **Stratified K-Fold Cross-Validation** (5 folds) for all models
- **Confusion matrices** and detailed classification reports
- **Multiple metrics**: Accuracy, Precision, Recall, F1-score

### Data Quality Assurance
- Systematic validation of conditional data relationships
- Missing data analysis and appropriate handling strategies
- Feature selection based on information content

## Results Summary

| Model | CV Accuracy | Test Accuracy | Key Strengths |
|-------|-------------|---------------|---------------|
| Random Forest | 95.6% | 95.7% | Robust, interpretable |
| CatBoost | 99.6% | 99.1% | Best performance, handles categoricals |
| FFNN | 99.6% | - | Deep learning approach, regularized |

## Usage

1. Load the dataset: `dataset.xlsx`
2. Run data validation and preprocessing steps
3. Choose your preferred model (CatBoost recommended for best performance)
4. Evaluate using cross-validation and test set metrics

## Dependencies

- pandas, numpy, matplotlib
- scikit-learn
- catboost
- tensorflow/keras (for neural network)
- autofeat (for automated feature engineering)

The project demonstrates state-of-the-art performance on clinical diagnosis classification with robust validation and comprehensive feature analysis.