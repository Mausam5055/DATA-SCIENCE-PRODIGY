# Titanic Dataset: Data Cleaning and Exploratory Data Analysis (EDA)

## Overview

This repository contains comprehensive data cleaning and exploratory data analysis (EDA) of the Titanic dataset, prepared as **Task 02** for Prodigy Data Science Internship. The project demonstrates a step-by-step approach to understanding, cleaning, analyzing, and visualizing real-world data using Python.

## Project Structure

| File/Folder        | Description                                     |
|--------------------|-------------------------------------------------|
| `train.csv`        | Training data used for analysis and EDA         |
| `png_outputs/`     | Folder containing all visualization PNGs         |
| `titanic_eda.py` or `notebook.ipynb` | Python script or Jupyter notebook with full analysis |

## Key Skills Demonstrated

- Data inspection with Pandas
- Handling missing values & data cleaning
- Feature engineering
- Visual data exploration with Matplotlib & Seaborn
- Professional plot saving for reporting

## Getting Started

### Prerequisites

- Python 3.x
- Libraries: pandas, numpy, matplotlib, seaborn

```bash
pip install pandas numpy matplotlib seaborn
```

### Running the Code

1. Place the Titanic `train.csv` file in your working directory.
2. Run `titanic_eda.py` (or execute the cells if using a Jupyter notebook).
3. All plots will be automatically saved to the `png_outputs/` directory.

## Data Cleaning Steps

| Step                     | Description                                                                                        |
|--------------------------|----------------------------------------------------------------------------------------------------|
| **Missing Values**       | Filled missing `Age` values with the median, `Embarked` with the mode; dropped `Cabin` column.    |
| **Type Conversion**      | Converted `Sex` and `Embarked` columns to categorical data.                                        |
| **Feature Engineering**  | Created new feature `FamilySize` = `SibSp` + `Parch` + 1.                                         |

## Exploratory Data Analysis (EDA)

### 1. Univariate Analysis

Plots distribution and counts for individual variables.

| Plot File                                      | Description                    |
|------------------------------------------------|--------------------------------|
| `png_outputs/survival_count.png`               | Bar chart: Survived vs Not     |
| `png_outputs/age_distribution.png`             | Histogram: Age distribution    |

### 2. Bivariate Analysis

Compares two variables to explore relationships.

| Plot File                           | Description                              |
|-------------------------------------|------------------------------------------|
| `png_outputs/survival_by_sex.png`   | Survival rate by gender                  |
| `png_outputs/survival_by_pclass.png`| Survival rate by passenger class         |
| `png_outputs/age_vs_survival.png`   | Age distribution by survival outcome     |

### 3. Correlation Analysis

| Plot File                                | Description                          |
|------------------------------------------|--------------------------------------|
| `png_outputs/correlation_heatmap.png`    | Heatmap of numeric feature correlations|

## Insights & Observations

- **Women and children** were more likely to survive.
- **Higher passenger class** increased chances of survival.
- **Family size** had visible impact on survival probabilities.
- **Paying higher fares** correlated with higher survival rates.

## Output Examples

| Example Image              | Purpose                      |
|----------------------------|------------------------------|
| ![Survival Count](png_outputs/survival_count count of survivors         |
| ![Survival by Sex](png_outputs/survival_by-based survival comparison |

*All output plots are found in the `png_outputs/` folder for easy review and presentation.*

## How to Use This Project

- **For learning:** Study the code and plots to understand a classic EDA workflow.
- **For reporting:** Use the PNGs in presentations or reports.
- **For modeling:** Refined data can be used for machine learning predictions.

## Acknowledgments

- Dataset: [Kaggle Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic/overview)

## Contact

For questions about this project, please contact [Your Name] (Intern, Prodigy Data Science Cohort).

**_End of Task 02 Submission: Data Cleaning & EDA with Titanic Dataset_**

[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/51244028/7ab23aa2-cf06-4a21-9298-67b7c1fc22a4/gender_submission.csv
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/51244028/9d174d1a-de62-4dec-bba3-8c0e026ac807/test.csv
[3] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/51244028/163a42bf-42d6-45e1-bf5d-a2a477a19613/train.csv