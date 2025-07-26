
# 🗞️ Project 8: News Headline Classifier

This project predicts the category of a news article headline using TF-IDF + Logistic Regression. It classifies headlines into five categories: Business, Sports, Tech, Entertainment, and World. Built using scikit-learn and deployed with Streamlit.

---

## 🧭 Phase-by-Phase Breakdown

### 🔹 Phase 1: Dataset Creation
- 25 news headlines
- 5 categories: Business, Sports, Tech, Entertainment, World
- File: `news_headlines_dataset.csv`

---

### 🔹 Phase 2: TF-IDF Vectorization
- Used `TfidfVectorizer` to convert text to numeric form
- Resulted in 90+ unique word features
- Created sparse matrix for model input

---

### 🔹 Phase 3: Model Training
- Model: `Logistic Regression`
- Train/test split: 80/20
- Evaluation: Precision, Recall, F1 Score
- File: `news_model.joblib`

---

### 🔹 Phase 4: Save Artifacts
- Saved model and TF-IDF vectorizer using `joblib`
- Files:
  - `models/news_model.joblib`
  - `models/tfidf_vectorizer.joblib`

---

### 🔹 Phase 5: Streamlit App
- UI: User enters a news headline → predicts category
- File: `app/news_classifier_app.py`

---

### 🔹 Phase 6: Hugging Face Deployment
- Files included:
  - `README.md` with YAML config
  - `requirements.txt` for dependencies
- Deploy-ready folder zipped

---

### 🔹 Phase 7: GitHub Setup
- GitHub-friendly ZIP created
- Includes all code, model, and README
- Great for portfolio or resume showcase

---

## 🎯 Core Components

| Stage           | Tools Used         | Output                          |
|----------------|--------------------|---------------------------------|
| Dataset         | Pandas             | `news_headlines_dataset.csv`    |
| Text Vector     | TfidfVectorizer    | TF-IDF matrix                    |
| Model           | LogisticRegression | Trained classifier               |
| UI              | Streamlit          | `news_classifier_app.py`         |
| Deployment      | Hugging Face       | Web app                          |
| Version Control | GitHub             | Repo-ready ZIP                   |
