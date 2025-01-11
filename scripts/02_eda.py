import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def perform_eda(input_path, output_folder):
    # Load dataset
    data = pd.read_csv(input_path)
    
    # Summary statistics
    summary = data.describe()
    summary.to_csv(f'{output_folder}/summary_statistics.csv')
    
    # Visualize distributions
    sns.histplot(data['Age'], kde=True)
    plt.title('Age Distribution')
    plt.savefig(f'{output_folder}/age_distribution.png')
    plt.clf()
    
    # Correlation heatmap
    corr = data.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Feature Correlations')
    plt.savefig(f'{output_folder}/correlation_heatmap.png')
    plt.clf()

if __name__ == "__main__":
    perform_eda('data/cleaned_data.csv', 'outputs')