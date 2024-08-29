# Iris Flower Classification

This project classifies iris flowers into three species based on their measurements.

## Project Overview

We use machine learning to predict the species of iris flowers (setosa, versicolor, or virginica) using the following measurements:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

## Steps

1. **Load Data**: The dataset contains measurements of 150 iris flowers.
2. **Train Models**: We use different machine learning models.
3. **Evaluate**: We check the accuracy of each model.

## Models and Accuracy

| Model                   | Accuracy |
|-------------------------|----------|
| K-Nearest Neighbors      | 96.67%   |
| Logistic Regression      | 97.50%   |
| Support Vector Machine   | 98.33%   |
| Decision Tree            | 95.00%   |

## Final Model

The **Support Vector Machine (SVM)** gave the best accuracy (98.33%), so it was selected as the final model.

## Required Libraries

- pandas
- numpy
- scikit-learn



## Conclusion

This project helped me learn how to apply machine learning models for classifying data. The SVM model worked best for this task.

## How to Run

1. Clone this repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Run the `classification.py` file to train and evaluate the models.

## Dataset

The dataset is sourced from the [Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris).

## Contact

If you have any questions or suggestions, feel free to reach out!

