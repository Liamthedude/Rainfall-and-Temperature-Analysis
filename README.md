
# My Data Science Portfolio

Welcome ! This repository showcases my work in data science, including various projects and analyses using Python, machine learning, and data visualization.

## Projects Overview

- **Rainfall and Temperature Analysis**: An analysis of the relationship between rainfall and temperature using a dataset from 2024.
  
## Data Source
- **Dataset**: Daily rainfall and temperature data for 2024, sourced from the Hong Kong Observatory (香港天文台).
  
          daily_HKA_RF_2024.csv: Daily rainfall data.

          CLMMAXT_HKA_2024.csv: Daily maximum temperature data.

          CLMMINT_HKA_2024.csv: Daily minimum temperature data.

          CLMTEMP_HKA_2024.csv: Daily average temperature data.

## Skills

- Python (Pandas, Matplotlib, Seaborn)
- Data Cleaning & Preprocessing
- Data Visualization


## Key Insights
-**Scatter Plot Analysis**:

          The scatter plots show the relationship between rainfall and temperature:

          Rainfall vs Max Temperature: No clear linear relationship is observed. The points are scattered, indicating weak correlation.

          Rainfall vs Min Temperature: Similar to max temperature, no significant linear trend is visible.

          Rainfall vs Average Temperature: The scatter plot also shows a weak relationship between rainfall and average temperature.
  

-**Correlation Matrix Analysis**:
          The correlation matrix heatmap reveals the following:

          Rainfall vs Temperature: The correlation coefficients are close to 0 (Rainfall vs Max Temperature: 0.04, Rainfall vs Min Temperature: 0.09, Rainfall vs  Average Temperature: 0.08), indicating no significant linear correlation.

          Temperature Variables: High correlation exists between temperature variables (Max, Min, and Average Temperature), with coefficients ranging from 0.96 to 0.99.
          
## Conclusion
- **Temperature Variables**: The maximum, minimum, and average temperatures are strongly correlated with each other, indicating a high degree of interdependence.

- **Rainfall and Temperature**: Rainfall shows little to no correlation with temperature variables, suggesting that there is no strong linear relationship between rainfall and temperature.
- The analysis demonstrates that while temperature variables are closely related to each other, rainfall operates independently of temperature in this dataset. This insight can be valuable for further studies, such as predicting weather patterns or understanding the impact of climate change on different meteorological variables.



## Code Structure
1. Import Libraries
```python
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
```
2. Set Data Directory &Define Files to Process
```python
data_dir = "E:\\py\\"

files = {
    "CLMMAXT_HKA_2024.csv": "Max Temperature",
    "CLMMINT_HKA_2024.csv": "Min Temperature",
    "CLMTEMP_HKA_2024.csv": "Average Temperature"
}
```
3.. Read Main Data (Daily Rainfall)
```python
main_csv = "daily_HKA_RF_2024.csv"
main_df = pd.read_csv(os.path.join(data_dir, main_csv), skiprows=2)
```
4. Set Correct Column Names
```python
main_df.columns = ["Year", "Month", "Day", "Total Rainfall (mm)", "Data Completeness"]
```

5. Data Cleaning & Preprocessing("Trace" Values)
```python
main_df["Total Rainfall (mm)"] = main_df["Total Rainfall (mm)"].replace("Trace", 0.05)
main_df["Total Rainfall (mm)"] = pd.to_numeric(main_df["Total Rainfall (mm)"], errors="coerce")
```

6. Data Merge Other Weather Data according to columns name
```python
for csv_file, col_name in files.items():
    file_path = os.path.join(data_dir, csv_file)
    df = pd.read_csv(file_path, skiprows=2)
    df.columns = ["Year", "Month", "Day", "Value", "Data Completeness"]
    df = df[["Year", "Month", "Day", "Value"]]
    df.rename(columns={"Value": col_name}, inplace=True)
    main_df = main_df.merge(df, on=["Year", "Month", "Day"], how="left")
```

7.Output csv to xlsx
```python
output_path = os.path.join(data_dir, "merged_weather_data.xlsx")
if os.path.exists(output_path):
    print(f"⚠️ File already exists: {output_path}. Overwriting...")
main_df.to_excel(output_path, index=False)
print(f"✅ Data has been merged and saved to: {output_path}")
```

8.Data Visualization and save imagine(Scatter Plot& Correlation Matrix Heatmap)
```python
plt.figure(figsize=(10, 6))
plt.scatter(main_df["Total Rainfall (mm)"], main_df["Max Temperature"], color='blue', label="Rainfall vs Max Temperature")
plt.scatter(main_df["Total Rainfall (mm)"], main_df["Min Temperature"], color='red', label="Rainfall vs Min Temperature")
plt.scatter(main_df["Total Rainfall (mm)"], main_df["Average Temperature"], color='green', label="Rainfall vs Average Temperature")
plt.xlabel("Total Rainfall (mm)")
plt.ylabel("Temperature (°C)")
plt.title("Relationship between Rainfall and Temperature")
plt.legend()
plt.tight_layout()
scatter_plot_path = os.path.join(data_dir, "scatter_plot.png")

if os.path.exists(scatter_plot_path):
    print(f"⚠️ File already exists: {scatter_plot_path}. Overwriting...")
plt.savefig(scatter_plot_path)
print(f"✅ Scatter plot saved to: {scatter_plot_path}")

plt.figure(figsize=(8, 6))
correlation_matrix = main_df[["Total Rainfall (mm)", "Max Temperature", "Min Temperature", "Average Temperature"]].corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", cbar_kws={'label': 'Correlation Coefficient'})
plt.title("Correlation of Meteorological Data")
heatmap_path = os.path.join(data_dir, "correlation_heatmap.png")

if os.path.exists(heatmap_path):
    print(f"⚠️ File already exists: {heatmap_path}. Overwriting...")
plt.savefig(heatmap_path)
print(f"✅ Heatmap saved to: {heatmap_path}")
```
## Contact

- Email: chunwailiu02@gmail.com
- LinkedIn: https://www.linkedin.com/in/chun-wai-liu-3253131b3/
