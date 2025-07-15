
# 📊🫀 Heart Attack Prediction

This Python project provides an efficient and clean solution to analyze datasets stored in CSV format using the `pandas` library. It is ideal for quick insights, data quality checks, and basic exploration tasks.

---

## 🧪 Script Features

The script performs foundational exploratory data analysis (EDA) using `pandas`, including:

- **Data Loading**: Reads the CSV into a pandas DataFrame.
- **Preview**: Displays the first few rows using `head()`.
- **Structure Overview**: Shows data types and memory usage via `info()`.
- **Missing Values Check**: Identifies columns with null entries.
- **Statistical Summary**: Uses `describe()` for numerical insights.

---

## 📦 Installation & Requirements

This project requires:

- Python 3.x
- pandas

To install dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install pandas
```

---

## 🚀 How to Run

Make sure `data.csv` is in the same directory as `main.py`.

To execute the analysis:

```bash
python main.py
```
---
## 🧾 Column Descriptions 

- `age`: Age of the patient
- `sex`: Sex (1 = male; 0 = female)
- `cp`: Chest pain type (0–3)
- `trestbps`: Resting blood pressure (mm Hg)
- `chol`: Serum cholesterol (mg/dl)
- `fbs`: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
- `restecg`: Resting electrocardiographic results (0–2)
- `thalach`: Maximum heart rate achieved
- `exang`: Exercise induced angina (1 = yes; 0 = no)
- `oldpeak`: ST depression induced by exercise
- `slope`: Slope of the peak exercise ST segment
- `ca`: Number of major vessels colored by fluoroscopy (0–3)
- `thal`: Thalassemia (3 = normal; 6 = fixed defect; 7 = reversible defect)
- `num`: Diagnosis of heart disease (0 = no disease, 1–4 = increasing severity)

---

## 📊 Sample Output

The script will print:

- Dataset information (column names, data types, and memory usage)
- A preview of the first few rows
- A summary of missing values per column
- Descriptive statistics (mean, min, max, standard deviation, etc.)

---

## 🧠 Future Work

- Data visualization using matplotlib/seaborn
- Advanced analysis (e.g., correlation heatmap, outlier detection)
- CLI argument support for input file flexibility

---

## 👤 Author

Developed by **Saud Aldalbahy**.
