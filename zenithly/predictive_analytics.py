```python
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

from data_processing import DataProcessor

class PredictiveAnalytics:
    def __init__(self):
        self.data_processor = DataProcessor()
        self.model = LinearRegression()

    def load_and_process_data(self, file_path):
        """
        Load and preprocess the data
        """
        data = self.data_processor.load_data(file_path)
        cleaned_data = self.data_processor.clean_data(data)
        transformed_data = self.data_processor.transform_data(cleaned_data)
        return transformed_data

    def split_data(self, data, target_column, test_size=0.2, random_state=42):
        """
        Split the data into training and testing sets
        """
        X = data.drop(target_column, axis=1)
        y = data[target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        return X_train, X_test, y_train, y_test

    def train_model(self, X_train, y_train):
        """
        Train the predictive model
        """
        self.model.fit(X_train, y_train)

    def evaluate_model(self, X_test, y_test):
        """
        Evaluate the performance of the predictive model
        """
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        return mse, r2

    def predict(self, new_data):
        """
        Use the trained model to make predictions
        """
        prediction = self.model.predict(new_data)
        return prediction
```
