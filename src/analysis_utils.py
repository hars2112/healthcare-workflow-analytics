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
