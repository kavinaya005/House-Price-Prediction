# -*- coding: utf-8 -*-

"""Created on Tue Dec 10 10:52:12 2024

@author: kavin"""


# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from joblib import dump, load
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, confusion_matrix, accuracy_score, classification_report

# Step 1: Data Selection and Preprocessing
df = pd.read_csv('house_price_regression_dataset.csv')
print(df.head())

# Visualize missing values
sns.heatmap(df.isnull(), cmap='viridis', cbar=False)
plt.title('Missing Values')
plt.show()

# Splitting data into features (X) and target (y)
X = df.drop(['House_Price'], axis=1)
y = df['House_Price']

# Step 2: Splitting the data (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Training the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
dump(model, 'house_price_model.joblib')
print("Model saved as 'house_price_model.joblib'")

# Step 4: Model Evaluation
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = model.score(X_test, y_test)

print(f'MAE: {mae}')
print(f'MSE: {mse}')
print(f'R²: {r2}')



# Plot Actual vs Predicted values
plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--', linewidth=2)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted Home Values')
plt.grid()
plt.show()

correlation_matrix = df.corr()

# Print correlation matrix (optional)
print("Correlation Matrix:")
print(correlation_matrix)

# Plotting the correlation matrix as a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()

# Step 5: Classify Prices and Generate Confusion Matrix
# Categorizing house prices into 'Low', 'Medium', 'High'
bins = [0, 200000, 500000, float('inf')]
labels = ['Low', 'Medium', 'High']
y_test_classes = pd.cut(y_test, bins=bins, labels=labels)
y_pred_classes = pd.cut(y_pred, bins=bins, labels=labels)

# Generate confusion matrix
cm = confusion_matrix(y_test_classes, y_pred_classes, labels=labels)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels)
plt.title("Confusion Matrix")
plt.xlabel("Predicted Classes")
plt.ylabel("Actual Classes")
plt.show()

# Display accuracy and classification report
accuracy = accuracy_score(y_test_classes, y_pred_classes)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:")
print(classification_report(y_test_classes, y_pred_classes, target_names=labels))

# Scatter Plot: Square Footage vs. House Price
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Square_Footage', y='House_Price', color='blue', alpha=0.6)
plt.title('Square Footage vs. House Price')
plt.xlabel('Square Footage')
plt.ylabel('House Price')
plt.grid()
plt.show()

# Step 6: Load Model and Make Predictions at Runtime
from joblib import dump

# Save the trained model to a .joblib file
dump(model, 'house_price_model.joblib')
print("Model saved as 'house_price_model.joblib'")


# Load the trained model from the .joblib file
def load_model(file_path):
    try:
        model = load(file_path)
        print(f"Model loaded successfully from {file_path}")
        return model
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None


    """Loads a saved model from a file."""
    try:
        model = load(file_path)
        print(f"Model loaded successfully from '{file_path}'")
        return model
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def predict_house_price(loaded_model):
    """Accepts user inputs and predicts house prices using the loaded model."""
    if loaded_model is None:
        print("Model not loaded. Exiting.")
        return
    
    try:
        print("\nEnter the house details for prediction:")
        Square_Footage = float(input("Enter square footage: "))
        Num_Bedrooms = int(input("Enter number of bedrooms: "))
        Num_Bathrooms = int(input("Enter number of bathrooms: "))
        Year_Built = int(input("Enter the year built: "))
        Lot_Size = float(input("Enter lot size (in acres): "))
        Garage_Size = float(input("Enter garage size (in square feet): "))
        Neighborhood_Quality = int(input("Enter neighborhood quality (1-10 scale): "))
    except ValueError:
        print("Invalid input. Please enter correct data types.")
        return

    # Create a DataFrame for the input
    new_data = pd.DataFrame({
        'Square_Footage': [Square_Footage],
        'Num_Bedrooms': [Num_Bedrooms],
        'Num_Bathrooms': [Num_Bathrooms],
        'Year_Built': [Year_Built],
        'Lot_Size': [Lot_Size],
        'Garage_Size': [Garage_Size],
        'Neighborhood_Quality': [Neighborhood_Quality]
    })

    # Predict the price
    try:
        predicted_price = loaded_model.predict(new_data)
        print(f"Predicted House Price: $ {predicted_price[0]:,.2f}")
    except Exception as e:
        print(f"An error occurred during prediction: {e}")

# Main execution
if __name__ == "__main__":
    model_path = 'house_price_model.joblib'
    loaded_model = load_model(model_path)
    predict_house_price(loaded_model)


'''# Save the trained model to a .joblib file
dump(model, 'house_price_model.joblib')
print("Model saved as 'house_price_model.joblib'")

import pandas as pd

# Load the trained model from the .joblib file
def load_model(file_path):
    try:
        model = load(file_path)
        print(f"Model loaded successfully from {file_path}")
        return model
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

# Predict house price based on user inputs
def predict_house_price(loaded_model):
    if loaded_model is None:
        print("Model not loaded. Exiting.")
        return
    
    print("Enter the house details for prediction:")
    try:
        Square_Footage = float(input("Enter square footage: "))
        Num_Bedrooms = int(input("Enter number of bedrooms: "))
        Num_Bathrooms = int(input("Enter number of bathrooms: "))
        Year_Built = int(input("Enter the year built: "))
        Lot_Size = float(input("Enter lot size (in acres): "))
        Garage_Size = float(input("Enter garage size (in square feet): "))
        Neighborhood_Quality = int(input("Enter neighbourhood quality (1-10 scale): "))
    except ValueError:
        print("Invalid input. Please enter the correct data types.")
        return

    # Create a DataFrame for the input
    new_data = pd.DataFrame({
        'Square_Footage': [Square_Footage],
        'Num_Bedrooms': [Num_Bedrooms],
        'Num_Bathrooms': [Num_Bathrooms],
        'Year_Built': [Year_Built],
        'Lot_Size': [Lot_Size],
        'Garage_Size': [Garage_Size],
        'Neighborhood_Quality': [Neighborhood_Quality]
    })

    # Predict using the loaded model
    try:
        predicted_price = loaded_model.predict(new_data)
        print(f"Predicted House Price: Rs {predicted_price[0]:,.2f}")
    except Exception as e:
        print(f"An error occurred during prediction: {e}")

# Main execution
if __name__ == "_main_":
    # Specify the saved model file path
    model_file_path = 'house_price_model.joblib'

    # Load the model
    loaded_model = load_model(model_file_path)

    # Predict house price
    predict_house_price(loaded_model)'''    