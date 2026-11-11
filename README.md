# 🎓 Student Success Predictor

An end-to-end Machine Learning project that predicts whether a student is likely to **Pass or Fail** based on their study hours, attendance, past academic scores, and sleep hours.

This project uses **Logistic Regression**, a supervised machine learning classification algorithm, to analyze student performance data and make predictions based on different academic factors.

## 🚀 Project Overview

The Student Success Predictor aims to demonstrate how Machine Learning can be used to analyze student performance and predict academic outcomes.

By providing information about a student's study routine and academic history, the trained model predicts whether the student is likely to pass or fail.

The project also evaluates the model using a classification report and confusion matrix to understand its performance.

## ✨ Key Features

- **Student Performance Prediction:** Predicts whether a student is likely to Pass or Fail.
- **Data Preprocessing:** Prepares numerical and categorical data for machine learning.
- **Feature Scaling:** Uses StandardScaler to standardize numerical features.
- **Logistic Regression:** Implements a supervised classification algorithm.
- **Model Evaluation:** Evaluates predictions using a classification report.
- **Confusion Matrix:** Visualizes correct and incorrect predictions using a Seaborn heatmap.
- **Custom Predictions:** Allows users to enter their own student information and receive predictions.
- **Prediction Probabilities:** Can display the probability of passing or failing.

## 🛠️ Technologies & Libraries

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading and manipulation |
| Matplotlib | Data visualization |
| Seaborn | Confusion matrix visualization |
| Scikit-learn | Machine Learning and preprocessing |

## 📊 Dataset Information

The project uses a student performance dataset containing 100 student records.

The dataset includes the following columns:

| Feature | Description |
|---|---|
| Study Hours | Number of hours spent studying |
| Attendance | Student attendance percentage |
| Past Score | Previous academic score |
| Internet | Internet availability (Yes/No) |
| Sleep Hours | Average hours of sleep |
| Passed | Target variable (Yes/No) |

**Target Variable:** `Passed`

- `0` = Fail
- `1` = Pass

## 🧠 Machine Learning Workflow

The project follows these Machine Learning steps:

1. **Data Loading:** Load the student dataset using Pandas.
2. **Data Exploration:** Examine the dataset using `head()` and other Pandas methods.
3. **Data Encoding:** Convert the target labels into numerical values.
4. **Feature Selection:** Select Study Hours, Attendance, Past Score, and Sleep Hours as input features.
5. **Feature Scaling:** Apply StandardScaler to standardize numerical features.
6. **Train-Test Split:** Divide the dataset into 80% training data and 20% testing data.
7. **Model Training:** Train a Logistic Regression model.
8. **Prediction:** Generate predictions using the testing dataset.
9. **Model Evaluation:** Evaluate the model using a classification report and confusion matrix.
10. **Custom Prediction:** Accept new student information and predict the academic outcome.

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/student-success-predictor.git
```

### 2. Navigate to the Project Folder

```bash
cd student-success-predictor
```

### 3. Install Required Libraries

```bash
pip install pandas matplotlib seaborn scikit-learn
```

### 4. Run the Project

```bash
python student_success_predictor.py
```

## 📁 Project Structure

```text
Student-Success-Predictor/
│
├── archive/
│   └── student_performance_100.csv
│
├── student_success_predictor.py
│
└── README.md
```

## 📈 Model Evaluation

The model's performance is evaluated using:

- **Accuracy:** Measures the overall percentage of correct predictions.
- **Precision:** Measures how many predicted positive cases were actually positive.
- **Recall:** Measures how many actual positive cases were correctly identified.
- **F1-Score:** Balances precision and recall.
- **Confusion Matrix:** Shows True Positives, True Negatives, False Positives, and False Negatives.

These evaluation techniques help understand how effectively the model predicts student academic performance.

## 🎯 Learning Outcomes

Through this project, I practiced and strengthened my understanding of:

- Supervised Machine Learning
- Classification Problems
- Logistic Regression
- Data Preprocessing
- Label Encoding
- Feature Scaling using StandardScaler
- Train-Test Split and Stratification
- Model Training and Prediction
- Classification Metrics
- Confusion Matrix Visualization
- Making Predictions with New Data

## 🔮 Future Improvements

- Build an interactive web application using Streamlit.
- Add more Machine Learning classification algorithms.
- Compare Logistic Regression with Random Forest and Decision Trees.
- Improve prediction performance through hyperparameter tuning.
- Add feature importance and student performance insights.
- Develop a more advanced student performance analysis dashboard.

## ⚠️ Disclaimer

This project is developed for educational and learning purposes. Predictions are based on the available dataset and should not be treated as guaranteed academic outcomes.

## 👨‍💻 Author

**Salman Khan**

AI/ML Student | Aspiring AI Engineer

Currently learning Machine Learning and building practical AI projects to strengthen my skills.

---

⭐ If you find this project interesting, consider giving this repository a star!
