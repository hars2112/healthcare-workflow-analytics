import pandas as pd

def load_clean_data(file_path):
    """Loads the processed CSV dataset."""
    return pd.read_csv(file_path)

def calculate_demographics(df):
    """Calculates basic workforce demographic metrics."""
    metrics = {
        'total_staff': int(df['staff_id'].nunique()),
        'average_age': float(df['age'].mean()),
        'average_tenure': float(df['tenure_years'].mean()),
        'gender_distribution': df['gender'].value_counts(normalize=True).to_dict()
    }
    return metrics

def calculate_contract_metrics(df):
    """Analyzes contract types and total workload allocation."""
    metrics = {
        'contract_type_counts': df['contract_type'].value_counts().to_dict(),
        'total_weekly_hours': float(df['contract_hours'].sum()),
        'average_hours_per_staff': float(df['contract_hours'].mean())
    }
    return metrics

def calculate_financial_insights(df):
    """Aggregates salary allocations by clinical category."""
    # Group by category and calculate total and mean base salary
    category_payroll = df.groupby('category')['base_salary'].agg(['sum', 'mean']).round(2)
    return category_payroll.to_dict(orient='index')

def calculate_retirement_risk(df):
    """
    Calculates deep metrics for staff at or past retirement age 
    (Women >= 60, Men >= 65), including risk concentration blocks.
    """
    is_female_retired = (df['gender'] == 'FEMENINO') & (df['age'] >= 60)
    is_male_retired = (df['gender'] == 'MASCULINO') & (df['age'] >= 65)
    
    retirement_df = df[is_female_retired | is_male_retired]
    total_eligible = len(retirement_df)
    
    if total_eligible > 0:
        avg_age = retirement_df['age'].mean()
        avg_salary = retirement_df['base_salary'].mean()
        pct_of_workforce = (total_eligible / len(df)) * 100
        
        # New Feature: Count distribution within the retirement pool
        category_breakdown = retirement_df['category'].value_counts().to_dict()
        role_breakdown = retirement_df['job_role'].value_counts().head(5).to_dict() # Top 5 critical roles
    else:
        avg_age = 0.0
        avg_salary = 0.0
        pct_of_workforce = 0.0
        category_breakdown = {}
        role_breakdown = {}
        
    metrics = {
        'total_eligible': total_eligible,
        'percentage_of_workforce': pct_of_workforce,
        'average_age': avg_age,
        'average_salary': avg_salary,
        'category_breakdown': category_breakdown,
        'role_breakdown': role_breakdown
    }
    return metrics
