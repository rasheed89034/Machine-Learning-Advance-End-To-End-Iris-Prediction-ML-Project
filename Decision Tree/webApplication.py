import streamlit as st
import pickle
import numpy as np

# Load the model
@st.cache_resource
def getModel():
    with open('Models/irisModel.pkl','rb') as f:
        return pickle.load(f)

model = getModel()

st.title("🌸 Iris Species Predictor")
st.markdown("Adjust the sliders below to predict the type of Iris flower.")

sepalLength = st.slider("Sepal Length (cm)",4.0,8.0,5.1,0.1)
sepalWidth = st.slider("Sepal Width (cm)",2.0,4.5,3.5,0.1)
petalLength = st.slider("Petal Length(cm)",1.0,7.0,1.4,0.1)
petalWidth = st.slider("Petal Width(cm)",0.1,2.5,0.2,0.1)

# 3. Prediction Logic
if st.button("Predict Species"):
    inputFeatures = np.array([[sepalLength,sepalWidth,petalLength,petalWidth]])

    prediction = model.predict(inputFeatures)

    # Map the numeric output to species names
    species_map = {0: "Setosa", 1: "Versicolour", 2: "Virginica"}
    result = species_map[prediction[0]]

    st.success(f"The model predicts this is an **Iris-{result}**!")