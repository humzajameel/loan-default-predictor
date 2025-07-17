# Import required libraries
import pandas as pd                              # For loading and manipulating the dataset
from sklearn.linear_model import LogisticRegression  # Our ML model
from sklearn.model_selection import train_test_split  # For splitting data into train/test sets
import joblib                                     # For saving the trained model

def train_and_save_model():
    # Load the Titanic dataset from a public GitHub URL
    df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
    
    # Select only the columns we want to use for training
    df = df[['Pclass', 'Sex', 'Age', 'Survived']].dropna()  # Drop rows with missing values
    
    # Convert 'Sex' from string to numerical values (0 for male, 1 for female)
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

    # Define input features (X) and target label (y)
    X = df[['Pclass', 'Sex', 'Age']]  # Features for prediction
    y = df['Survived']                # Target: whether the passenger survived or not

    # Split the data into 80% training and 20% testing sets for evaluation
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create and train the logistic regression model using training data
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Save the trained model to a file so it can be reused later
    joblib.dump(model, 'model.joblib')
    print("✅ Model trained on 80% and saved as model.joblib")

# Run the function only if this file is executed directly (not imported)
if __name__ == "__main__":
    train_and_save_model()
