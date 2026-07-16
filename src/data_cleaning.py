import os
import pandas as pd

def clean_and_translate_data(file_path):
    print(f"=== Loading raw data from: {file_path} ===")
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        print(f"✔ Successfully loaded {df.shape[0]} rows.")
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return None

    # Clean raw column headers
    df.columns = df.columns.astype(str).str.strip()

    column_mapping = {
        'ID_RC': 'staff_id',
        'Tipo Contrato': 'contract_type',
        'Planta': 'staff_group',
        'Cod.Centro de Costo': 'cost_center_id',
        'Centro de Costo': 'cost_center_name',
        'Fec.Nacimiento': 'birth_date',
        'Fec.Ingreso': 'hire_date',
        'Sexo': 'gender',
        'Mes': 'payroll_month',
        'Ano': 'payroll_year',
        'Categoria': 'category',
        'Nivel': 'step_level',
        'Area': 'area',
        'Cod.Funcion': 'function_code',
        'Glosa Funcion': 'job_role',
        'Cargo Espec': 'specific_role',
        'Fec.Inicio Contrato': 'contract_start_date',
        'Fec.Termino Contrato': 'contract_end_date',
        'Horas Contrato': 'contract_hours',
        'H_003 SUELDO BASE SALUD': 'base_salary',
        'H_011 ASIG.ATENCION PRIMARIA': 'primary_care_allowance'
    }

    existing_cols = [col for col in column_mapping.keys() if col in df.columns]
    df_clean = df[existing_cols].rename(columns=column_mapping)

    print("=== Cleaning data types & strings ===")

    # String cleaning
    string_cols = ['contract_type', 'staff_group', 'cost_center_name', 'gender', 'category', 'area', 'job_role', 'specific_role']
    for col in string_cols:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].astype(str).str.strip().str.upper()

    # Financial conversion: Remove commas, cast to float, and double the base salary (as it is duplicated)
    financial_cols = ['base_salary', 'primary_care_allowance']
    for col in financial_cols:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].astype(str).str.replace(',', '', regex=False)
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce').fillna(0.0)
    
    # Apply the 2x gross baseline multiplier to base_salary
    if 'base_salary' in df_clean.columns:
        df_clean['base_salary'] = df_clean['base_salary'] * 2

    # Date parsing & age calculations
    if 'birth_date' in df_clean.columns:
        df_clean['birth_date'] = pd.to_datetime(df_clean['birth_date'], errors='coerce')
        df_clean['age'] = 2026 - df_clean['birth_date'].dt.year
        
    if 'hire_date' in df_clean.columns:
        df_clean['hire_date'] = pd.to_datetime(df_clean['hire_date'], errors='coerce')
        df_clean['tenure_years'] = 2026 - df_clean['hire_date'].dt.year

    return df_clean

if __name__ == "__main__":
    RAW_DATA_PATH = os.path.join("data", "raw", "healthcare_data.xlsx")
    PROCESSED_DATA_PATH = os.path.join("data", "processed", "healthcare_clean.csv")
    
    cleaned_df = clean_and_translate_data(RAW_DATA_PATH)
    
    if cleaned_df is not None:
        os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
        cleaned_df.to_csv(PROCESSED_DATA_PATH, index=False)
        print(f"✔ Cleaned dataset successfully saved to: {PROCESSED_DATA_PATH}")
