import pandas as pd
import pyrebase
from openpyxl import Workbook

# Initialize Firebase
config = {
  "apiKey": "YOUR_API_KEY",
  "authDomain": "YOUR_AUTH_DOMAIN",
  "databaseURL": "YOUR_DATABASE_URL",
  "storageBucket": "YOUR_STORAGE_BUCKET"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Get data from Firebase
energy_data = db.child("energy_consumption").get().val()
water_data = db.child("water_consumption").get().val()
waste_data = db.child("waste_management").get().val()
ghg_data = db.child("ghg_emissions").get().val()

# Create a DataFrame to store all the data
data = {'Energy Consumption (kWh)': energy_data, 'Water Consumption (m3)': water_data,
        'Waste Management (tonnes)': waste_data, 'Greenhouse Gas Emissions (kgCO2e)': ghg_data}
df = pd.DataFrame(data)

# Perform calculations as per GRESB standard
df["Energy Intensity (kWh/m2)"] = df["Energy Consumption (kWh)"]/df["Area"]
df["Water Intensity (m3/m2)"] = df["Water Consumption (m3)"]/df["Area"]
df["Waste Intensity (tonnes/m2)"] = df["Waste Management (tonnes)"]/df["Area"]
df["GHG Intensity (kgCO2e/m2)"] = df["Greenhouse Gas Emissions (kgCO2e)"]/df["Area"]

# Create an Excel Workbook
book = Workbook()
writer = pd.ExcelWriter('GRESB_Environmental_Report.xlsx', engine='openpyxl') 
writer.book = book

# Write the DataFrame to an Excel worksheet
df.to_excel(writer, sheet_name='Environmental Data')

# Save the Excel Workbook
writer.save()
