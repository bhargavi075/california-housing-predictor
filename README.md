# california-housing-predictor

An end-to-end Machine Learning project that predicts the median house value in California using a Linear Regression model. This project includes data exploration, model training, evaluation, and an interactive web interface built with Streamlit.

## Project Structure
- `task1_ml_linear_regression.ipynb`: Jupyter Notebook containing EDA, data preprocessing, model training, and evaluation.
- `app.py`: Streamlit application file for the web interface.
- `linear_regression_model.pkl`: The trained and serialized Linear Regression model.
- `california_housing.csv`: Dataset used for training and testing.
- `requirements.txt`: Python dependencies required to run the project.

## Model Performance
- **Mean Absolute Error (MAE):** ~0.53 (indicating predictions are off by roughly $53,000 on average)
- **Root Mean Squared Error (RMSE):** ~0.74
- **R-squared ($R^2$):** ~0.57 (explains 57% of the variance in the target variable)

## How to Run the Web App
1. Clone this repository:
   ```bash
   git clone <your-github-repo-link>