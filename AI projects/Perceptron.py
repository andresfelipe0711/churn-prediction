## Simple Perceptron Implementation in Python

#%%
## Import necessary libraries
import numpy as np

## Define the Perceptron class
class Perceptron:
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        # Initialize weights and bias
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Training the perceptron
        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self._activation_function(linear_output)

                # Update weights and bias
                update = self.lr * (y[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self._activation_function(linear_output)
        return y_predicted

    def _activation_function(self, x):
        return np.where(x >= 0, 1, 0)
## Example usage
if __name__ == "__main__":
    # Sample data (AND logic gate)
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    y = np.array([0, 0, 0, 1])

    # Create Perceptron instance
    p = Perceptron(learning_rate=0.1, n_iters=10)
    p.fit(X, y)

    # Make predictions
    predictions = p.predict(X)
    print("Predictions:", predictions)
    print("Actual labels:", y)
    print("Weights:", p.weights)
    print("Bias:", p.bias)
    

# %%
