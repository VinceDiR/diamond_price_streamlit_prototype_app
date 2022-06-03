import xgboost as xgb
import streamlit as st


#Loading up the Regression model we created
model = xgb.XGBRegressor()
model.load_model('xgb_model.json')

#Caching the model for faster loading
@st.cache

def predict(carat, cut, color, clarity, depth, table, price, x, y, z):

    