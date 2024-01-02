```python
# Import necessary libraries
import matplotlib.pyplot as plt
from predictive_analytics import PredictiveAnalytics

class Dashboard:
    def __init__(self):
        self.predictive_analytics = PredictiveAnalytics()

    def load_and_process_data(self, file_path):
        """
        Load and preprocess the data
        """
        data = self.predictive_analytics.load_and_process_data(file_path)
        return data

    def split_data(self, data, target_column, test_size=0.2, random_state=42):
        """
        Split the data into training and testing sets
        """
        X_train, X_test, y_train, y_test = self.predictive_analytics.split_data(data, target_column, test_size, random_state)
        return X_train, X_test, y_train, y_test

    def train_and_evaluate_model(self, X_train, X_test, y_train, y_test):
        """
        Train the predictive model and evaluate its performance
        """
        self.predictive_analytics.train_model(X_train, y_train)
        mse, r2 = self.predictive_analytics.evaluate_model(X_test, y_test)
        return mse, r2

    def plot_predictions(self, X_test, y_test):
        """
        Plot the model's predictions against the actual values
        """
        y_pred = self.predictive_analytics.predict(X_test)
        plt.scatter(y_test, y_pred)
        plt.xlabel('Actual Values')
        plt.ylabel('Predicted Values')
        plt.title('Predictive Model Performance')
        plt.show()

    def create_dashboard(self, file_path, target_column):
        """
        Create a dashboard to display the model's performance
        """
        data = self.load_and_process_data(file_path)
        X_train, X_test, y_train, y_test = self.split_data(data, target_column)
        mse, r2 = self.train_and_evaluate_model(X_train, X_test, y_train, y_test)
        print(f'Mean Squared Error: {mse}')
        print(f'R2 Score: {r2}')
        self.plot_predictions(X_test, y_test)
```
