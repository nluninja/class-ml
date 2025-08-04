#!/usr/bin/env python3
"""
Generate synthetic clinical diagnosis dataset for testing
"""

import pandas as pd
import numpy as np
from sklearn.datasets import make_classification

# Set random seed for reproducibility
np.random.seed(42)

def generate_clinical_dataset(n_samples=4048, n_features=270):
    """Generate synthetic clinical dataset matching the original structure"""
    
    # Generate base classification data
    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=100,
        n_redundant=50,
        n_clusters_per_class=3,
        n_classes=2,
        class_sep=0.8,
        random_state=42
    )
    
    # Convert target to match original (1=syndrome, 2=control)
    y = y + 1
    y[y == 1] = 1  # syndrome
    y[y == 2] = 2  # control
    
    # Create DataFrame
    feature_names = []
    
    # Clinical diagnosis features (30 features)
    for i in [1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28]:
        feature_names.append(f'clinical_diagnosis___{i}')
    
    # Skin disease features
    feature_names.append('primary_skin_disease___1')
    
    # Demographic features
    feature_names.extend(['sex', 'ethnicity', 'race'])
    
    # Symptom features
    for i in range(1, 20):
        feature_names.append(f'symptoms___{i}')
    
    # Joint/arthritis features
    feature_names.extend([
        'inflammatory_arthropathy', 'joint_involvement_type', 'symmetric_polyarthritis',
        'joint_deformity', 'ra_diagnosis', 'joint_x_ray', 'joint_erosions'
    ])
    
    # Muscle features
    feature_names.extend([
        'muscle', 'weakness_upper_extremity', 'weakness_lower_extremity',
        'weakness_neck', 'muscle_onset_type', 'severity_muscle_wekness',
        'muscle_myalgia', 'muscle_tenderness', 'muscle_respiratory'
    ])
    
    # Respiratory method features
    for i in range(1, 6):
        feature_names.append(f'muscle_resp_method___{i}')
    
    # Dysphagia features
    feature_names.extend(['muscle_dysphagia', 'muscle_dysphagia_type'])
    
    # Dysphagia method features
    for i in range(1, 7):
        feature_names.append(f'muscle_dysphagia_method___{i}')
    
    # Additional muscle features
    feature_names.extend([
        'patient_dysphonia', 'muscle_enzyme', 'muscle_emg', 'ecg_other_myopathies',
        'emg_activity', 'musce_mri', 'mri_myopathies'
    ])
    
    # MRI findings
    for i in range(1, 6):
        feature_names.append(f'mri_findings___{i}')
    
    # MRI areas
    for i in [2, 3, 4, 5, 6]:
        feature_names.append(f'mri_areas_involved___{i}')
    
    # Biopsy features
    feature_names.extend([
        'muscle_biopsy', 'n_muscle_biopsies', 'muscle_biopsied',
        'perimysial_infiltrate', 'endomysial_infiltrate', 'endomysial_infiltrate_sur',
        'endomysial_infiltrate_no_necrotic', 'predominant_mononuclear',
        'predominant_t_cd4', 'predominant_t_cd8', 'predominant_b'
    ])
    
    # Muscle fiber features
    feature_names.extend([
        'muscle_fiber_atrophy_diffu', 'perifascicular_atrophy', 'perimysial_connective_tiss',
        'perifascicular_necrosis_de', 'scattered_endomysial_degen', 'mhc_1_perifascul',
        'mhc_1_muscle_fibers', 'mhc_1_most_muscle_fibers', 'mhc_2_perifascicular_fib',
        'mhc_2_muscle_fibers', 'mhc_2_most_muscle_fibers', 'mac_membrane_complex',
        'mac_membrane_complex_no_necrotic', 'decreased_density_of_endom',
        'tubuloreticular_inclusions', 'necrotic_muscle_fibers_as', 'ragged_red_fibers',
        'cytochrome_oxidase_negativ', 'scattered_cd68_macrophages', 'rimmed_vacuoles_in_non_nec'
    ])
    
    # Lung features
    feature_names.extend(['lung_involvement', 'nature_lung_involvment'])
    
    # Lung symptoms
    for i in range(1, 5):
        feature_names.append(f'lung_symptom___{i}')
    
    # PFT features
    feature_names.extend([
        'pft', 'first_pft_param_available', 'first_pft_pattern',
        'abnormal_pft_param_available', 'abnormal_pft_pattern'
    ])
    
    # HRCT features
    feature_names.extend(['hrct', 'findings_first_hrct'])
    
    # HRCT chest findings
    for i in range(1, 7):
        feature_names.append(f'first_hrct_chest___{i}')
    
    # HRCT patterns
    for i in range(1, 8):
        feature_names.append(f'first_hrct_patterns___{i}')
    
    # Abnormal HRCT
    feature_names.extend(['findings_abnormal_hrct'])
    
    # Abnormal HRCT findings
    for i in range(1, 7):
        feature_names.append(f'abnormal_hrct_findings___{i}')
    
    # HRCT chest findings
    for i in range(1, 8):
        feature_names.append(f'hrct_chest_findings___{i}')
    
    # Skin manifestations
    feature_names.extend([
        'skin_manifestations_1', 'mechanic_s_hands', 'hiker_s_feet', 'gottron_papules',
        'heliotrope_rash', 'v_sign', 'shawl_sign', 'malar_rash', 'calcinosis_skin',
        'scalp_rash', 'palmar_papules_skin', 'upper_thigh_rash_holster_s',
        'upper_arm_rash_sleeve_sign', 'peri_ungual_erythema', 'nailfold_capillaroscopy_al',
        'puffy_hands', 'skin_thickening_cutaneous', 'fingertip_digital_pits_or',
        'other_types_of_cutaneous_u', 'psoriasis', 'erythroderma', 'discoid_lupus',
        'panniculitis', 'purpura_or_petechiae', 'pyoderma_gangrenosum', 'alopecia',
        'any_other_rashes_skin_abno'
    ])
    
    # Raynaud and capillaroscopy
    feature_names.extend(['raynaud', 'raynaud_type'])
    
    for i in [1, 2, 3, 4, 9]:
        feature_names.append(f'capillaroscopy_lesion___{i}')
    
    # CTD symptoms
    feature_names.extend([
        'ctd_sympt_signs', 'ctd_dry_eyes', 'ctd_dry_mouth', 'ctd_fever',
        'ctd_weight_loss', 'ctd_schirmer', 'ctd_salivary_flow', 'ctd_salivary_bps',
        'ctd_sjogren'
    ])
    
    # Antibody features
    feature_names.extend([
        'ana_1', 'rf_1', 'anti_ccp_1', 'dsdna_1', 'sm_1', 'rnp_1', 'anca_mpo_1',
        'anca_pr3_1', 'ana_pattern', 'cytoplasmic_pattern_ana'
    ])
    
    # Specific antibodies
    feature_names.extend([
        'anti_ro52_ssa', 'anti_ro60_ssa', 'anti_ssa', 'anti_la_ssb1',
        'anti_ribonucleoprotein_rnp', 'anti_mi_2', 'anti_srp', 'anti_ku',
        'anti_jo_1', 'anti_pl7', 'anti_pl12', 'anti_oj', 'anti_ej', 'anti_ks',
        'anti_zo', 'anti_yrs_thy_ha', 'anti_pm_scl', 'anti_mda_5', 'anti_nxp2_or_mj',
        'anti_tif1_gamma', 'anti_hmgcr', 'anti_sae', 'anti_centromere_antibody_a',
        'anti_topoisomerase_1_anti', 'anti_rna_polymerase_iii_rn', 'anti_th_to'
    ])
    
    # Method test
    feature_names.append('method_test_myositis_2')
    
    # Pad with additional features if needed
    while len(feature_names) < n_features:
        feature_names.append(f'additional_feature_{len(feature_names)}')
    
    # Trim if too many
    feature_names = feature_names[:n_features]
    
    # Create DataFrame
    df = pd.DataFrame(X, columns=feature_names)
    
    # Add patient_id and target
    df.insert(0, 'patient_id', range(1, n_samples + 1))
    df.insert(1, 'target', y)
    
    # Convert features to appropriate data types and ranges
    for col in df.columns[2:]:  # Skip patient_id and target
        if 'clinical_diagnosis' in col or 'symptoms' in col:
            # Binary features (0, 1)
            df[col] = (df[col] > df[col].median()).astype(int)
        elif any(x in col for x in ['sex', 'ethnicity', 'race', 'pattern']):
            # Categorical features (1, 2, 3)
            df[col] = pd.cut(df[col], bins=3, labels=[1, 2, 3]).astype(int)
        elif 'anti_' in col or 'method_' in col:
            # Antibody tests (1.0, 2.0, 3.0)
            df[col] = pd.cut(df[col], bins=3, labels=[1.0, 2.0, 3.0]).astype(float)
        else:
            # Other features (0, 1, 2)
            df[col] = pd.cut(df[col], bins=3, labels=[0, 1, 2]).astype(int)
    
    # Introduce some missing values to make it realistic
    missing_mask = np.random.random(df.shape) < 0.1  # 10% missing
    for col in df.columns[2:]:  # Skip patient_id and target
        mask = missing_mask[:, df.columns.get_loc(col) - 2]
        df.loc[mask, col] = np.nan
    
    return df

def main():
    print("🔬 Generating synthetic clinical diagnosis dataset...")
    
    # Generate dataset
    df = generate_clinical_dataset()
    
    print(f"📊 Dataset generated:")
    print(f"   - Shape: {df.shape}")
    print(f"   - Target distribution:")
    print(f"     Syndrome (1): {(df['target'] == 1).sum()}")
    print(f"     Control (2): {(df['target'] == 2).sum()}")
    
    # Save to Excel
    output_path = "data/dataset.xlsx"
    df.to_excel(output_path, index=False)
    print(f"💾 Dataset saved to: {output_path}")
    
    # Show sample
    print("\n📋 Sample data:")
    print(df.head())
    
    print("\n✅ Dataset generation complete!")

if __name__ == "__main__":
    main()