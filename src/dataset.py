import pandas as pd

# Data on energy consumption (kWh)
energy_data = {'jan': 100, 'feb': 120, 'mar': 130, 'apr': 150}

# Data on water consumption (m3)
water_data = {'jan': 50, 'feb': 55, 'mar': 60, 'apr': 65}

# Data on waste management (tonnes)
waste_data = {'jan': 5, 'feb': 6, 'mar': 7, 'apr': 8}

# Data on greenhouse gas emissions (kgCO2e)
ghg_data = {'jan': 1000, 'feb': 1100, 'mar': 1200, 'apr': 1300}

# Create a DataFrame to store all the data
data = {'Energy Consumption (kWh)': energy_data, 'Water Consumption (m3)': water_data,
        'Waste Management (tonnes)': waste_data, 'Greenhouse Gas Emissions (kgCO2e)': ghg_data}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Perform calculations as per GRESB standard
df["Energy Intensity (kWh/m2)"] = df["Energy Consumption (kWh)"]/df["Area"]
df["Water Intensity (m3/m2)"] = df["Water Consumption (m3)"]/df["Area"]
df["Waste Intensity (tonnes/m2)"] = df["Waste Management (tonnes)"]/df["Area"]
df["GHG Intensity (kgCO2e/m2)"] = df["Greenhouse Gas Emissions (kgCO2e)"]/df["Area"]

# Output the final report
df.to_csv("GRESB_Environmental_Report.csv")
