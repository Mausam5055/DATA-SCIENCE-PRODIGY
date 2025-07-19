import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap
import os

# 1. Load Data
DATA_PATH = os.path.join('Data', 'US_Accidents_March23.csv')
df = pd.read_csv(DATA_PATH)

# 2. Data Cleaning
# Select relevant columns
columns_needed = [
    'ID', 'Start_Time', 'End_Time', 'Start_Lat', 'Start_Lng',
    'Weather_Condition', 'Road_Condition', 'Severity'
]
# Some datasets may not have 'Road_Condition', so check and adjust
columns_available = [col for col in columns_needed if col in df.columns]
df = df[columns_available]

# Convert Start_Time to datetime
if 'Start_Time' in df.columns:
    df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
    df['Hour'] = df['Start_Time'].dt.hour
    df['Date'] = df['Start_Time'].dt.date

# Handle missing values
for col in ['Weather_Condition', 'Road_Condition']:
    if col in df.columns:
        df[col] = df[col].fillna('Unknown')

# 3. EDA: Patterns by Time of Day
if 'Hour' in df.columns:
    plt.figure(figsize=(10,6))
    sns.countplot(x='Hour', data=df, palette='viridis')
    plt.title('Accidents by Hour of Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Accidents')
    plt.tight_layout()
    plt.savefig('accidents_by_hour.png')
    plt.close()

# 4. EDA: Patterns by Weather Condition
if 'Weather_Condition' in df.columns:
    top_weather = df['Weather_Condition'].value_counts().nlargest(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x=top_weather.index, y=top_weather.values, palette='coolwarm')
    plt.title('Top 10 Weather Conditions in Accidents')
    plt.xlabel('Weather Condition')
    plt.ylabel('Number of Accidents')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('accidents_by_weather.png')
    plt.close()

# 5. EDA: Patterns by Road Condition (if available)
if 'Road_Condition' in df.columns:
    top_road = df['Road_Condition'].value_counts().nlargest(10)
    plt.figure(figsize=(10,6))
    sns.barplot(x=top_road.index, y=top_road.values, palette='magma')
    plt.title('Top 10 Road Conditions in Accidents')
    plt.xlabel('Road Condition')
    plt.ylabel('Number of Accidents')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('accidents_by_road.png')
    plt.close()

# 6. Accident Hotspots Visualization (Heatmap)
if {'Start_Lat', 'Start_Lng'}.issubset(df.columns):
    # Remove rows with missing coordinates
    df_map = df.dropna(subset=['Start_Lat', 'Start_Lng'])
    # Sample for performance if too large
    if len(df_map) > 10000:
        df_map = df_map.sample(10000, random_state=42)
    # Center map
    map_center = [df_map['Start_Lat'].mean(), df_map['Start_Lng'].mean()]
    accident_map = folium.Map(location=map_center, zoom_start=5)
    heat_data = list(zip(df_map['Start_Lat'], df_map['Start_Lng']))
    HeatMap(heat_data, radius=8, blur=6).add_to(accident_map)
    accident_map.save('accident_hotspots.html')

# --- Enhanced Analysis & Visualizations ---

# 1. Severity Distribution
plt.figure(figsize=(8,5))
sns.countplot(x='Severity', data=df, palette='Set2')
plt.title('Accident Severity Distribution')
plt.xlabel('Severity (1=Low, 4=High)')
plt.ylabel('Number of Accidents')
plt.tight_layout()
plt.savefig('severity_distribution.png')
plt.close()

# 2. Severity by Hour of Day
if 'Hour' in df.columns:
    plt.figure(figsize=(10,6))
    sns.heatmap(pd.crosstab(df['Hour'], df['Severity']), annot=True, fmt='d', cmap='YlOrRd')
    plt.title('Accident Severity by Hour of Day')
    plt.xlabel('Severity')
    plt.ylabel('Hour of Day')
    plt.tight_layout()
    plt.savefig('severity_by_hour.png')
    plt.close()

# 3. Accidents by Day of Week
if 'Start_Time' in df.columns:
    df['DayOfWeek'] = df['Start_Time'].dt.day_name()
    order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    plt.figure(figsize=(10,6))
    sns.countplot(x='DayOfWeek', data=df, order=order, palette='pastel')
    plt.title('Accidents by Day of Week')
    plt.xlabel('Day of Week')
    plt.ylabel('Number of Accidents')
    plt.tight_layout()
    plt.savefig('accidents_by_dayofweek.png')
    plt.close()

# 4. Time Series: Accidents Over Time
if 'Date' in df.columns:
    daily_counts = df.groupby('Date').size()
    plt.figure(figsize=(14,6))
    daily_counts.plot()
    plt.title('Accidents Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Accidents')
    plt.tight_layout()
    plt.savefig('accidents_over_time.png')
    plt.close()

