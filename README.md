# Giddly AI Enhancements – Internship Prototype

This repository contains prototype implementations and demos for the AI features
proposed in my Giddly Product Improvement Design Document.

## 📌 Features Included

### 1. Event Attendance Forecasting (Prototype)
A simple regression-based model that predicts expected event turnout using:
- Event category
- Time of day
- Day of week
- Host reputation
- Historical attendance trends (synthetic dataset)

Implemented in `prototype/forecasting_model.ipynb`.

### 2. AI Event Safety Check (Prototype)
A lightweight rule-based + ML-supported safety scoring function that detects
potentially unsafe or misleading events based on:
- Suspicious keywords
- Vague descriptions
- Organizer behavior
- Formatting patterns

Implemented in `prototype/safety_check.py`.


## 🔗 Design Document

The full write-up, feature specifications, bug reports, and technical design
can be found here:

👉 **Google Doc:** https://docs.google.com/document/d/1b3aKn3vIO3B5zmQhsO_w51buike4EdG0TLrYju77tfg/edit?usp=sharing
---

## 🚀 How to Run the Prototypes

### 1. Clone the Repository
git clone https://github.com/Srinidhi888/giddly-enhancements.git

cd giddly-enhancements


### 2. Install Dependencies


pip install -r requirements.txt


### 3. Run Safety Check

python prototype/safety_check.py

### 4. Open the Forecasting
Use Jupyter Notebook or VSCode:
jupyter notebook prototype/forecasting_model.ipynb

---

## 🧠 Notes
- This repo contains **prototype-level demos** intended to illustrate how AI/ML
  models can enhance the Giddly platform.
- These prototypes are simplified versions of production-ready systems.

---

## 👤 Author
**Srinidhi**  
Software Developer  
