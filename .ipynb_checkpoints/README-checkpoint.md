mka # homework_two

# 🧾 Problem 1 — Text Processing (TF-IDF)

## 📍 Overview

This program (`tfidf.py`) performs **text preprocessing** and **TF-IDF computation** on a collection of documents listed in `tfidf_docs.txt`.  
It follows all steps described in the assignment specification.

### Part 1 – Preprocessing

For each document, the script:

1. **Cleans text**
   - Removes all non-word and non-whitespace characters.
   - Removes URLs starting with `http://` or `https://`.
   - Converts everything to lowercase.
   - Replaces multiple spaces with a single space.
2. **Removes stopwords** using the words listed in `stopwords.txt`.
3. **Applies stemming rules**
   - `ing → ""` (e.g., `running → run`)
   - `ly → ""` (e.g., `quickly → quick`)
   - `ment → ""` (e.g., `punishment → punish`)
4. **Outputs** the cleaned text to a new file named  
   `preproc_<original-filename>.txt`  
   (for example, `doc1.txt → preproc_doc1.txt`).

### Part 2 – TF-IDF Computation

After preprocessing:

1. **Term Frequency (TF)**  
   \[
   TF(t) = \frac{\text{count of t in doc}}{\text{total # of words in doc}}
   \]
2. **Inverse Document Frequency (IDF)**  
   \[
   IDF(t) = \log\!\left(\frac{N}{n_t}\right) + 1
   \]  
   where _N_ = total # of documents, _nₜ_ = # of documents containing term _t_.
3. **TF-IDF** = TF × IDF (rounded to 2 decimal places).
4. Selects **top 5 words** per document (sorted by descending TF-IDF, then alphabetically).
5. **Outputs** results to  
   `tfidf_<original-filename>.txt`.


# 📘 README — Problem 2: German Credit Dataset

This notebook (`german_credit.ipynb`) loads and processes the German Credit dataset and performs all required preprocessing, analysis, and visualization tasks.

---

## Preprocessing
- **Drop least-informative columns**  
  Removed the 3 columns with the highest number of `'none'` values.
- **Remove apostrophes**  
  Cleaned `'` characters from all string entries.
- **Recode checking_status**  
  Converted raw categories into: *No Checking, Low, Medium, High*.
- **Recode savings_status**  
  Converted raw categories into: *No Savings, Low, Medium, High*.
- **Convert class values**  
  `'good' → 1`, `'bad' → 0`.
- **Recode employment**  
  Mapped ranges into: *Unemployed, Amateur, Professional, Experienced, Expert*.

---

## Analysis
- **Foreign worker vs class**  
  Crosstab showing counts of good/bad credit for foreign vs non-foreign workers.
- **Employment vs savings_status**  
  Crosstab showing distribution across employment and savings categories.
- **Average credit amount**  
  Computed mean credit amount for *male single* customers with *Experienced* employment.
- **Average credit duration by job**  
  Grouped job types and calculated mean duration.
- **Most common checking/savings for education**  
  Printed the most frequent checking_status and savings_status for customers with purpose `'education'`.

---

## Visualizations
- **Two bar-chart subplots**  
  Counts of personal_status grouped by savings_status and checking_status.
- **Bar graph (credit_amount > 4000)**  
  Plotted property_magnitude vs average age.
- **Three pie charts**  
  For customers with **High** savings_status and **age > 40**, displayed distributions of:
  - personal_status  
  - credit_history  
  - job  

---

## How to Run
1. Open `german_credit.ipynb` in JupyterHub or JupyterLab.
2. Ensure `GermanCredit.csv` is in the same directory.
3. Run all cells in order using **Restart & Run All**.
4. All outputs (tables, plots) will appear inline.



---
