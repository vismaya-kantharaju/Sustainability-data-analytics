# Project Portfolio: Leveraging Data science and Visualization for Sustainability Investigating and reporting 

## Introduction
- Environmental, Social, and Governance (ESG) investing is gaining traction in the financial world, with socially conscious investors seeking to align their investments with their values. However, there's a lack of standardized measures and a credibility gap for evaluating companies' performance in ESG areas. This project addresses this challenge by leveraging data analytics and machine learning techniques to provide transparent ESG assessments.

- It connects to databases, retrieves data on 4 major parameters like downstream transportation, electricity usage, total solid waste, and ambient temperature calculates the carbon emissions, performs analysis, and visualizes results, aiding in informed investment decisions aligned with ethical values using machine learning techniques with forecasting and anomaly detection.
  
## Technology Introduced
- **SQL Database:** Utilizes SQLite for local storage and MySQL for remote data retrieval.
- **Time series indexing:** Utilizes numpy, pandas which Normalize data, organizes time series, estimates carbon emissions, performs statistical analysis 
- **Machine Learning Models:** Implements SARIMAX for time series forecasting and Isolation Forest for anomaly detection.
- **Data Visualization:** Utilizes Plotly for interactive, aesthetically pleasing visualizations.
- **SMTP:** Sends email notifications using smtplib.
  
## Software Requirement Specifications

### Software Interfaces
- **Database Libraries:** sqlite3, mysql.connector.
- **Data Manipulation Libraries:** pandas, matplotlib, Plotly.
- **Command-Line Interface (CLI):** Text-based interaction.
- **Anomaly Detection Interface:** pyod.models.iforest.
- **Forecasting Interface:** statsmodels.tsa.statespace.sarimax.
- **Visualization Interfaces:** plotly.graph_objects .
-  **Email notification**:  smtplib, MIMEText, MIMEMultipart.

### Communication Interfaces
- **HTTP:** Connects to remote MySQL database on the EC2 instance on AWS through MQTT broker.
- **SMTP:** Sends email notifications.


## Implementation
- **Selection of  local or remote database** : based on the requirements option to choose between the two databases based on real-time or non-real-time updates.
  
- **local database** :
  
    ### preprocessing module
    - Data for 4 parameters (electricity consumed, solid-waste generated, downstream transportation, ambient temperature) is extracted from the SQLite database 
        which is recorded for a year and stored locally.
    - Each parameter has different sources, electricity consumed :('HVAC', 'Lighting', 'Appliances & Equipment', 'Elevators & Escalators') , solid-waste generated : ('Office Paper Waste', 'Organic Waste', 
      'Electronic Waste', 'Construction Waste', 'NON-Recyclable Waste')  , downstream transportation: ('Supply Chain', 'Flights', 'Logistics & Delivery Trucks')
    - Data is cleaned, and normalized. Total carbon emission is calculated using the respective carbon offset values.
    - The data is classified as offset and embodied carbon , also w.r.t different scopes of emission.
    - variation of ambient temperature w.r.t electricity consumed using statistical analysis is done.
    
     ### Machine learning module 
    - outliers are detected using the anomaly detection module and the data is forecasted for the next month using the forecasting module.
      
     ### visualization module
    - the visualization is divided into a high-level overview, manager-level view, and employee view to give policy-based suggestions

- **Remote database**:

     ### preprocessing module
    - Data for electricity consumed is extracted from the MySql database from the EC2 instance.
     - this data is tracked in real-time from a simulator that represents a real-estate environment and stored in the database via MQTT broker
    - the electricity data is cleaned and normalized and carbon emission is calculated from its carbon offset values, an option is given to the user to enter the 
       carbon offset value
    - if the carbon emission reaches a certain level a notification is sent to the recipient.
    
     ### visualization module
     - the visualization is created using matplotlib to track the changes in real time.

## Conclusion
This project bridges the gap in ESG reporting by leveraging advanced data analytics and AI techniques. Providing transparent and real-time assessments of companies' ESG performance empowers socially conscious investors to make informed decisions aligned with their values.




