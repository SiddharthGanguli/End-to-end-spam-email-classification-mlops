# End-to-End Spam Email Classification (MLOps)

##  Problem Statement

Spam emails are unwanted messages that often contain advertisements, scams, or harmful links. These emails waste time, reduce productivity, and can create security risks for users and businesses.

---

##  Business Value

This project helps to:

-  Reduce unwanted emails  
- Improve email security  
- Save user time and productivity  
- Automatically filter harmful or phishing messages  

---

##  Project Overview

This project builds an **end-to-end machine learning pipeline** that classifies email messages as **Spam** or **Ham (Not Spam)** using **MLOps practices**.

The system covers the **full ML lifecycle**, including:

- Data processing
- Model training
- Experiment tracking
- Version control
- Model deployment

---

## How This Project Was Built

### 1️ Data Ingestion
- Loaded raw email dataset  
- Stored and managed dataset inside project structure  
- Used pipeline-based automation  

---

### 2️ Data Preprocessing
- Cleaned email text  
- Removed special characters and noise  
- Converted text into machine learning features using vectorization techniques  

---

### 3️ Model Training
- Used **Scikit-learn classification algorithms**  
- Tuned model parameters using configuration files  
- Trained model using processed dataset  

---

### 4️ Model Evaluation

Model performance was evaluated using classification metrics:

| Metric | Score |
|----------|------------|
| Accuracy | 98.02% |
| Precision | 97.05% |
| Recall | 88.00% |
| F1 Score | 92.30% |

These results show that the model performs strongly while keeping false predictions low.

---

### 5️ Experiment Tracking

Used **MLflow** to track:

- Training runs  
- Model parameters  
- Evaluation metrics  
- Model versioning  

---

### 6️ Data Version Control

Used **DVC** to:

- Track dataset versions  
- Maintain reproducibility  
- Manage ML pipeline stages  

---

## Tech Stack

- Python  
- Scikit-learn  
- Pandas  
- NumPy  
- MLflow  
- DVC  
- Streamlit / Flask  

---

##  Project Structure
```
End-to-end-spam-email-classification-mlops
│
├── artifacts/ # Saved models
├── config/ # Configuration files
├── data/ # Dataset
├── mlruns/ # MLflow experiments
├── src/ # ML pipeline code
│
├── app.py # Web application
├── main.py # Training pipeline
├── params.yaml # Model parameters
├── requirements.txt # Dependencies
├── setup.py # Package setup
```



---

##  Running the Project

### 1. Clone Repository

```bash
git clone https://github.com/SiddharthGanguli/End-to-end-spam-email-classification-mlops
cd End-to-end-spam-email-classification-mlops
```
2. Create Virtual Environment
```bash
python -m venv venv
```

Activate Environment
Windows

```bash
venv\Scripts\activate
```

Linux / Mac
```bash
source venv/bin/activate
```
3. Install Requirements\
 ```bash
pip install -r requirements.txt
```
4. Train Model
```bash
python main.py
```
 5. Run Web Application
```bash
python app.py
```






