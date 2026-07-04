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
