# Machine-Learning-Advance-End-To-End-Iris-Species-Prediction-DecisionTree-Project

# 🚀 Overview
# 🌸 Iris Species Predictor: Decision Tree Analysis
This project implements a robust machine learning solution for the classic Iris flower classification task. It utilizes a Decision Tree Classifier to predict species based on sepal and petal measurements, deployed via a high-performance Streamlit web interface.

.

# 🛠️ Technical Implementation
## Model Architecture: 
A Decision Tree Classifier was selected for its inherent interpretability and ability to handle non-linear relationships without the need for feature scaling.

## Hyperparameter Optimization: 
To prevent overfitting and ensure maximum generalization, I utilized GridSearchCV to tune parameters including criterion (Gini vs. Entropy), max_depth, and splitter.

## Performance: 
The optimized model achieves an impressive accuracy range of 96% to 98%, as validated through confusion matrices and classification reports during the testing phase.

## Deployment: 
The finalized model is serialized as a Pickle file and integrated into a Streamlit dashboard, allowing for real-time inference via interactive hardware-mimicking sliders.

# 📊 Dataset Features
The model evaluates four key morphological attributes to identify the species:
Sepal Length (cm)
Sepal Width (cm)
Petal Length (cm)
Petal Width (cm)
Target Classes: Iris-Setosa, Iris-Versicolour, and Iris-Virginica.





















