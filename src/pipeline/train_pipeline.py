import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load your dataset
data = pd.read_csv('notebook/StudentsPerformance.csv')
X = data.drop(columns='target_column')
y = data['target_column']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
with open('artifacts/model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Optionally, save a preprocessor (e.g., StandardScaler)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

with open('artifacts/preprocessor.pkl', 'wb') as f:
    pickle.dump(scaler, f)
