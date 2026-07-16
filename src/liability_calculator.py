import pandas as pd

class RetirementLiabilityCalculator:
    def __init__(self, months_per_year=1, max_months_cap=11, annual_growth_rate=0.054):
        """
        Calculates retirement severance liabilities.
        - months_per_year: Number of months of salary paid per year of service (Standard: 1).
        - max_months_cap: Maximum capped months of salary (Standard: 11).
        - annual_growth_rate: Compound annual salary growth (5.4%).
        """
        self.months_per_year = months_per_year
        self.max_months_cap = max_months_cap
        self.annual_growth_rate = annual_growth_rate

    def calculate_individual_liability(self, current_salary, tenure_years, years_in_future=0):
        """
        Calculates the projected severance payout for an individual worker.
        Formula: Projected Salary * Min(Tenure * months_per_year, max_months_cap)
        """
        # Compound salary into the future
        projected_salary = current_salary * ((1 + self.annual_growth_rate) ** years_in_future)
        
        # Future tenure
        projected_tenure = tenure_years + years_in_future
        
        # Calculate severance months earned
        months_deserved = projected_tenure * self.months_per_year
        capped_months = min(months_deserved, self.max_months_cap)
        
        # Total liability for this individual
        return projected_salary * capped_months

    def calculate_portfolio_liability(self, df):
        """
        Evaluates the cumulative liability for Year 0, Year 5, and Year 10 pools.
        """
        timeline_results = {}
        
        for years_forward in [0, 5, 10]:
            future_age = df['age'] + years_forward
            
            # Isolate retirement eligible staff at this future timeline
            is_female_retired = (df['gender'] == 'FEMENINO') & (future_age >= 60)
            is_male_retired = (df['gender'] == 'MASCULINO') & (future_age >= 65)
            
            retired_df = df[is_female_retired | is_male_retired]
            
            total_liability = 0.0
            individual_payouts = []
            
            for _, row in retired_df.iterrows():
                payout = self.calculate_individual_liability(
                    current_salary=row['base_salary'],
                    tenure_years=row['tenure_years'],
                    years_in_future=years_forward
                )
                total_liability += payout
                individual_payouts.append(payout)
                
            timeline_results[years_forward] = {
                'eligible_count': len(retired_df),
                'total_liability_clp': total_liability,
                'average_payout_clp': total_liability / len(retired_df) if len(retired_df) > 0 else 0.0
            }
            
        return timeline_results
