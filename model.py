from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import re

def extract_numerical_size(size_str):
    match = re.match(r'(\d+(\.\d+)?)', str(size_str))
    return float(match.group(1)) if match else 0.0

# Load and preprocess the dataset
df = pd.read_csv('123.csv')

# Use label encoder for the 'Category' column
label_encoder_category = LabelEncoder()
df['Category'] = label_encoder_category.fit_transform(df['Category'])

# Handle missing values using the most frequent strategy
df = df.apply(lambda col: col.fillna(col.mode()[0]))

# Preprocess the 'Size' column
df['Size'] = df['Size'].apply(extract_numerical_size)

# Train the Random Forest model
X = df[['Category', 'Size']]
y = df['Name']
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X, y)

# Collect user input for category and features
user_input_category = input("Enter the category you're interested in: ")
user_input_features = input("Enter the features you're interested in (comma-separated): ")
user_input_size = input("Enter the app's size: ")

# Preprocess user input size
user_input_size = extract_numerical_size(user_input_size)

# Use the trained model to predict the app name for the user's input
user_input_df = pd.DataFrame({'Category': [user_input_category], 'Size': [user_input_size]})
user_input_df['Category'] = label_encoder_category.transform(user_input_df['Category'])

predicted_app_name = rf_classifier.predict(user_input_df)[0]

# Now, you can recommend apps based on the predicted app name
recommended_apps = df[df['Name'] == predicted_app_name]
print(f'Recommended apps with the name "{predicted_app_name}":')
print(recommended_apps)
