# 📊 Student Performance Analysis

This project focuses on analyzing student academic data and predicting final grades using machine learning techniques.

---

## 🚀 Overview
The objective of this project is to understand how different factors such as study time and previous grades affect a student’s final performance.  
A Linear Regression model is used to predict the final grade (G3).

---

## 📂 Dataset
- 📌 Name: Student Performance Dataset  
- 📌 Source: UCI Machine Learning Repository  
- 📌 File Used: `student-mat.csv`  

### 📊 Key Features:
- `G1` – First period grade  
- `G2` – Second period grade  
- `G3` – Final grade (Target variable)  
- `studytime` – Weekly study time  
- `absences` – Number of absences  

---

## ⚙️ Steps Performed

### 🔹 Data Loading
- Loaded dataset using pandas  

### 🔹 Data Exploration
- Checked dataset structure (`head()`, `info()`)  
- Verified missing values  

### 🔹 Data Visualization
- Study time vs final grade  
- Grade distribution  
- Correlation heatmap  

### 🔹 Model Building
- Selected features: G1, G2, studytime  
- Applied Linear Regression  
- Split data into training and testing sets  

---

## 🤖 Machine Learning Model
- Model Used: Linear Regression  
- Goal: Predict final grade (G3)  
- Evaluation: Model accuracy using score  

---

## 📈 Results
- Previous grades (G1, G2) strongly influence final grade  
- Study time has a noticeable impact  
- Model provides good prediction accuracy  

---

## 🛠 Technologies Used
- Python 🐍  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  

---

## ▶️ How to Run
1. Open the notebook (`student_analysis.ipynb`)  
2. Ensure dataset file is in the same folder  
3. Run all cells step by step  

---

## 🎯 Learning Outcomes
- Data cleaning and preprocessing  
- Data visualization techniques  
- Understanding correlation  
- Basic machine learning implementation  

---

## 👨‍💻 Author
**Piyush Patane**