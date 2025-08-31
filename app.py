import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Boston Housing Price Prediction")

# Load pre-trained model
model_file = "boston_housing.pkl"
try:
    with open(model_file, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error(f"Model file '{model_file}' not found. Please ensure it exists in the project directory.")
    st.stop()
except Exception as e:
    st.error(f"Error loading model: {str(e)}")
    st.stop()

# Input fields using sliders (except CHAS)
st.subheader("Enter Property Details")
crim = st.slider("CRIM: Per capita crime rate", min_value=0.0, max_value=89.0, value=0.1, step=0.1)
zn = st.slider("ZN: Proportion of residential land zoned", min_value=0.0, max_value=100.0, value=0.0, step=1.0)
indus = st.slider("INDUS: Proportion of non-retail business acres", min_value=0.5, max_value=28.0, value=5.0, step=0.1)
chas = st.selectbox("CHAS: Charles River (1 = tract bounds river, 0 = otherwise)", [0, 1], index=0)
nox = st.slider("NOX: Nitric oxides concentration (parts per 10M)", min_value=0.4, max_value=0.9, value=0.5, step=0.01)
rm = st.slider("RM: Average number of rooms per dwelling", min_value=3.5, max_value=8.8, value=6.0, step=0.1)
age = st.slider("AGE: Proportion of units built before 1940", min_value=2.9, max_value=100.0, value=50.0, step=0.1)
dis = st.slider("DIS: Distance to employment centers", min_value=1.0, max_value=12.5, value=4.0, step=0.1)
rad = st.slider("RAD: Accessibility to highways (index)", min_value=1.0, max_value=24.0, value=5.0, step=1.0)
tax = st.slider("TAX: Property tax rate per $10,000", min_value=187.0, max_value=711.0, value=300.0, step=1.0)
ptratio = st.slider("PTRATIO: Pupil-teacher ratio", min_value=12.0, max_value=22.0, value=15.0, step=0.1)
b = st.slider("B: 1000(Bk - 0.63)^2 (proportion of Black residents)", min_value=0.0, max_value=400.0, value=350.0, step=1.0)
lstat = st.slider("LSTAT: % lower-status population", min_value=1.7, max_value=38.0, value=10.0, step=0.1)

# Create user_dict with lowercase feature names
user_dict = {
    'crim': crim,
    'zn': zn,
    'indus': indus,
    'chas': chas,
    'nox': nox,
    'rm': rm,
    'age': age,
    'dis': dis,
    'rad': rad,
    'tax': tax,
    'ptratio': ptratio,
    'b': b,
    'lstat': lstat
}

# Convert to DataFrame
user_df = pd.DataFrame(user_dict, index=[0])

# Predict button
if st.button("Predict"):
    
        # Verify feature names match model's expectations
        expected_features = model.feature_names_in_ if hasattr(model, 'feature_names_in_') else user_dict.keys()
        if not all(f in user_df.columns for f in expected_features):
            st.error(f"Feature mismatch. Expected: {expected_features}, Got: {list(user_df.columns)}")
            st.stop()
        prediction = model.predict(user_df)
        st.success(f"The Predicted price is ${np.round(prediction[0] * 1000, 2)}")
        
if st.checkbox("Show Feature Importance") and hasattr(model, 'feature_importances_'):
    st.subheader("Feature Importance")
    fig, ax = plt.subplots()
    importances = pd.Series(model.feature_importances_, index=user_dict.keys())
    sns.barplot(x=importances, y=importances.index, ax=ax)
    ax.set_title("Feature Importance")
    st.pyplot(fig)