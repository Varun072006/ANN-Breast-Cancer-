# 🧠 Breast Cancer Prediction using Artificial Neural Network (ANN)

## 📌 Introduction
Breast cancer is one of the most common and life-threatening diseases affecting millions of people worldwide.  
Early and accurate detection of breast cancer can significantly improve treatment outcomes and survival rates.  

This project focuses on building an **Artificial Neural Network (ANN)** using the Breast Cancer Wisconsin dataset to predict whether a tumor is **Benign (non-cancerous)** or **Malignant (cancerous)**.  
The trained model is deployed through a simple Flask web application with a clear HTML interface for real-time predictions.

---

## 📖 Detailed Description

### 🔹 Dataset
- **Name**: Breast Cancer Wisconsin (Diagnostic) Dataset  
- **Features**: 30 diagnostic attributes such as mean radius, mean texture, smoothness, compactness, concavity, etc.  
- **Target Classes**:  
  - `0` → Benign (Non-Cancerous)  
  - `1` → Malignant (Cancerous)  

---

### 🔹 Workflow
1. **Data Preprocessing**
   - Cleaned the dataset and handled missing values.  
   - Scaled features using `StandardScaler` to ensure ANN convergence.  

2. **Exploratory Data Analysis (EDA)**
   - Plotted distributions of key features.  
   - Checked correlation between variables.  
   - Identified imbalance in classes.  

3. **Feature Engineering**
   - Selected and refined important features based on correlation analysis.  
   - Applied **SMOTE (Synthetic Minority Oversampling Technique)** to handle class imbalance.  

4. **Artificial Neural Network (ANN) Model**
   - Implemented using **`MLPClassifier`** from `scikit-learn`.  
   - Architecture tuned with multiple hidden layers and ReLU activation.  
   - Optimization performed with `adam` solver for efficiency.  

5. **Evaluation**
   - Metrics: Accuracy, Precision, Recall, F1-Score, and ROC-AUC.  
   - The model achieved strong performance, showing capability for medical decision support.  

6. **Deployment**
   - Trained model exported with `joblib`.  
   - Integrated into a Flask web app (`app.py`).  
   - User interface (`index.html`) allows doctors/researchers to input feature values and receive predictions instantly.  

---

## 🎯 Conclusion
This project demonstrates the **end-to-end lifecycle of a Machine Learning system** applied in healthcare:  
- **Data Understanding → Preprocessing → Modeling → Evaluation → Deployment**  

The Artificial Neural Network provides high accuracy in predicting breast cancer diagnosis, serving as a valuable **decision-support tool** for medical professionals.  
Although not a replacement for clinical expertise, such AI-driven systems can **assist in early detection, reduce diagnostic errors, and enhance patient outcomes**.  

This work highlights the power of combining **Machine Learning and Web Deployment** to transform raw medical data into actionable insights that can positively impact healthcare services.  