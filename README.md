# data-science-student-depression

## Project Overview
This project analyzes a dataset on student depression to uncover potential correlations and trends. The analysis includes data preprocessing, exploratory data analysis (EDA), visualization of key relationships, and building a predictive model to identify students at risk of depression. The goal is to provide insights into factors that contribute to mental health challenges among students.

## Folder Structure
```
project/
├── data/
│   ├── Student Depression Dataset.csv  # Original dataset
│   ├── cleaned_data.csv                # Processed dataset
├── scripts/
│   ├── 01_preprocessing.py             # Data preprocessing script
│   ├── 02_eda.py                       # EDA script
│   ├── 03_visualization.py             # Visualization script
│   ├── 04_modeling.py                  # Predictive modeling script
├── outputs/
│   ├── summary_statistics.csv          # Summary statistics from EDA
│   ├── age_distribution.png            # Age distribution visualization
│   ├── correlation_heatmap.png         # Correlation heatmap
│   ├── depression_by_gender.png        # Visualization of depression by gender
│   ├── work_study_hours_vs_depression.png  # Visualization of work/study hours vs depression
│   ├── classification_report.txt       # Model evaluation results
```

## Usage
1. Clone the repository and navigate to the project directory.
2. Place the dataset in the `data/` folder.
3. Run the scripts in sequence:
   - `python scripts/01_preprocessing.py` to preprocess the dataset.
   - `python scripts/02_eda.py` to perform exploratory data analysis.
   - `python scripts/03_visualization.py` to generate visualizations.
   - `python scripts/04_modeling.py` to train and evaluate a predictive model.
4. Outputs will be saved in the `outputs/` folder.

## Requirements
- Python 3.7 or later
- Required Python packages (install via `pip install -r requirements.txt`):
  - pandas
  - seaborn
  - matplotlib
  - scikit-learn

## Acknowledgments
- **Dataset Author:** Shodolamu Opeyemi
- **Source:** [Kaggle - Student Depression Dataset](https://www.kaggle.com/datasets/hopesb/student-depression-dataset)

This dataset and analysis aim to contribute to understanding and addressing mental health issues among students.
