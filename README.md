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


This repository contains **two independent prototypes**:

- **Prototype 1:** AI Safety Check (Python script)
- **Prototype 2:** Event Attendance Forecasting (Jupyter Notebook)

You can run them separately using the instructions below.

### ▶️ Prototype 1: Run the AI Safety Check
```bash
python prototype/safety_check.py

This will display:
Safety score
Safety label
Detection of suspicious patterns

---

### ▶️ Prototype 2: Run the Event Forecasting Model
Open the Jupyter Notebook:

```bash
jupyter notebook prototype/forecasting_model.ipynb

This notebook demonstrates:
Synthetic event data
Feature encoding
A simple regression model
Predicted attendance for a new event
---

## 🧠 Notes
These prototypes are simplified demos, not production-ready systems.
The goal is to illustrate how AI/ML can enhance the Giddly experience.
The code uses synthetic data for demonstration.

---

## 👤 Author
**Srinidhi**  
AI/ML & Software Developer 
