# Step 1: Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

print("--- Starting the script ---")

# Step 2: Load and Prepare the Data
try:
    # This dataset might use a semicolon separator, so we specify sep=';'
    # If that fails, it will try with a comma.
    try:
        df = pd.read_csv('bank.csv', sep=';')
        # Check if 'deposit' is in the columns, if not, try comma
        if 'deposit' not in df.columns:
            df = pd.read_csv('bank.csv')
    except Exception:
        df = pd.read_csv('bank.csv')

    print("Dataset loaded successfully.")
    print("Columns found:", df.columns.tolist())

except FileNotFoundError:
    print("Error: 'bank.csv' not found. Make sure the file is in the same directory as the script.")
    exit()

# --- Data Preprocessing ---
# The target variable is 'deposit' (if the client subscribed).
# We need to convert it from 'yes'/'no' to 1/0.
le = LabelEncoder()
df['deposit'] = le.fit_transform(df['deposit']) # <-- CHANGED 'y' to 'deposit'

# Separate the features (X) from the target (deposit)
X = df.drop('deposit', axis=1) # <-- CHANGED 'y' to 'deposit'
y = df['deposit']             # <-- CHANGED 'y' to 'deposit'

# One-hot encode the categorical features. This converts categories into numbers.
X_processed = pd.get_dummies(X, drop_first=True)

# --- Split data into training and testing sets ---
X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)
print("Data preprocessed and split into training and testing sets.")

# Step 3: Train the Decision Tree Model
clf = DecisionTreeClassifier(random_state=42, max_depth=5, min_samples_leaf=10)

# Train the classifier on the training data
clf.fit(X_train, y_train)
print("Model training complete.")

# Step 4: Evaluate the Model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.4f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['no', 'yes']))

# Step 5: Display the Decision Tree Rules
tree_rules = export_text(clf, feature_names=X_processed.columns.tolist())
print("\n--- Decision Tree Rules ---")
print(tree_rules)
print("\n--- Script finished ---")