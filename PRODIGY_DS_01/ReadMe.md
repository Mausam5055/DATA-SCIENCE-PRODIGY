# Prodigy InfoTech Data Science Internship - Task 01

## Visualizing World Population Data

This repository contains the work for Task 01 of my Data Science Internship at Prodigy InfoTech. The primary objective of this task is to create visualizations to understand the distribution of a categorical or continuous variable using world population data.

---

### 📋 Task Description

**Task-01:** Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable, such as the distribution of ages or genders in a population.

For this task, I have used the World Bank dataset for total population by country. The analysis involves:
1.  **Categorical Analysis:** Visualizing the total population grouped by geographical region (a categorical variable).
2.  **Continuous Analysis:** Visualizing the distribution of populations across all countries (a continuous variable).

---

### 💾 Dataset Used

The dataset is sourced from The World Bank and contains information about the total population for countries and regions from 1960 to 2022.

The dataset consists of the following files:

| File Name                                                 | Description                                                                 |
| --------------------------------------------------------- | --------------------------------------------------------------------------- |
| `API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv`                   | Main data file with population figures for each country and year.           |
| `Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv`  | Contains metadata for each country, including its region and income group.  |
| `Metadata_Indicator_API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv`| Contains metadata about the "Total Population" indicator.                   |

---

### ⚙️ Methodology

The analysis was performed following these steps:

1.  **Data Loading:** The primary population data and country metadata were loaded into pandas DataFrames.
2.  **Data Cleaning:** Unnecessary columns were removed from both DataFrames to streamline the dataset.
3.  **Data Merging:** The two DataFrames were merged on the `Country Code` to enrich the population data with regional information. This step was crucial for the categorical analysis.
4.  **Data Filtering:** The merged dataset was filtered to remove aggregate regional data, ensuring that visualizations were based only on individual country data.
5.  **Visualization:**
    * A **bar chart** was created to compare the total population by region for the year 2022.
    * A **histogram** was generated to show the distribution of populations for all countries in 2022. A logarithmic scale was used to better visualize the highly skewed data.

---

### 📊 Visualizations and Insights

#### 1. Bar Chart: Total Population by Region (2022)

This bar chart displays the total population for each world region. It provides a clear comparison of population sizes across different parts of the world.

![Population by Region](https://i.imgur.com/gJ4y2jH.png)

**Insight:** East Asia & Pacific and South Asia are by far the most populous regions, highlighting their significance in global demographics.

#### 2. Histogram: Distribution of Country Populations (2022)

This histogram shows the frequency distribution of country populations. Due to the vast differences in country sizes, a logarithmic scale provides a more insightful view.

![Population Distribution on a Log Scale](https://i.imgur.com/bX6tQ9E.png)

**Insight:** The distribution is heavily right-skewed, indicating that most countries have relatively small populations, while a few countries have extremely large populations. The peak in the histogram suggests a large number of countries have populations in the range of 10 to 100 million.

---

### 🛠️ Tools and Libraries

The following tools and libraries were used to complete this task:

| Tool/Library   | Description                                           |
| -------------- | ----------------------------------------------------- |
| **Python** | The core programming language for the analysis.       |
| **Pandas** | Used for data loading, manipulation, and cleaning.    |
| **Matplotlib** | The foundational library for creating visualizations. |
| **Seaborn** | A high-level interface for creating attractive statistical graphics. |

---

### 🚀 How to Run the Code

To replicate this analysis, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install the required libraries:**
    ```bash
    pip install pandas matplotlib seaborn
    ```

3.  **Run the Python script:**
    Make sure the dataset files are in the same directory as the script.
    ```bash
    python your_script_name.py
    ```
The script will generate the visualization images (`population_by_region.png` and `population_distribution_log.png`) in the project directory.

---

### 🙏 Acknowledgments

I would like to express my gratitude to **Prodigy InfoTech** for providing this excellent internship opportunity. This task has been a valuable experience in applying data visualization techniques to real-world data.
