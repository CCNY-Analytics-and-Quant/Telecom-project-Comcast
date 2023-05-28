import pandas as pd

import matplotlib.pyplot as mpt
import numpy as np

# Importing data
pd.read_csv('Telecom_data.csv')
df = pd.read_csv('Telecom_data.csv')

# Looking at data
df

# Check for duplicate columns and make sure to erase them
print(df.duplicated().sum())

# Checking for null values
df.isna().sum()

# The column 'offer' had a lot of null values
print(df['Offer'])

# Checking the data types of the columns to see if they are being registered correctly
df.dtypes

# Replace null values with "Unknown" (Categorical)
df['Churn_Category'].fillna('Unknown', inplace=True)
df['Churn_Reason'].fillna('Unknown', inplace=True)
df['Internet_Type'].fillna('Unknown', inplace=True)

# Replace null values with "0" (Numerical)
df['Avg_Monthly_Long_Distance_Charges'].fillna(round(df['Avg_Monthly_Long_Distance_Charges'].mean(), 0), inplace=True)
df['Multiple_Lines'].fillna(round(df['Multiple_Lines'].mean(), 0), inplace=True)
df['Avg_Monthly_GB_Download'].fillna(round(df['Avg_Monthly_GB_Download'].mean(), 0), inplace=True)
df['Online_Security'].fillna(round(df['Online_Security'].mean(), 0), inplace=True)
df['Online_Backup'].fillna(round(df['Online_Backup'].mean(), 0), inplace=True)
df['Device_Protection_Plan'].fillna(round(df['Device_Protection_Plan'].mean(), 0), inplace=True)
df['Premium_Tech_Support'].fillna(round(df['Premium_Tech_Support'].mean(), 0), inplace=True)
df['Streaming_TV'].fillna(round(df['Streaming_TV'].mean(), 0), inplace=True)
df['Streaming_Movies'].fillna(round(df['Streaming_Movies'].mean(), 0), inplace=True)
df['Streaming_Music'].fillna(round(df['Streaming_Music'].mean(), 0), inplace=True)
df['Unlimited_Data'].fillna(round(df['Unlimited_Data'].mean(), 0), inplace=True)

# Show sample data
df.sample(100)

# Data is now clean and we will begin analysis and manipulation
mpt.scatter(df['Total_Revenue'], df['Churn_Category'])
mpt.xlabel('Total Revenue')
mpt.ylabel('Churn category')
mpt.show()

CHU = df[~df['Churn_Category'].str.contains('Unknown')]
CHI = df[~df['Churn_Reason'].str.contains('Unknown')]

churn_reason_counts = df['Churn_Reason'].value_counts()

mpt.figure(figsize=(10, 6))
churn_reason_counts.plot(kind='bar')
mpt.title('Churn Causes')
mpt.xlabel('Churn Reason')
mpt.ylabel('Customer')
mpt.show()

services = df[['Online_Security', 'Online_Backup', 'Device_Protection_Plan',
               'Premium_Tech_Support', 'Streaming_TV', 'Streaming_Movies',
               'Unlimited_Data', 'Churn_Category', 'Internet_Service', 'Phone_Service']]

churn_counts = services.groupby('Churn_Category').sum()

churn_counts.plot(kind='bar', figsize=(10, 6))
mpt.xlabel('Churn Category')
mpt.ylabel('Customer')
mpt.title('Churn Count by Service')
mpt.show()

churned_customers = df[df['Customer_Status'] == 'Churned']

offer_counts = churned_customers['Offer'].value_counts()

mpt.figure(figsize=(8, 6))
mpt.title('Customer Churn using Offers')
mpt.xlabel('Offer')
mpt.ylabel('Customer Sum')
offer_counts.plot(kind='bar')
mpt.show()

internet = df[['Internet_Type', 'Churn_Category']]

# Calculate the churn counts by internet type
churn_counts = internet['Internet_Type'].value_counts()

# Plot the churn counts for each internet type
mpt.bar(churn_counts.index, churn_counts.values)
mpt.xlabel('Internet Type')
mpt.ylabel('Customer')
mpt.title('Churn by Internet Type')
mpt.show()

payment_time = df[['Contract', 'Churn_Category']]

contract_counts = payment_time['Contract'].value_counts()

mpt.bar(contract_counts.index, contract_counts.values)
mpt.xlabel('Contract Type')
mpt.ylabel('Churn Count')
mpt.title('Churn Count by Contract Type')
mpt.xticks(rotation=0)
mpt.show()

# Competitor had better devices and made better offer are the reasons for Churn
mpt.scatter(df['Total_Revenue'], df['Churn_Reason'])
mpt.xlabel('Total Revenue')
mpt.ylabel('Churn reason')
mpt.show()

mpt.scatter(df['Total_Refunds'], df['Churn_Reason'])
mpt.xlabel('Customer')
mpt.ylabel('Offer')
mpt.show()

age_reason = df.groupby('Age')['Churn_Reason'].value_counts().unstack()

df.hist('Age', 'Customer_Status')

# Save the cleaned dataset
df.to_csv("Telecom_Data_cleaned.csv", index=False)