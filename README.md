# 🎓 Student Performance Prediction – End-to-End ML Project

An **end-to-end Machine Learning web application** that predicts a student’s academic performance based on study habits, attendance, and lifestyle factors.
The project covers **data processing, model training, serialization, and deployment using Flask**.

---

## 🚀 Project Overview

This project demonstrates a complete **ML lifecycle**:

* Dataset creation & preprocessing
* Feature engineering
* Model training & evaluation
* Model persistence using `.pkl`
* Flask-based web interface for real-time predictions

The goal is to classify student performance as **Good / Average / Bad** based on multiple parameters.

---

## 🧠 Features Used for Prediction

* 📚 Study Hours per Day
* 🏫 Attendance Percentage
* 📊 Previous Academic Score
* 📱 Social Media Usage (hours/day)
* 🏅 Extracurricular Participation
* ⏳ Study Consistency

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Machine Learning:** Scikit-learn
* **Web Framework:** Flask
* **Frontend:** HTML (Jinja Templates)
* **Model Storage:** Pickle (`.pkl`)
* **Environment:** Virtual Environment (`venv`)

---

## 📂 Project Structure

```
Student-Performance-EndToEnd/
│
├── data/
│   └── processed_student_data.csv
│
├── model/
│   ├── student_pipeline.pkl
│   ├── label_encoder.pkl
│   └── feature_order.pkl
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ How to Run the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Student-Performance-EndToEnd.git
cd Student-Performance-EndToEnd
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Flask App

```bash
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 📊 Model Details

* Preprocessing and ML model are combined using a **Scikit-learn Pipeline**
* Label encoding is applied for categorical target values
* The trained model is saved using `pickle` for reuse during inference

---

## 🎯 Output

The system predicts student performance as:

* ✅ **Good**
* ⚠️ **Average**
* ❌ **Bad**

---

## 📌 Future Improvements

* Add database support for storing predictions
* Improve UI using CSS / Bootstrap
* Add authentication (Login/Signup)
* Deploy on cloud platforms (Render / AWS / Railway)
* Add model explainability (SHAP / Feature Importance)

---

## 👨‍💻 Author

**Pratik Deshmukh**
Computer Science Student | Machine Learning Enthusiast

---

## ⭐ If you like this project

Don’t forget to **star the repository** ⭐
