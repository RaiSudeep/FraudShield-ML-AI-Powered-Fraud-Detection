![ FraudShield-ML](https://github.com/user-attachments/assets/b42c216b-0099-4c98-9d89-881496334408)

# 🚀 FraudShield-ML: AI-Powered Fraud Detection 
FraudShield-ML is an AI-powered fraud detection system that analyses financial transactions using machine learning, providing real-time fraud risk assessment via predictive modelling and a Streamlit dashboard.

## 📌 Table of Contents  
- [Dataset Overview](#📌-dataset-overview)  
- [Dataset Source](#🗂-dataset-source)   
- [Key Objectives](#🎯-key-objectives)  
- [Technology Stack](#🛠-technology-stack)   
- [Exploratory Data Analysis (EDA)](#📊-exploratory-data-analysis-eda)  
- [User Insights](#📊-user-insights)  
- [Fraud Distribution & Correlation Analysis](#🔎-fraud-distribution--correlation-analysis)  
- [Machine Learning Model](#⚙️-machine-learning-model)  
- [Streamlit Dashboard](#🖥️-streamlit-dashboard-fraudshield)  
- [How to Use](#🔎-how-to-use)  
- [Contact](#📬-contact)  
- [Final Thoughts](#🚀-final-thoughts)

## 📌 Dataset Overview  
This dataset presents a **synthetic representation of mobile money transactions**, designed to replicate real-world financial behaviors while incorporating fraudulent patterns for research purposes.  

## 🗂 Dataset Source  
The dataset used in this project comes from **Kaggle's Financial Fraud Detection Dataset**:  
🔗 [Financial Fraud Detection Dataset](https://www.kaggle.com/datasets/sriharshaeedala/financial-fraud-detection-dataset)  

### 🗂 Google Drive Access  
The dataset used in this project is hosted on Google Drive due to file size limitations on GitHub.  

🔗 [Download Fraud Detection Dataset](https://drive.google.com/drive/folders/1EGWfy0c0_-gv2hdq2ZWMuGXbYDggzXtd?usp=drive_link) 

### 📊 Dataset Structure  
| Column          | Description |
|----------------|------------|
| `step`        | Time unit (1 step = 1 hour), covering **744 steps** (30 days). |
| `type`        | Transaction type (**CASH-IN, CASH-OUT, DEBIT, PAYMENT, TRANSFER**). |
| `amount`      | Transaction amount in local currency. |
| `nameOrig`    | Customer initiating the transaction. |
| `oldbalanceOrg` | Initial sender's balance before transaction (**not useful for fraud detection**). |
| `newbalanceOrig` | Sender's balance after transaction (**not useful for fraud detection**). |
| `nameDest`    | Recipient of the transaction. |
| `oldbalanceDest` | Initial recipient's balance (**not applicable for merchants**). |
| `newbalanceDest` | Recipient's balance after transaction (**not applicable for merchants**). |
| `isFraud`     | **Identifies fraudulent transactions** targeting customer accounts. |
| `isFlaggedFraud` | Flags unauthorised transactions exceeding **200,000 currency units**. |

## 🎯 Key Objectives  
- **Transaction Monitoring** – Analyse transaction patterns for fraud detection.  
- **Predictive Modelling** – Use ML models to classify fraudulent transactions.  
- **Interactive Dashboard** – Develop a **Streamlit app** for real-time fraud assessment.  
- **Feature Engineering** – Enhance fraud detection accuracy through data processing.  

## 🛠 Technology Stack  
FraudShield-ML leverages **modern data science and machine learning tools** to enhance fraud detection accuracy.  

### 🔹 **Programming Languages & Frameworks**  
- **Python** – Core programming language for ML model development.  
- **Streamlit** – Interactive web framework for real-time fraud detection dashboard.  
- **Jupyter Notebook** – Used for **EDA, data visualisation, and model training**.  

### 🔹 **Machine Learning & Data Science**  
- **Scikit-Learn** – Model training (Logistic Regression, SVM, Random Forest).  
- **Pandas & NumPy** – Data manipulation and preprocessing.  
- **Matplotlib & Seaborn** – Fraud trend visualisation.  
- **Joblib** – Model serialisation for efficient fraud prediction.  

### 🔹 **Deployment & Integration**  
- **GitHub** – Code versioning and repository management.   

### ⚡ **Why These Technologies?**  
FraudShield-ML is **optimised for financial fraud detection**, using a combination of **ML algorithms, real-time dashboards, and scalable deployment tools**.   

## 📊 Exploratory Data Analysis (EDA)  
This project investigates various transaction behaviors to detect fraud patterns:  
- 📌 **Transaction Type Analysis** – Understanding **PAYMENT, TRANSFER, and CASH_OUT** behaviours.  
- 📌 **Fraud Rate by Type** – Identifying transaction types with **higher fraud risk**.  
- 📌 **Amount Distribution Trends** – Analysing transaction values for anomalies.  
- 📌 **Balance Behaviour** – Examining pre/post transaction balances for irregularities.  
- 📌 **Fraud vs Transaction Amount Relationship** – Analysing transaction values to determine if larger amounts correlate with fraudulent behaviour.  
- 📌 **Fraud Trends Over Time** – Detecting fraud occurrence per step intervals.  

## 📊 User Insights    
- 📌 **Top 10 Most Active Senders** - Users with the highest number of outgoing transactions, potentially large financial movers.  
- 📌 **Top 10 Most Active Receivers** - Accounts receiving frequent transactions, which may indicate high transaction volume entities.  
- 📌 **Top 10 Fraudulent Users** - Senders associated with multiple fraudulent transactions, potentially linked to fraud rings.  

## 🔎 Fraud Distribution & Correlation Analysis  
- 📌 **Fraud Distribution in Transaction Types** - Fraudulent transactions are concentrated in **TRANSFER and CASH_OUT**, suggesting that these payment types are more vulnerable to fraudulent activities.  
- 📌 **Correlation Analysis** - A heatmap analysis reveals strong correlations between transaction **amount, balance changes, and fraud occurrence**:  

## ⚙️ Machine Learning Model  
The fraud detection model is trained using **Logistic Regression**, incorporating:  
- **Feature Scaling** – Standardised transaction attributes.  
- **One-Hot Encoding** – Categorical variable processing (transaction type).  
- **Class Weight Balancing** – Handling fraud-class imbalance.  

### 🏆 Model Performance  
- **Classification Report** – Precision, recall, F1-score evaluation.  
- **Confusion Matrix** – Fraud detection accuracy breakdown.  
- **Fraud Probability Score** – Real-time risk assessment.  

## 🖥️ Streamlit Dashboard (`FraudShield`)  
FraudShield provides an **interactive, AI-driven fraud detection experience**, allowing users to:  
- 🔹 **Enter transaction details** for assessment.  
- 🔹 **View fraud probability scores** (real-time prediction).  
- 🔹 **Understand feature importance** behind fraud detection.  
- 🔹 **Analyse high-risk transactions** before approval.  

### 📌 Dashboard Screenshot  
![FraudShield Dashboard](https://github.com/user-attachments/assets/b5fab9d4-6b17-4d68-917e-7b89f35fcb96)  

## 🔎 How to Use  
### 1️⃣ **Install Dependencies**  
```bash
pip install -r requirements.txt
```
### 2️⃣ **Review & Run Jupyter Notebook**  
To explore **EDA, feature engineering, and model training**, open and execute the notebook:  
```bash
jupyter notebook fraud_detection_analysis_model.ipynb
```
### 3️⃣ **Run Streamlit App**  
```bash
streamlit run app.py
```
### 4️⃣ **Use the Dashboard**  
- Enter transaction details.  
- Click **'Predict Fraud Risk'**.  
- Get an instant fraud assessment.

## 📬 Contact  
For questions, contributions, or collaboration:  
📧 **Email**: [sudeeprai969@gmail.com](mailto:sudeeprai969@gmail.com)  
🔗 **LinkedIn**: [Sudeep Rai](https://www.linkedin.com/in/sudeep-rai/)  

## 🚀 Final Thoughts  
FraudShield provides **intelligent fraud detection** using ML models and interactive dashboards.  
Feel free to **open an issue or contribute** to enhance fraud detection capabilities! 🔍💡  
