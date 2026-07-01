# Startup Profit Prediction Web Application

## 📌 Project Description
This project is a complete End-to-End Machine Learning application built to predict the **Profit of Startups** based on their expenses (R&D Spend, Administration, Marketing Spend, and State). 

The project compares multiple regression models (Simple Linear, Multiple Linear, and Polynomial Regression) to find the best fit, and the final trained model is deployed using a web interface.

---

## 🛠️ Technologies Used
- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Joblib
- **Visualization:** Matplotlib, Seaborn (for Exploratory Data Analysis)
- **Web Framework:** Flask / Streamlit
- **Version Control:** Git & GitHub

---

## 📊 Machine Learning Pipeline Followed
1. **Data Exploration & Preprocessing:** Handled missing values, explored descriptive statistics (Mean, Variance, Std Dev), and generated distribution, scatter, and correlation plots.
2. **Feature Engineering:** Separated independent features ($X$) and target variable ($y$), and handled categorical data.
3. **Model Training & Evaluation:** Split dataset into 80% Train and 20% Test. Evaluated performance using MAE, MSE, and $R^2$ Score.
4. **Model Saving:** Saved the best-performing model as `model.pkl` using Joblib.

---

## 💻 How to Run This Project Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Startup_Profit_App.git](https://github.com/YOUR_USERNAME/Startup_Profit_App.git)
   cd Startup_Profit_App
