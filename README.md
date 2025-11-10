# homework_two

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

---