# 5. Top 10 Cities with Most Accidents
if 'City' in df.columns:
    top_cities = df['City'].value_counts().nlargest(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x=top_cities.index, y=top_cities.values, palette='Blues_d')
    plt.title('Top 10 Cities with Most Accidents')
    plt.xlabel('City')
    plt.ylabel('Number of Accidents')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('top_cities.png')
    plt.close()

# 6. Weather vs. Road Condition Crosstab
if 'Weather_Condition' in df.columns and 'Road_Condition' in df.columns:
    crosstab = pd.crosstab(df['Weather_Condition'], df['Road_Condition'])
    crosstab = crosstab.loc[crosstab.sum(axis=1).nlargest(10).index, crosstab.sum().nlargest(5).index]
    plt.figure(figsize=(12,8))
    sns.heatmap(crosstab, annot=True, fmt='d', cmap='crest')
    plt.title('Weather vs. Road Condition (Top 10 Weather, Top 5 Road)')
    plt.tight_layout()
    plt.savefig('weather_vs_road_heatmap.png')
    plt.close()

# 7. Severity by Weather Condition (Top 10)
if 'Weather_Condition' in df.columns:
    top_weather = df['Weather_Condition'].value_counts().nlargest(10).index
    plt.figure(figsize=(14,7))
    sns.boxplot(x='Weather_Condition', y='Severity', data=df[df['Weather_Condition'].isin(top_weather)], palette='Set3')
    plt.title('Severity by Top 10 Weather Conditions')
    plt.xlabel('Weather Condition')
    plt.ylabel('Severity')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('severity_by_weather.png')
    plt.close()

# 8. Correlation Matrix for Numerical Features
num_cols = ['Severity', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)', 'Hour']
num_cols = [col for col in num_cols if col in df.columns]
if len(num_cols) > 1:
    plt.figure(figsize=(10,8))
    corr = df[num_cols].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix (Numerical Features)')
    plt.tight_layout()
    plt.savefig('correlation_matrix.png')
    plt.close()

# 9. Advanced Geospatial: Cluster Map of Accidents
try:
    from folium.plugins import MarkerCluster
    if {'Start_Lat', 'Start_Lng'}.issubset(df.columns):
        df_map = df.dropna(subset=['Start_Lat', 'Start_Lng'])
        if len(df_map) > 2000:
            df_map = df_map.sample(2000, random_state=42)
        map_center = [df_map['Start_Lat'].mean(), df_map['Start_Lng'].mean()]
        cluster_map = folium.Map(location=map_center, zoom_start=5)
        marker_cluster = MarkerCluster().add_to(cluster_map)
        for idx, row in df_map.iterrows():
            folium.Marker(location=[row['Start_Lat'], row['Start_Lng']], popup=f"Severity: {row['Severity']}").add_to(marker_cluster)
        cluster_map.save('accident_cluster_map.html')
except Exception as e:
    print(f"Could not create cluster map: {e}")

# 10. High Severity Accident Hotspots
if {'Start_Lat', 'Start_Lng', 'Severity'}.issubset(df.columns):
    df_severe = df[df['Severity'] == df['Severity'].max()].dropna(subset=['Start_Lat', 'Start_Lng'])
    if len(df_severe) > 1000:
        df_severe = df_severe.sample(1000, random_state=42)
    if not df_severe.empty:
        map_center = [df_severe['Start_Lat'].mean(), df_severe['Start_Lng'].mean()]
        severe_map = folium.Map(location=map_center, zoom_start=5)
        heat_data = list(zip(df_severe['Start_Lat'], df_severe['Start_Lng']))
        HeatMap(heat_data, radius=8, blur=6).add_to(severe_map)
        severe_map.save('high_severity_hotspots.html')

# --- End of Enhanced Analysis ---

print("Analysis complete!\n")
print("Generated visualizations:")
print("- accidents_by_hour.png")
print("- accidents_by_weather.png")
if 'Road_Condition' in df.columns:
    print("- accidents_by_road.png")
print("- accident_hotspots.html (open in browser)")
print("- severity_distribution.png")
print("- severity_by_hour.png")
print("- accidents_by_dayofweek.png")
print("- accidents_over_time.png")
print("- top_cities.png")
print("- weather_vs_road_heatmap.png")
print("- severity_by_weather.png")
print("- correlation_matrix.png")
print("- accident_cluster_map.html (open in browser)")
print("- high_severity_hotspots.html (open in browser)")

print("\nIf you are missing any packages, install them with:")
print("pip install pandas matplotlib seaborn folium") 