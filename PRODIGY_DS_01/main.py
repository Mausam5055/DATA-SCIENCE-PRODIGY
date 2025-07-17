import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
try:
    population_df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv', skiprows=4)
    country_meta_df = pd.read_csv('Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv')

    # --- Data Cleaning ---
    # Drop unnecessary columns
    population_df.drop(columns=['Unnamed: 69'], inplace=True)
    country_meta_df.drop(columns=['Unnamed: 5'], inplace=True)

    # --- Merge DataFrames ---
    # Merge the population data with the country metadata
    merged_df = pd.merge(population_df, country_meta_df, on='Country Code', how='left')

    # --- Bar Chart: Population by Region in 2022 ---
    # Filter out rows that are not actual countries (e.g., regions, income groups)
    regions_df = merged_df.dropna(subset=['Region'])

    # Calculate the total population for each region in 2022
    region_population = regions_df.groupby('Region')['2022'].sum().sort_values(ascending=False)

    # Create the bar chart
    plt.figure(figsize=(12, 8))
    sns.barplot(x=region_population.values, y=region_population.index, palette='viridis')
    plt.title('Total Population by Region in 2022')
    plt.xlabel('Total Population')
    plt.ylabel('Region')
    plt.tight_layout()
    plt.savefig('population_by_region.png')
    plt.close()

    # --- Histogram: Distribution of Country Populations in 2022 ---
    # Filter for the year 2022 and drop rows with missing population data
    population_2022 = merged_df[['Country Name', '2022']].dropna()
    # Also remove the aggregate regions/income groups from this list for a true country distribution
    population_2022 = population_2022[population_2022['Country Name'].isin(regions_df['Country Name'])]


    # Create the histogram
    plt.figure(figsize=(12, 6))
    sns.histplot(population_2022['2022'], bins=30, kde=True)
    plt.title('Distribution of Country Populations in 2022')
    plt.xlabel('Population')
    plt.ylabel('Number of Countries')
    plt.savefig('population_distribution.png')
    plt.close()

    # Create the histogram with a logarithmic scale for the x-axis
    plt.figure(figsize=(12, 6))
    sns.histplot(population_2022['2022'], bins=30, kde=True, log_scale=True)
    plt.title('Distribution of Country Populations in 2022 (Log Scale)')
    plt.xlabel('Population (Log Scale)')
    plt.ylabel('Number of Countries')
    plt.savefig('population_distribution_log.png')
    plt.close()
    
    print("Visualizations created successfully!")

except FileNotFoundError:
    print("Make sure the CSV files are in the same directory as the script.")
except Exception as e:
    print(f"An error occurred: {e}")