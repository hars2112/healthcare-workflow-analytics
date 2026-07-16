# 🏥 CareForce Horizon
## A Predictive Analytics Pipeline & Financial Liability Model for Public Healthcare Workforce Volatility under Law 19.378

An enterprise-grade, modular data engineering and predictive analytics pipeline built to ingest, clean, and forecast workforce transition dynamics and financial liabilities under the Chilean Primary Care Statute (**Law 19.378**). 

This system processes clinical staff data to identify immediate operational risks and projects cumulative staffing gaps and retirement liabilities 5 and 10 years into the future, assuming an annual compounding salary growth rate of **5.4%**.

---

## 🏗️ System Architecture & Data Flow

The pipeline is designed with a professional, modular structure split into three distinct phases:

1. **Phase 1: Ingestion & Data Sanitation (`src/data_cleaning.py`)**
   - Automatically sanitizes and maps localized Spanish fields to standard database schemas.
   - Converts financial values into clean numeric floats, resolving text format anomalies.
   - Programmatically calculates exact employee `age` and institutional `tenure_years` based on date parameters.
   - Doubles the raw base salary column to represent the **true gross monthly baseline earnings** (accounting for duplicate payroll structures).
   
2. **Phase 2: Predictive Analytical Engine (`src/analysis_utils.py` & `src/liability_calculator.py`)**
   - **Demographic Baselines:** Extracts workforce age averages, stability markers, and tenure indicators.
   - **Gender-Aligned Retirement Modeling:** Evaluates retirement eligibility mapped directly to Chilean standard legal thresholds (Women $\ge$ 60, Men $\ge$ 65).
   - **Decade-Out Compound Forecasting:** Projects workforce age shifts and compounded salary growth ($S_t = S_0 \times (1 + 0.054)^t$) over 5 and 10-year horizons.
   - **Deterministic Liability Calculator:** Projects total severance liabilities capped at a maximum of 11 months of gross salary (1 month per year of service).

3. **Phase 3: Pipeline Orchestration (`main.py`)**
   - Serves as the central pipeline controller, sequentially running the ETL cleaning process, running statistical calculations, and generating executive console reports in **CLP**.

---

## 📊 Key Executive Findings & Forecasts

Executing the master pipeline against the workforce dataset of **511 active professionals** yielded the following strategic insights:

### 1. Demographic & Stability Baseline
* **Total Active Workforce:** 511 Employees
* **Average Age:** 42.3 Years Old
* **Average Experience (Tenure):** 10.5 Years
* **Workforce Hours Load:** 19,880 Weekly Hours Contracted

### 2. Fiscal Liability & Retirement Forecast Timeline (CLP)

| Timeline | Eligible Staff Count | % of Total Workforce | Estimated Cumulative Liability (CLP) | Average Individual Payout (CLP) |
| :--- | :---: | :---: | :---: | :---: |
| **Year 0 (Today)** | 37 members | 7.2% | **705,657,844 CLP** | 19,071,834 CLP |
| **Year 5 (Future)** | 76 members | 14.9% | **1,978,531,578 CLP** | 26,033,310 CLP |
| **Year 10 (Future)** | 126 members | 24.7% | **4,313,433,983 CLP** | 34,233,603 CLP |

### 3. Immediate Operational Vulnerability Hotspots (Year 0)
The pipeline isolates **Category C** (Nursing Technicians - TENS) and **Category B** (Midwives, Nurses) as the highest risk sectors for upcoming vacancies:
* **Category C (Technicians):** 16 members currently eligible (Led by **TÉCNICO DE ENFERMERÍA** with 9 vacancies pending).
* **Category B (Health Professionals):** 7 members currently eligible (Led by **MATRONA** with 3 vacancies pending).

---

## 🏛️ Strategic Decisions Assisted by This Pipeline

This pipeline serves as a decision-making framework for a CESFAM Director to execute:
1. **Targeted Succession Planning:** Initiate proactive recruiting for the 9 pending TENS vacancies to prevent operational care bottlenecks.
2. **Financial Reserves Provisioning:** Leverage the 10-year liability forecast to request regional budget allocations (*Incentivo al Retiro*) early, mitigating the impending **4.3 Billion CLP** liability.
3. **Logistics Risk Management:** Identify vehicle operators (Category F) approaching retirement to preserve critical community outreach programs.
