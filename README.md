# ❤️ Heart Disease Prediction Using Machine Learning

## CodeAlpha Machine Learning Internship

### 📌 Project Overview

Heart Disease Prediction is a machine learning project developed to predict the likelihood of heart disease based on a patient's medical information. Early prediction of heart disease can help healthcare professionals take preventive measures and provide timely treatment.

This project uses machine learning algorithms to analyze patient health parameters and classify whether a person is at risk of heart disease.

---

## 🎯 Objective

The objective of this project is to build an accurate machine learning model that can predict the presence of heart disease using patient medical data.

---

## 📊 Dataset Information

The dataset contains 918 patient records and 12 attributes.

### Features

- Age
- Sex
- ChestPainType
- RestingBP
- Cholesterol
- FastingBS
- RestingECG
- MaxHR
- ExerciseAngina
- Oldpeak
- ST_Slope

### Target Variable

- **HeartDisease**
  - 0 → No Heart Disease
  - 1 → Heart Disease Present

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

---

## 🔍 Machine Learning Workflow

### 1. Data Preprocessing
- Data inspection
- Categorical variable encoding
- Feature selection
- Data preparation for model training

### 2. Exploratory Data Analysis (EDA)
- Heart Disease Distribution
- Gender Distribution
- Chest Pain Type Analysis
- Age Distribution
- Correlation Matrix

### 3. Model Training

The following machine learning models were implemented:

#### Logistic Regression
Used as a baseline classification algorithm for disease prediction.

#### Random Forest Classifier
An ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

---

## 📈 Model Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix

---

## 🏆 Results

| Model | Accuracy |
|---------|---------|
| Logistic Regression | 84.24% |
| Random Forest | 88.04% |

### Final Model Performance

- Accuracy: **88.04%**
- Precision: **89.72%**
- Recall: **89.72%**
- F1 Score: **89.72%**
- ROC-AUC Score: **94.30%**

The Random Forest Classifier achieved the highest performance and was selected as the final model.

---

## 🌐 Streamlit Web Application

A user-friendly Streamlit web application was developed to allow users to enter medical information and predict the risk of heart disease in real time.

### Application Features

- Interactive user interface
- Real-time disease prediction
- Professional healthcare-themed design
- Easy to use and deploy

---

## 📂 Project Structure

```text
CodeAlpha_DiseasePrediction/
│
├── heart.csv
│
├── Disease_Prediction.ipynb
├── disease_model.pkl
├── app.py
├── requirements.txt
├── README.md
```

---

## 🚀 How to Run the Project

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run Jupyter Notebook

```bash
jupyter notebook
```

### Launch Streamlit Application

```bash
streamlit run app.py
```

---

## 📌 Conclusion

This project demonstrates how machine learning can be applied in the healthcare sector to assist in disease prediction and risk assessment.

The Random Forest Classifier achieved excellent performance with an accuracy of 88.04% and a ROC-AUC score of 94.30%, making it an effective model for predicting heart disease risk based on patient medical data.

---

## 👩‍💻 Author

**Dishmitha**
