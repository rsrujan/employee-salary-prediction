# 🧠 Employee Salary Prediction App

A machine learning project to predict employee salaries based on years of experience.  
Built with scikit-learn and deployed using Streamlit.

---

## 📌 Problem Statement

Organizations often face challenges in deciding fair salaries based on an employee’s experience.  
This project provides a machine learning-based solution to predict salary using historical data and regression algorithms.

---

## 📊 Features Used

- ✅ Years of Experience *(primary feature)*
- *(Extendable to include Gender, Education, Job Title, etc.)*

---

## 🛠️ Tech Stack

| Category        | Tools/Libraries                               |
|----------------|------------------------------------------------|
| Language        | Python 3.10                                   |
| ML Libraries    | scikit-learn, pandas, numpy                   |
| Visualization   | matplotlib, seaborn                           |
| Deployment      | Streamlit                                     |
| Serialization   | joblib                                        |

---

## 🚀 How it Works

1. **Preprocessing:**
   - Clean column names
   - Encode categorical features
   - Standardize numerical input

2. **Model Training:**
   - Linear Regression  
   - Decision Tree  
   - Random Forest (best accuracy ✅)

3. **Evaluation Metrics:**
   - R² Score, MAE, RMSE

4. **Deployment:**
   - Streamlit app for interactive predictions

---

## 📈 Model Performance

| Model              | R² Score | MAE (₹)   | RMSE (₹)   |
|-------------------|----------|-----------|------------|
| Linear Regression | 0.8991   | 12094.17  | 15551.04   |
| Decision Tree     | 0.8918   | 11751.76  | 16107.08   |
| **Random Forest** | **0.9008** | **11732.72** | **15418.67** |

---

## 💻 Streamlit App Demo

<p align="center">
  <img src="https://user-images.githubusercontent.com/your_screenshot_url" alt="Streamlit Screenshot" width="80%">
</p>

### ▶️ To Run Locally

```bash
# Step 1: Clone repo
git clone https://github.com/rsrujan/employee-salary-prediction
cd employee-salary-prediction

# Step 2: Create virtual env (optional but recommended)
python -m venv salaryenv
salaryenv\Scripts\activate  # or source salaryenv/bin/activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Launch Streamlit app
streamlit run app.py
