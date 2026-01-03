import pandas as pd
from sklearn.linear_model import LinearRegression

# Load CSV
df = pd.read_csv("data/sales_small.csv")

# Encode categorical variables
df['Product'] = df['Product'].map({'Mobile':0, 'Laptop':1})
df['Region'] = df['Region'].map({'Pune':0, 'Mumbai':1})

# Convert Month to numeric
month_map = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5}
df['Month_num'] = df['Month'].map(month_map)

# Features and target
X = df[['Month_num','Product','Region']]
y = df['Sales']

# Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Function to predict sales
def predict_sales(month, product, region):
    month_num = month_map[month]
    product_num = 0 if product=='Mobile' else 1
    region_num = 0 if region=='Pune' else 1
    prediction = model.predict([[month_num, product_num, region_num]])
    return round(prediction[0], 2)
