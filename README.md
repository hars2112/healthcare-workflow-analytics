## Project Progress Log

### Phase 1: Data Ingestion & Cleansing (Completed)
- **Status:** Done.
- **Data Privacy & Anonymization Precautions:**
  - Fully anonymized the dataset prior to processing to comply with data privacy standards.
  - Stripped out all compromise-prone personal identifying information (PII) such as full names, real national registry IDs (RUT), and email addresses.
  - Replaced sensitive fields with dummy/masked attributes (`staff_id`) to ensure absolute confidentiality.
- **Technical Actions Taken:**
  - Standardized 21 public health workforce columns from Spanish to English.
  - Stripped white spaces from text features to prevent syntax errors.
  - Parsed financial columns (`base_salary`, `primary_care_allowance`) from text strings into floats for analytical math.
  - Engineered two dynamic numerical variables: `age` and `tenure_years`.
  - Saved the structured, fully cleaned dataset to `data/processed/healthcare_clean.csv`.

## Expected Outcomes & Analytical Focus

This analysis is designed to answer critical organizational questions for the healthcare center's management team, focusing on four primary pillars:

### 1. Workforce Demographics
* **Age & Generational Distribution:** Identifying the average age of the staff and checking for upcoming retirement risks.
* **Gender Balance:** Evaluating representation across different organizational units.

### 2. Contractual & Workload Structure
* **Contract Type Splits:** Measuring the ratio of fixed-term contracts (`PLAZO FIJO`) vs. permanent tenure staff (`PLANTA`).
* **Resource Allocation:** Analyzing how weekly hours (`contract_hours`) are distributed across various center roles.

### 3. Salary & Compensation Framework
* **Payroll Optimization:** Mapping the distribution of the `base_salary` and `primary_care_allowance` across clinical categories (Categories A through F under Law 19.378).
* **Tenure vs. Pay:** Visualizing how operational costs scale alongside staff experience levels (`step_level` and `tenure_years`).

### 4. Operational Role Insights
* **Talent Density:** Identifying which specific job functions represent the highest personnel density and financial commitment within the clinic.

## 📈 Initial Analytical Key Findings

Based on the execution of the primary analytics pipeline, the following baseline organization metrics were extracted:

### 1. Workforce Demographics & Core Stability
* **Total Monitored Workforce:** 511 Active Professionals.
* **Average Staff Age:** 42.3 Years Old.
* **Average Institutional Tenure:** 10.5 Years of experience.

### 2. Contractual Breakdown & Resource Loading
* **Total Weekly Workforce Delivery:** 19,880 Contracted Hours/Week.
* **Contractual Stability Split:**
  - `INDEFINIDO` (Permanent Tenure): 276 Staff Members
  - `PLAZO FIJO` (Fixed Term): 179 Staff Members
  - `INDEFINIDO CT`: 41 Staff Members
  - `REEMPLAZO` (Substitutes/Replacements): 15 Staff Members

### 3. Financial Payroll Metrics (Base Salary by Law 19.378 Category)
* **Category A (Medics/Dentists/Pharmacists):** Avg: $1,082,984 | Gross Base Allocation: $126,709,134
* **Category B (Nurses and Other Health Professionals):** Avg: $1,001,882 | Gross Base Allocation: $128,240,909
* **Category C (Technicians):** Avg: $628,595 | Gross Base Allocation: $89,889,065
* **Category D (Technical Paramedical):** Avg: $606,611 | Gross Base Allocation: $6,066,110
* **Category E (Administrative Staff):** Avg: $559,903 | Gross Base Allocation: $33,034,269
* **Category F (Drivers/Service/Auxiliary Staff):** Avg: $489,399 | Gross Base Allocation: $6,362,188

### ⚠️ Deep Retirement Risk Profiles
A targeted breakdown of the 37 retirement-eligible members reveals distinct risk hotspots:

#### Risk Concentration by APS Category (Law 19.378)
* **Category C (Technicians):** 16 members (Highest volume risk)
* **Category B (Health Professionals):** 7 members (High financial/specialty risk)
* **Category F (Service/Drivers):** 5 members (Logistical infrastructure risk)
* **Category E (Paramedical Auxiliaries):** 4 members
* **Category A (Physicians/Dentists):** 3 members
* **Category D (Administrative Staff):** 1 member

#### Top Operational Impact Zones (Pending Vacancies)
1. **TECNICO DE ENFERMERIA (TENS):** 9 pending vacancies (Critical baseline care risk)
2. **ADMINISTRATIVO:** 5 pending vacancies
3. **AUXILIAR DE SERVICIOS:** 4 pending vacancies
4. **TECNICO DENTAL:** 4 pending vacancies
5. **MATRONA (Midwife):** 3 pending vacancies
