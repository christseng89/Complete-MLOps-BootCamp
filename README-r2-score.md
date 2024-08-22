### What is R² Score?

The R² Score, also known as the coefficient of determination, is a statistical measure that indicates how well a regression model's predictions approximate the actual data points. It provides a measure of how well the independent variables explain the variance in the dependent variable.

- R² Score Range: The R² value ranges from 0 to 1 (or sometimes negative for particularly poor models). 
  - R² = 1: Indicates that the model perfectly predicts the dependent variable (all variance is explained by the independent variables).
  - R² = 0: Indicates that the model does not explain any of the variance in the dependent variable.
  - Negative R²: Indicates that the model performs worse than a horizontal line (mean of the data).

### Formula

 R² = 1 - sum{(y_i - {y}_i)^2}/sum{(y_i - {y})^2}

Where:
- y_i  are the actual values.
- {y}_i  are the predicted values.
- {y}  is the mean of the actual values.

### Example

Let's consider a simple example where we fit a linear regression model to a small dataset.

#### Dataset:

| X | Y (Actual) |
|---|------------|
| 1 | 2          |
| 2 | 4          |
| 3 | 5          |
| 4 | 4          |
| 5 | 5          |

#### Fitting a Linear Regression Model:

Assume we fit a linear regression model, and the predicted values (\(\hat{y}) are as follows:

| X | Y (Actual) | Y (Predicted) |
|---|------------|---------------|
| 1 | 2          | 2.2           |
| 2 | 4          | 3.1           |
| 3 | 5          | 4.0           |
| 4 | 4          | 4.9           |
| 5 | 5          | 5.8           |

#### Calculation of R² Score:

1. Calculate the Total Sum of Squares (TSS):
   - TSS measures the total variance in the actual data.
 
   TSS = sum{(y_i - {y})^2} = (2-4)^2 + (4-4)^2 + (5-4)^2 + (4-4)^2 + (5-4)^2 = 2 + 0 + 1 + 0 + 1 = 4


2. Calculate the Residual Sum of Squares (RSS):
   - RSS measures the variance that the model fails to capture.
 
   RSS = sum{(y_i - {y}_i)^2} = (2-2.2)^2 + (4-3.1)^2 + (5-4.0)^2 + (4-4.9)^2 + (5-5.8)^2 = 0.04 + 0.81 + 1.00 + 0.81 + 0.64 = 3.3


3. Calculate R²:
 
   R² = 1 - {RSS}/{TSS} = 1 - {3.3}/{4} = 1 - 0.825 = 0.175


### Interpretation

In this example, the R² score is 0.175, which indicates that approximately 17.5% of the variance in the dependent variable Y is explained by the model. This suggests that the model does not fit the data particularly well, as it only explains a small portion of the variance. In practice, a higher R² score is generally desired, as it indicates a better fit to the data.
