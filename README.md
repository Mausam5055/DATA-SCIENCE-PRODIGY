# DATA-SCIENCE-PRODIGY

A comprehensive collection of data science projects, each focusing on a unique real-world dataset and problem. This repository is designed for learning, exploration, and demonstration of data analysis, visualization, and machine learning techniques.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Project Summaries](#project-summaries)
- [Usage Instructions](#usage-instructions)
- [Dependencies](#dependencies)
- [Credits](#credits)

---

## Project Overview

This repository contains five major data science projects, each in its own subfolder. Each project includes datasets, code, visualizations, and documentation to guide you through the data science workflow: data cleaning, analysis, visualization, and modeling.

---

## Project Structure

| Folder           | Project Title/Theme                | Main Dataset(s)                  | Main Script      | Description                       |
|------------------|------------------------------------|----------------------------------|------------------|------------------------------------|
| PRODIGY_DS_01    | World Population Analysis          | API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv | main.py          | Population data analysis and visualization |
| PRODIGY_DS_02    | Titanic Survival Prediction        | train.csv, test.csv              | main.py          | Data cleaning, EDA, and ML on Titanic dataset |
| PRODIGY_DS_03    | Bank Marketing Decision Tree       | bank.csv                         | build_tree.py    | Decision tree modeling on bank marketing data |
| PRODIGY_DS_04    | Twitter Sentiment Analysis         | twitter_training.csv             | main.py          | Sentiment analysis and keyword extraction |
| PRODIGY_DS_05    | US Traffic Accident Analysis       | US_Accidents_March23.csv         | analyze_accidents.py | Accident data analysis and visualization |

---

## Project Summaries

### 1. PRODIGY_DS_01: World Population Analysis
- **Goal:** Analyze and visualize global population trends by region and country.
- **Key Files:**
  - `main.py`: Data processing and visualization
  - `API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv`: Main dataset
  - Output images: `population_by_region.png`, `population_distribution.png`, etc.
- **Documentation:** Task PDF and mind map included.

### 2. PRODIGY_DS_02: Titanic Survival Prediction
- **Goal:** Predict passenger survival using the Titanic dataset.
- **Key Files:**
  - `main.py`: Data cleaning, feature engineering, and modeling
  - `train.csv`, `test.csv`: Datasets
  - Output images: Age distribution, survival by class/sex, heatmaps
- **Documentation:** Step-by-step explanation PDF and mind map.

### 3. PRODIGY_DS_03: Bank Marketing Decision Tree
- **Goal:** Build a decision tree to predict client subscription to term deposits.
- **Key Files:**
  - `build_tree.py`: Model building and evaluation
  - `bank.csv`: Dataset
- **Documentation:** Task PDF and mind map.

### 4. PRODIGY_DS_04: Twitter Sentiment Analysis
- **Goal:** Classify tweets by sentiment and extract top keywords.
- **Key Files:**
  - `main.py`: Data processing, sentiment analysis, visualization
  - `twitter_training.csv`: Dataset
  - Output images: Sentiment distribution, top keywords per sentiment
- **Documentation:** Task PDF and mind map.

### 5. PRODIGY_DS_05: US Traffic Accident Analysis
- **Goal:** Analyze and visualize US traffic accident data for patterns and hotspots.
- **Key Files:**
  - `analyze_accidents.py`: Data analysis and visualization
  - `Data/US_Accidents_March23.csv`: Dataset
  - Output: Various PNGs and interactive HTML maps
- **Documentation:** PDF and mind map in Documentation/

---

## Usage Instructions

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd DATA-SCIENCE-PRODIGY
   ```
2. **Navigate to a project folder:**
   ```bash
   cd PRODIGY_DS_01  # or any other subproject
   ```
3. **Install dependencies:**
   - Most projects require Python 3.x and common data science libraries (see below).
   - Install with:
     ```bash
     pip install -r requirements.txt  # if available
     # or manually install: pandas, numpy, matplotlib, seaborn, scikit-learn, etc.
     ```
4. **Run the main script:**
   ```bash
   python main.py  # or build_tree.py, analyze_accidents.py, etc.
   ```
5. **View outputs:**
   - Visualizations and results are saved as PNG or HTML files in the respective folders.

---

## Dependencies

Most projects use the following Python libraries:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- plotly (for interactive plots)

Install them via pip if not already installed.

---

## Credits

- **Author:** [Your Name or Team]
- **Contact:** [Your Email or GitHub]
- **License:** For educational and demonstration purposes.

---

For detailed instructions and explanations, refer to the ReadMe.md or PDF documentation in each subproject folder. 