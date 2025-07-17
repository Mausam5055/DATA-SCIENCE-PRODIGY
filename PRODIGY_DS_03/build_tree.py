# Step 1: Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

print("--- Starting the script ---")

# Step 2: Load and Prepare the Data
try:
    # This dataset uses a semicolon separator, so we specify sep=';'
    df = pd.read_csv('bank.csv', sep=';')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'bank.csv' not found. Make sure the file is in the same directory as the script.")
    exit()

# --- Data Preprocessing ---
# The target variable is 'y' (if the client subscribed to a term deposit).
# We need to convert it from 'yes'/'no' to 1/0.
le = LabelEncoder()
df['y'] = le.fit_transform(df['y'])

# Separate the features (X) from the target (y)
X = df.drop('y', axis=1)
y = df['y']

# One-hot encode the categorical features. This converts categories into numbers.
# drop_first=True helps avoid redundancy in the encoded columns.
X_processed = pd.get_dummies(X, drop_first=True)

# --- Split data into training and testing sets ---
# 80% for training, 20% for testing. random_state ensures we get the same split every time.
X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)
print("Data preprocessed and split into training and testing sets.")

# Step 3: Train the Decision Tree Model
# We set max_depth to avoid making the tree too complex (overfitting).
# min_samples_leaf requires a certain number of samples to be in a leaf node.
clf = DecisionTreeClassifier(random_state=42, max_depth=5, min_samples_leaf=10)

# Train the classifier on the training data
clf.fit(X_train, y_train)
print("Model training complete.")

# Step 4: Evaluate the Model
# Make predictions on the test data
y_pred = clf.predict(X_test)

# Calculate and print the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.4f}")

# Display a detailed classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['no', 'yes']))

# Step 5: Display the Decision Tree Rules
# Generate a text representation of the tree
tree_rules = export_text(clf, feature_names=X_processed.columns.tolist())
print("\n--- Decision Tree Rules ---")
print(tree_rules)
print("\n--- Script finished ---")