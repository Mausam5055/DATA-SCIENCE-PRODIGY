# 🧠 Prodigy InfoTech Data Science Internship - Task 01  
## Decision Tree Classifier for Customer Subscription Prediction

This repository contains the solution for **Task 01** of my **Data Science Internship at Prodigy InfoTech**. The main objective is to build and visualize a **Decision Tree Classifier** that predicts whether a customer will subscribe to a **term deposit** based on demographic and campaign-related data.

---

## 📋 Task Description

**Task-03**: Implement a Decision Tree Classifier to predict a binary outcome (Yes/No) based on the customer's data.

### The task includes:
- 🔄 Data Preprocessing  
- 🧠 Model Implementation  
- ✅ Model Evaluation  
- 🌳 Visualization of the Decision Tree

---

## 💾 Dataset Used

The dataset used is the **Bank Marketing Dataset** from the **UCI Machine Learning Repository**. It includes data from direct marketing campaigns by a Portuguese banking institution.

| File Name  | Description                                      |
|------------|--------------------------------------------------|
| bank.csv   | Customer attributes and campaign outcomes        |

### Dataset Overview

| Property           | Details                                   |
|--------------------|--------------------------------------------|
| 📚 Source          | [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/bank+marketing) |
| 🧑‍🤝‍🧑 Instances     | 45,211                                    |
| 📊 Features        | 16 input features + 1 binary target         |
| 🎯 Target Variable | `deposit` (yes = subscribed, no = not subscribed) |

---

## ⚙️ Methodology

### 🔹 Step 1: Data Loading
- Loaded the dataset using **Pandas**.

### 🔹 Step 2: Data Cleaning & Preprocessing
- Converted the target variable `deposit` to binary: `1` for *yes*, `0` for *no*.
- Applied **One-Hot Encoding** to categorical features: `job`, `marital`, `education`, etc.

### 🔹 Step 3: Model Training
- Split dataset into 80% training and 20% testing.
- Trained a **DecisionTreeClassifier** from **Scikit-learn**.
- Used `max_depth=5` to prevent overfitting.

### 🔹 Step 4: Model Evaluation & Visualization
- Evaluated model using **accuracy score** and **classification report**.
- Visualized the decision tree using **Graphviz**.

---

## 📊 Visualizations & Insights

### 🌲 Decision Tree Flowchart

A flowchart illustrating the tree-based decisions made by the model.

#### 🔍 Key Insights:
- **`duration`** (last contact duration) is the most significant factor.
- Other key factors: **`age`**, **`housing` loan status**, and **`poutcome`**.
- These insights can help refine future marketing strategies.

---

## 🛠️ Tools & Libraries

| Tool/Library | Purpose                                  |
|--------------|------------------------------------------|
| Python       | Programming language                     |
| Pandas       | Data loading, cleaning, and manipulation |
| Scikit-learn | Model implementation and evaluation      |
| Graphviz     | Decision tree visualization              |

---

## 🚀 How to Run

### Step-by-step Instructions

```bash
# Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Install required libraries
pip install pandas scikit-learn graphviz
