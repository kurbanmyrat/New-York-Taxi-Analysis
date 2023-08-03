import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
import random
import joblib


data_for_app = pd.read_csv("data_for_app.csv")
data_for_app = data_for_app.drop(["Unnamed: 0"], axis=1)
data_for_app["PULocationID"] = data_for_app["PULocationID"].astype("str")
data_for_app["amount of precipitation"] = data_for_app["amount of precipitation"].astype("str")
st.write("""
# New York taxi

This app predicts the 


""")

st.sidebar.header("User Input Features")

def user_input_features():
    is_holiday = st.sidebar.selectbox("Holiday", (True, False))
    Borough = st.sidebar.selectbox("Borough",("Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island", "EWR"))
    PULocationID = random.choice(data_for_app.PULocationID.values)
    transaction_month = 1
    transaction_day = st.sidebar.slider("Transaction day", 1, 31, 15)
    transaction_hour = st.sidebar.slider("Transaction Hour", 0, 23, 14)
    temperature = st.sidebar.slider("Temperature", -15.6, 30.6, 0.0)
    humidity = st.sidebar.slider("Humidity", 24.0,100.0,50.0)
    wind_speed = st.sidebar.slider("Wind speed", 0.0,14.0,5.0)
    cloud_cover = st.sidebar.slider("Cloud cover", 0.0,0.1,0.5)
    amount_of_precipitation = random.choice(data_for_app["amount of precipitation"])



    data = {"PULocationID":PULocationID,
            "transaction_month":transaction_month,
            "transaction_day":transaction_day,
            "transaction_hour":transaction_hour,
            "Borough":Borough,
            "temperature":temperature,
            "humidity":humidity,
            "wind speed":wind_speed,
            "cloud cover":cloud_cover,
            "amount of precipitation":amount_of_precipitation,
            "is_holiday":is_holiday}

    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

df = pd.concat([input_df,data_for_app],axis=0)
df = pd.get_dummies(df)
df = df[:1] # Selects only the first row (the user input data)
#df = df.drop(["Unnamed: 0"], axis=1)
st.subheader('User Input features')

st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
st.write(df)

load_clf = pickle.load(open('nyc_taxi_model.pkl', 'rb'))
#loaded_pipeline = joblib.load('pipeline.pkl')
#predictions = loaded_pipeline.predict(df)
prediction = load_clf.predict(df)
#prediction_proba = load_clf.predict_proba(df)


st.subheader('Prediction')

st.write(prediction)

#st.subheader('Prediction Probability')
#st.write(prediction_proba)