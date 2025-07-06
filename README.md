# Titanic Survival Prediction – Data Science Mini Project 🚢

This is a beginner-friendly end-to-end machine learning project to predict survival of Titanic passengers using various features like class, gender, age, fare, and family size.

### 📊 Accuracy Achieved:
**80.4%** on test data using a tuned Random Forest classifier.

---

## 🧠 Features Used:
- Pclass, Sex, Age, Fare, SibSp, Parch, Embarked
- Engineered: `FamilySize`, `IsAlone`, `Title`

---

## 🤖 Models Implemented:
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest (with GridSearchCV)

---

## 📈 Tools & Libraries:
- `pandas`, `numpy`, `matplotlib`, `seaborn`
- `scikit-learn` for ML models and GridSearch

---

## 📂 File Structure
- `titanic_model.ipynb` – Jupyter notebook with code and visualizations
- `titanic_cheatsheet.pdf` – Summary + quiz (optional)
- `README.md` – You're reading it

---

### ✅ Result:
Final tuned model achieved **80.4% test accuracy**  
Best hyperparameters via GridSearchCV:
```python
{'max_depth': 10, 'min_samples_split': 10, 'n_estimators': 100}


What I Learned:
Feature engineering boosts accuracy

Random Forest works great for structured data

GridSearchCV is key to tuning a model

Data science is actually fun!

Built by Tia Sukhnanni | Guided by ChatGPT 🤖
