# High School Graduation Prediction Project
## Overview

This project is designed to analyze factors influencing high school graduation rates using student data, including course grades, yearly absences, and state testing scores. The code utilizes machine learning techniques to predict whether a student is likely to graduate based on these factors.

## Usage Instructions
### Prerequisites
Before running the notebook, ensure that you have the following installed:
* Python 3.x
* Jupyter Notebook
* Required Python libraries (install using the command below if necessary):

`pip install pandas numpy scikit-learn matplotlib seaborn`

## Running the Notebook
1. Open the Jupyter Notebook environment:

`jupyter notebook`

2. Load the `Plymouth-Graduation-Project-Final-Clean_020325.ipynb` file.

3. The notebook is structured into the following sections:
* **Data Import & Preprocessing**: Loads the dataset (not included for privacy reasons) and cleans the data.
* **Exploratory Data Analysis (EDA)**: Visualizes key trends and distributions in student performance.
* **Feature Engineering**: Transforms raw data into meaningful features for modeling.
* **Model Training & Evaluation**: Trains a machine learning model (likely a Random Forest) to predict graduation likelihood.
* **Feature Importance Analysis**: Identifies the most influential factors affecting graduation.
* **Model Interpretation & Conclusions**: Summarizes findings and insights from the model.

## Notes on Data Privacy
The dataset is not included in this repository to protect student privacy. If you have access to the appropriate dataset, ensure that it is formatted correctly before running the notebook.

## Summary of Code
The core components of the project include:
* **Data Cleaning**: Handling missing values, encoding categorical features, and standardizing numerical data.
* **Data Visualization**: Generating histograms, bar charts, and pairwise plots to explore data relationships.
* **Machine Learning Model**: Implementing and training a Random Forest classifier to predict student graduation outcomes.
* **Feature Importance Analysis**: Using SHAP values and feature importance scores to explain model predictions.

## Future Improvements
* **Hyperparameter Tuning**: Optimizing model parameters for better performance.
* **Additional Data Sources**: Incorporating socioeconomic or behavioral data for improved predictions.
* **Model Deployment**: Creating a web app or dashboard to make predictions accessible to educators.

## Contact Information

For questions or collaboration opportunities, please email me at [mitchell.yenkastoff@gmail.com](mailto:mitchell.yenkastoff@gmail.com).
