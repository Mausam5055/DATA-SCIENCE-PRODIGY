# US Traffic Accident Analysis

## Overview
This project analyzes US traffic accident data to identify patterns related to road conditions, weather, time of day, and location. It provides deep exploratory data analysis (EDA) and rich visualizations to uncover accident hotspots and contributing factors.

## Dataset
- **Source:** [US Accidents (Kaggle)](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)
- **Note:** The raw CSV file is very large and is not included in the repository. Please download it from Kaggle and place it in the `Data/` folder as `US_Accidents_March23.csv`.

## Setup Instructions
1. **Clone the repository**
2. **Download the dataset** from Kaggle and place it in `Data/US_Accidents_March23.csv`
3. **Install required packages:**
   ```bash
   pip install pandas matplotlib seaborn folium
   ```
4. **Run the analysis script:**
   ```bash
   python analyze_accidents.py
   ```
5. **View the generated plots and maps** in the project directory.

## Methods & Techniques Used

| Step                        | Method/Technique/Visualization         | Description |
|-----------------------------|----------------------------------------|-------------|
| Data Loading                | pandas read_csv                        | Load large CSV efficiently |
| Data Cleaning               | Handling missing values, type conversion| Prepare data for analysis |
| Time Feature Engineering    | Extract hour, day of week, date        | Analyze temporal patterns |
| Severity Analysis           | Countplot, heatmap, boxplot            | Distribution and relation to other factors |
| Weather & Road Analysis     | Bar plots, heatmaps, crosstab          | Top conditions, interactions |
| Temporal Analysis           | Countplot, time series plot            | By hour, day, and over time |
| City Analysis               | Bar plot                               | Top 10 cities with most accidents |
| Correlation Analysis        | Correlation matrix heatmap             | Numerical feature relationships |
| Geospatial Visualization    | Folium heatmap, cluster map            | Accident hotspots, high-severity locations |

## Visualizations Generated

| File Name                      | Description |
|-------------------------------|-------------|
| accidents_by_hour.png          | Accidents by hour of day |
| accidents_by_weather.png       | Top 10 weather conditions in accidents |
| accidents_by_road.png          | Top 10 road conditions in accidents (if available) |
| accident_hotspots.html         | Interactive heatmap of accident locations |
| severity_distribution.png      | Distribution of accident severity |
| severity_by_hour.png           | Severity by hour of day (heatmap) |
| accidents_by_dayofweek.png     | Accidents by day of week |
| accidents_over_time.png        | Time series of accidents over days |
| top_cities.png                 | Top 10 cities with most accidents |
| weather_vs_road_heatmap.png    | Weather vs. road condition interaction |
| severity_by_weather.png        | Severity by top 10 weather conditions |
| correlation_matrix.png         | Correlation matrix of numerical features |
| accident_cluster_map.html      | Interactive cluster map of accidents |
| high_severity_hotspots.html    | Heatmap of high-severity accident locations |

## .gitignore
To avoid pushing the large dataset to GitHub, ensure your `.gitignore` includes:
```
# Ignore large data files
Data/US_Accidents_March23.csv
```

## Notes
- The script is modular and can be extended for further analysis.
- For any custom analysis or visualization, modify `analyze_accidents.py` as needed.

---
**Author:** [Your Name]
