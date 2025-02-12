import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Set the directory for the CSV and Excel files
data_dir = "E:\\py\\"

# Files to process (key: CSV filename, value: corresponding column name)
files = {
    "CLMMAXT_HKA_2024.csv": "Max Temperature",
    "CLMMINT_HKA_2024.csv": "Min Temperature",
    "CLMTEMP_HKA_2024.csv": "Average Temperature"
}

# Read the main data (daily rainfall)
main_csv = "daily_HKA_RF_2024.csv"
main_df = pd.read_csv(os.path.join(data_dir, main_csv), skiprows=2)

# Set correct column names
main_df.columns = ["Year", "Month", "Day", "Total Rainfall (mm)", "Data Completeness"]

# **Handle "Trace" values, convert them to 0.05 mm**
main_df["Total Rainfall (mm)"] = main_df["Total Rainfall (mm)"].replace("Trace", 0.05)
main_df["Total Rainfall (mm)"] = pd.to_numeric(main_df["Total Rainfall (mm)"], errors="coerce")

# Merge other weather data into the main dataframe
for csv_file, col_name in files.items():
    file_path = os.path.join(data_dir, csv_file)
    
    # Read CSV file
    df = pd.read_csv(file_path, skiprows=2)
    
    # Set correct column names
    df.columns = ["Year", "Month", "Day", "Value", "Data Completeness"]

    # Keep only the "Value" column and rename it
    df = df[["Year", "Month", "Day", "Value"]]
    df.rename(columns={"Value": col_name}, inplace=True)

    # **Merge the data**
    main_df = main_df.merge(df, on=["Year", "Month", "Day"], how="left")

# Output to Excel
output_path = os.path.join(data_dir, "merged_weather_data.xlsx")

# 檢查文件是否存在，並提示是否覆蓋
if os.path.exists(output_path):
    print(f"⚠️ File already exists: {output_path}. Overwriting...")
main_df.to_excel(output_path, index=False)
print(f"✅ Data has been merged and saved to: {output_path}")

# **Scatter Plot**
plt.figure(figsize=(10, 6))
plt.scatter(main_df["Total Rainfall (mm)"], main_df["Max Temperature"], color='blue', label="Rainfall vs Max Temperature")
plt.scatter(main_df["Total Rainfall (mm)"], main_df["Min Temperature"], color='red', label="Rainfall vs Min Temperature")
plt.scatter(main_df["Total Rainfall (mm)"], main_df["Average Temperature"], color='green', label="Rainfall vs Average Temperature")

plt.xlabel("Total Rainfall (mm)")
plt.ylabel("Temperature (°C)")
plt.title("Relationship between Rainfall and Temperature")
plt.legend()
plt.tight_layout()

# 保存散點圖
scatter_plot_path = os.path.join(data_dir, "scatter_plot.png")
if os.path.exists(scatter_plot_path):
    print(f"⚠️ File already exists: {scatter_plot_path}. Overwriting...")
plt.savefig(scatter_plot_path)  # 保存散點圖
print(f"✅ Scatter plot saved to: {scatter_plot_path}")

# **Plot the Correlation Matrix Heatmap**
plt.figure(figsize=(8, 6))
correlation_matrix = main_df[["Total Rainfall (mm)", "Max Temperature", "Min Temperature", "Average Temperature"]].corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", cbar_kws={'label': 'Correlation Coefficient'})
plt.title("Correlation of Meteorological Data")

# 保存熱力圖
heatmap_path = os.path.join(data_dir, "correlation_heatmap.png")
if os.path.exists(heatmap_path):
    print(f"⚠️ File already exists: {heatmap_path}. Overwriting...")
plt.savefig(heatmap_path)  # 保存熱力圖
print(f"✅ Heatmap saved to: {heatmap_path}")

# 一次性顯示所有圖形
plt.show()