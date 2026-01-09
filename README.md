# 🎓 Intelligent Student Performance Predictor

A full-stack Machine Learning web application that predicts a student’s expected exam score based on key academic and lifestyle factors.
Built using Python, Machine Learning (Linear Regression), and Flask, and deployed as a real-world web application.

## 🚀 Project Overview

The Intelligent Student Performance Predictor estimates a realistic score range for a student by analyzing:

📚 Study Hours

🏫 Class Attendance

😴 Sleep Hours

📈 Previous Academic Performance

The system is designed to handle dataset bias (especially toward average-performing students) and outputs practical score ranges instead of misleading exact values.

This project represents an end-to-end ML workflow, from training on a large dataset to real deployment.

## 🧠 How It Works

Data Preprocessing

Cleaning and organizing a dataset with 10,000+ records

Feature selection and normalization

Model Training

Supervised Machine Learning using Linear Regression

Model evaluation using metrics like MAE (Mean Absolute Error)

Bias-Aware Prediction

Instead of a single number, the model returns score ranges

Different ranges for average and above-average students to improve realism

Model Serialization

Trained model exported using Joblib (.pkl)

Allows reuse without retraining

Web Deployment

Flask-based backend

Model loaded and used for live predictions via web interface

## 🛠️ Tech Stack
### 🔹 Backend & ML

Python 3

Flask

Scikit-learn

Pandas

NumPy

Joblib

### 🔹 Frontend

HTML

CSS

Jinja2 Templates

##🔹 Tools & Platforms

Google Colab (Model Training & Evaluation)

Replit (Web App Development)

Git & GitHub (Version Control & Deployment)

## 📂 Project Structure
├── app.py                  # Flask application entry point
├── student_model.pkl       # Trained ML model (Joblib)
├── templates/
│   └── index.html          # Frontend UI
├── static/
│   └── style.css           # Styling
├── requirements.txt        # Dependencies
└── README.md               # Project documentation

## ▶️ How to Run Locally

### Clone the Repository

git clone https://github.com/Samin-Saikia/Intelligent-Student-Performance-Predictor


### Install Dependencies

pip install -r requirements.txt


### Run the Application

python app.py


### Open in Browser

<http://127.0.0.1:5000/>

## 🎯 Key Learnings from This Project

Large datasets require thoughtful evaluation

Model bias must be handled consciously

Deployment is just as important as training

Separating training environment and deployment environment is powerful

ML models can be reused across platforms with .pkl files

## 🌟 Why This Project Matters

This was my first complete Machine Learning project, and it goes beyond basic experimentation:

Trained on a large dataset

Solved real environment limitations

Deployed as a working web application

Demonstrates practical ML engineering skills

It proves that meaningful ML projects can be built even with limited hardware by using the right tools and workflows.

## 🔮 Future Improvements

Support for multiple ML models

User accounts & prediction history

Better frontend (React-based UI)

Advanced regression or ensemble methods

Model explainability (feature importance)

## 👤 Author

Samin Saikia
Aspiring Developer & ML Enthusiast

