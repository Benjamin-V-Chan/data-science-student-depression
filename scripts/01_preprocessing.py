import pandas as pd

def preprocess_data(input_path, output_path):
    data = pd.read_csv(input_path)
    data = data.dropna()
    categorical_cols = ['Gender', 'City', 'Profession', 'Dietary Habits', 'Degree', 
                        'Have you ever had suicidal thoughts ?', 'Family History of Mental Illness']
    data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)
    data.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess_data('data/student_depression_dataset.csv', 'data/cleaned_data.csv')