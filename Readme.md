# <span style='color:purple'> <img style='height:50px; width:50px' src="heart.png" alt=""> Heart Disease Prediction Project <img style='height:50px; width:50px' src="heart.png" alt=""> 

### <span style='color:lightgreen'> 📘 Overview

<span style='color:lightblue'> A heart disease prediction model is a machine learning system designed to predict the likelihood of a person developing heart disease based on various factors like age, blood pressure, cholesterol, and medical history. These models use algorithms trained on datasets of patient records to identify patterns and predict the risk of heart disease. They help in early detection and risk stratification, allowing for timely interventions and potentially improving patient outcomes. 

### <span style='color:lightgreen'> 🎯 Objective

<span style='color:lightblue'> To build a machine learning model that predicts the person have heart disease or not based on features such as:

<span style='color:lightblue'> Age

<span style='color:lightblue'> Chest Pain

<span style='color:lightblue'> Cholestrol

<span style='color:lightblue'> Slope

<span style='color:lightblue'> Oldpeak

<span style='color:lightblue'> Trestbps

### <span style='color:lightgreen'> 🧩 Dataset

 <span style='color:yellow'> Source:<span style='color:lightblue'>  (e.g., Kaggle – Heart Disease Prediction Dataset)

 <span style='color:yellow'> Size:<span style='color:lightblue'>  [Number of rows and columns, e.g., 1025 rows × 14 columns]

 <span style='color:yellow'> Target Variable:<span style='color:lightblue'>  Target (1 = Heart Disease Detected, 0 = Heart Disease Not Detected)

 #### <span style='color:lightgreen'> Key Features:
</span>
<span style='color:yellow'>
<li>Age  -->  <span style='color:lightblue'>  Provide the age of the patient
<li>  cp --> <span style='color:lightblue'>  0, 1, 2 and 3
<li>  trestbps --><span style='color:lightblue'>  Resting Blood Pressure
<li>  chol --> <span style='color:lightblue'>  Serum Cholestoral (in mg/dl)
<li>  thalach --> <span style='color:lightblue'>  Maximum Heart Rate Achieved
<li>  exang --><span style='color:lightblue'>  Exercise Induced Angina
<li>  oldpeak --> <span style='color:lightblue'> ST depression induced by exercise relative to rest
<li>  slope --><span style='color:lightblue'>  slope of the peak exercise ST segment
<li>  ca --><span style='color:lightblue'>  Number of major Vessels (0-3) colored by flourosopy
</span>

### <span style='color:lightgreen'> ⚙️ Technologies Used

 <span style='color:yellow'> Programming Language:  <span style='color:lightblue'>  Python

 <span style='color:lightgreen'> Libraries:

 <span style='color:yellow'> pandas, numpy –  <span style='color:lightblue'>  Data preprocessing

 <span style='color:yellow'> matplotlib, seaborn –  <span style='color:lightblue'> Data visualization

 <span style='color:yellow'> scikit-learn –  <span style='color:lightblue'>Model building and evaluation

 <span style='color:yellow'> pickle  –  <span style='color:lightblue'>Model saving

### <span style='color:lightgreen'> 🧠 Machine Learning Models Used

 <span style='color:lightblue'>Logistic Regression

 <span style='color:lightblue'>K Neighbor Classifier

 <span style='color:lightblue'>Random Forest Classifier

 <span style='color:lightblue'>Support Vector Machine (SVM)

 <span style='color:yellow'>Model Evaluation Metrics:

 <span style='color:lightblue'>Accuracy

 ### <span style='color:lightgreen'> 🚀 Project Workflow

<span style='color:yellow'> Data Collection –<span style='color:lightblue'> Load and inspect dataset

<span style='color:yellow'> Data Cleaning – <span style='color:lightblue'> Handle missing values, encode categorical variables

<span style='color:yellow'> Exploratory Data Analysis (EDA) –<span style='color:lightblue'>  Understand relationships between variables

<span style='color:yellow'> Feature Engineering – <span style='color:lightblue'> Scale/transform variables

<span style='color:yellow'> Model Training – <span style='color:lightblue'> Train multiple ML algorithms

<span style='color:yellow'> Model Evaluation – <span style='color:lightblue'> Compare model performance

<span style='color:yellow'> Prediction –<span style='color:lightblue'>  Use best model for Heart Disease prediction

<span style='color:yellow'> Deployment – <span style='color:lightblue'> Streamlit web app for user interaction