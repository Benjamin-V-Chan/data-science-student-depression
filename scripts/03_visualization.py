import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_visualizations(input_path, output_folder):
    # Load dataset
    data = pd.read_csv(input_path)
    
    # Depression by Gender
    sns.countplot(x='Depression', hue='Gender_Male', data=data)
    plt.title('Depression by Gender')
    plt.savefig(f'{output_folder}/depression_by_gender.png')
    plt.clf()
    
    # Sleep Duration vs Depression
    sns.boxplot(x='Depression', y='Work/Study Hours', data=data)
    plt.title('Work/Study Hours vs Depression')
    plt.savefig(f'{output_folder}/work_study_hours_vs_depression.png')
    plt.clf()

if __name__ == "__main__":
    create_visualizations('data/cleaned_data.csv', 'outputs')