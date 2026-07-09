import os
from src.data_cleaning import clean_and_translate_data
from src.analysis_utils import load_clean_data, calculate_demographics, calculate_contract_metrics, calculate_financial_insights

def main():
    print("=============================================")
    print("   HEALTHCARE WORKFLOW ANALYTICS PIPELINE    ")
    print("=============================================\n")
    
    # Define paths
    RAW_PATH = os.path.join("data", "raw", "healthcare_data.xlsx")
    PROCESSED_PATH = os.path.join("data", "processed", "healthcare_clean.csv")
    
    # 1. Trigger Data Pipeline (Phase 1)
    cleaned_df = clean_and_translate_data(RAW_PATH)
    if cleaned_df is not None:
        cleaned_df.to_csv(PROCESSED_PATH, index=False)
        print(f"✔ Phase 1 Complete: Clean data saved to {PROCESSED_PATH}\n")
    
    # 2. Trigger Analytics Engine (Phase 2)
    print("=== Running Phase 2: Statistical Extraction ===")
    df = load_clean_data(PROCESSED_PATH)
    
    demo = calculate_demographics(df)
    contracts = calculate_contract_metrics(df)
    financials = calculate_financial_insights(df)
    
    # 3. Print Results to Terminal
    print(f"\n[DEMOGRAPHICS]")
    print(f"• Total Active Staff: {demo['total_staff']}")
    print(f"• Average Age: {demo['average_age']:.1f} years old")
    print(f"• Average Experience (Tenure): {demo['average_tenure']:.1f} years")
    
    print(f"\n[CONTRACTS & HOURS]")
    print(f"• Total Budgeted Weekly Hours: {contracts['total_weekly_hours']} hrs")
    for c_type, count in contracts['contract_type_counts'].items():
        print(f"  - {c_type}: {count} staff members")
        
    print(f"\n[FINANCIAL PAYROLL BY LAW 19.378 CATEGORY]")
    for cat, data in financials.items():
        print(f"• Category {cat} | Average Base Salary: ${data['mean']:,.0f} | Total Allocation: ${data['sum']:,.0f}")

if __name__ == "__main__":
    main()
