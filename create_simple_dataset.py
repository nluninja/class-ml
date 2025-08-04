#!/usr/bin/env python3
"""
Create a simple synthetic clinical dataset in CSV format
"""

import csv
import random

# Set random seed for reproducibility
random.seed(42)

def generate_simple_dataset():
    """Generate a simplified clinical dataset"""
    
    # Define column names
    columns = [
        'patient_id', 'target',
        # Clinical diagnosis features
        'clinical_diagnosis___1', 'clinical_diagnosis___2', 'clinical_diagnosis___6',
        'clinical_diagnosis___7', 'clinical_diagnosis___8', 'clinical_diagnosis___9',
        # Demographics
        'sex', 'ethnicity', 'race',
        # Symptoms
        'symptoms___1', 'symptoms___2', 'symptoms___3', 'symptoms___4', 'symptoms___5',
        # Joint features
        'inflammatory_arthropathy', 'joint_involvement_type', 'symmetric_polyarthritis',
        # Muscle features
        'muscle', 'weakness_upper_extremity', 'weakness_lower_extremity',
        'muscle_myalgia', 'muscle_tenderness',
        # Lung features
        'lung_involvement', 'nature_lung_involvment',
        # Skin features
        'skin_manifestations_1', 'mechanic_s_hands', 'gottron_papules',
        'heliotrope_rash', 'v_sign', 'shawl_sign',
        # Antibody features
        'ana_1', 'rf_1', 'anti_ccp_1', 'anti_ro52_ssa', 'anti_jo_1',
        'anti_mi_2', 'anti_srp', 'anti_mda_5', 'anti_nxp2_or_mj',
        'anti_tif1_gamma', 'anti_hmgcr', 'anti_sae'
    ]
    
    data = []
    n_samples = 1000  # Smaller dataset for testing
    
    for i in range(1, n_samples + 1):
        # Generate target: syndrome (1) or control (2)
        target = random.choices([1, 2], weights=[0.48, 0.52])[0]  # Slightly imbalanced
        
        row = [i, target]  # patient_id, target
        
        # Generate features based on target to create some signal
        for j, col in enumerate(columns[2:]):
            if 'clinical_diagnosis' in col or 'symptoms' in col:
                # Binary features (0, 1) - syndrome patients more likely to have symptoms
                prob = 0.3 if target == 1 else 0.1
                value = 1 if random.random() < prob else 0
            elif col in ['sex', 'ethnicity', 'race']:
                # Categorical features (1, 2, 3)
                value = random.randint(1, 3)
            elif 'anti_' in col:
                # Antibody tests (1.0, 2.0, 3.0) - syndrome patients more likely positive
                if target == 1:
                    value = random.choices([1.0, 2.0, 3.0], weights=[0.2, 0.3, 0.5])[0]
                else:
                    value = random.choices([1.0, 2.0, 3.0], weights=[0.7, 0.2, 0.1])[0]
            else:
                # Other features (0, 1, 2) - syndrome patients more likely to have abnormalities
                if target == 1:
                    value = random.choices([0, 1, 2], weights=[0.3, 0.4, 0.3])[0]
                else:
                    value = random.choices([0, 1, 2], weights=[0.7, 0.2, 0.1])[0]
            
            # Add some missing values (represented as empty string)
            if random.random() < 0.05:  # 5% missing
                value = ''
            
            row.append(value)
        
        data.append(row)
    
    return columns, data

def save_to_csv(filename, columns, data):
    """Save data to CSV file"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        writer.writerows(data)

def main():
    print("🔬 Generating simple synthetic clinical dataset...")
    
    # Generate dataset
    columns, data = generate_simple_dataset()
    
    print(f"📊 Dataset generated:")
    print(f"   - Samples: {len(data)}")
    print(f"   - Features: {len(columns) - 2}")  # Exclude patient_id and target
    
    # Count target distribution
    syndrome_count = sum(1 for row in data if row[1] == 1)
    control_count = sum(1 for row in data if row[1] == 2)
    
    print(f"   - Target distribution:")
    print(f"     Syndrome (1): {syndrome_count}")
    print(f"     Control (2): {control_count}")
    
    # Save to CSV
    csv_path = "data/dataset.csv"
    save_to_csv(csv_path, columns, data)
    print(f"💾 Dataset saved to: {csv_path}")
    
    # Show sample
    print("\n📋 Sample data (first 3 rows):")
    print("Columns:", columns[:10], "...")
    for i, row in enumerate(data[:3]):
        print(f"Row {i+1}:", row[:10], "...")
    
    print("\n✅ Dataset generation complete!")
    print("💡 You can convert this to Excel format using pandas if needed")

if __name__ == "__main__":
    main()