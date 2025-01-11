import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def train_model(input_path, output_folder):
    # Load dataset
    data = pd.read_csv(input_path)
    
    # Features and target
    X = data.drop(columns=['Depression'])
    y = data['Depression']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    with open(f'{output_folder}/classification_report.txt', 'w') as f:
        f.write(report)

if __name__ == "__main__":
    train_model('data/cleaned_data.csv', 'outputs')