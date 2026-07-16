import os
from src.data_cleaning import clean_and_translate_data
from src.analysis_utils import (
    load_clean_data, 
    calculate_demographics, 
    calculate_contract_metrics, 
    calculate_financial_insights,
    calculate_retirement_risk,
    calculate_retirement_projections
)
# Import the new Liability Calculator
from src.liability_calculator import RetirementLiabilityCalculator

def main():
    print("=============================================")
    print("   HEALTHCARE WORKFLOW ANALYTICS PIPELINE    ")
    print("=============================================\n")
    
    RAW_PATH = os.path.join("data", "raw", "healthcare_data.xlsx")
    PROCESSED_PATH = os.path.join("data", "processed", "healthcare_clean.csv")
    
    cleaned_df = clean_and_translate_data(RAW_PATH)
    if cleaned_df is not None:
        cleaned_df.to_csv(PROCESSED_PATH, index=False)
        print(f"✔ Phase 1 Complete: Clean data saved to {PROCESSED_PATH}\n")
    
    print("=== Running Phase 2: Statistical Extraction ===")
    df = load_clean_data(PROCESSED_PATH)
    
    demo = calculate_demographics(df)
    contracts = calculate_contract_metrics(df)
    financials = calculate_financial_insights(df)
    retirement = calculate_retirement_risk(df)
    projections = calculate_retirement_projections(df)

    # Initialize and run the Liability Calculator
    calculator = RetirementLiabilityCalculator()
    liabilities = calculator.calculate_portfolio_liability(df)

    # Print Demographics
    print(f"\n[DEMOGRAPHICS]")
    print(f"• Total Active Staff: {demo['total_staff']}")
    print(f"• Average Age: {demo['average_age']:.1f} years old")
    print(f"• Average Experience (Tenure): {demo['average_tenure']:.1f} years")
    
    # Current Retirement Risk (Year 0)
    print(f"\n[⚠️ CURRENT RETIREMENT RISK (YEAR 0)]")
    print(f"• Staff At/Past Retirement Age: {retirement['total_eligible']} members ({retirement['percentage_of_workforce']:.1f}% of workforce)")
    if retirement['total_eligible'] > 0:
        print(f"  - Average Age of Retiring Staff: {retirement['average_age']:.1f} years old")
        print(f"  - Average Base Salary: {retirement['average_salary']:,.0f} CLP")
        print(f"  - Estimated Severance Liability (Year 0): {liabilities[0]['total_liability_clp']:,.0f} CLP")
        print(f"  - Average Individual Payout: {liabilities[0]['average_payout_clp']:,.0f} CLP")

    # 5 & 10 Year Forecasts & Liabilities
    print(f"\n[🔮 FUTURE RETIREMENT & FINANCIAL LIABILITIES]")
    for years, data in projections.items():
        print(f"• In {years} Years:")
        print(f"  - Cumulative Eligible Staff: {data['total_eligible']} members ({data['percentage_of_workforce']:.1f}% of total workforce)")
        print(f"  - Estimated Cumulative Severance Liability: {liabilities[years]['total_liability_clp']:,.0f} CLP")
        print(f"  - Average Individual Payout: {liabilities[years]['average_payout_clp']:,.0f} CLP")

    # Contracts
    print(f"\n[CONTRACTS & HOURS]")
    print(f"• Total Budgeted Weekly Hours: {contracts['total_weekly_hours']} hrs")
    for c_type, count in contracts['contract_type_counts'].items():
        print(f"  - {c_type}: {count} staff members")
        
    # Financials
    print(f"\n[FINANCIAL PAYROLL BY LAW 19.378 CATEGORY]")
    for cat, data in financials.items():
        print(f"• Category {cat} | Average Base Salary: {data['mean']:,.0f} CLP | Total Allocation: {data['sum']:,.0f} CLP")

if __name__ == "__main__":
    main()
