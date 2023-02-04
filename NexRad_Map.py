## Imports
import pandas as pd
import numpy as mp
import streamlit as st
# st.title('This is a title')
st.title('A title with _italics_ :blue[colors] and emojis :sunglasses:')
def load_data(nrows):
    data = pd.read_csv('https://www.ncei.noaa.gov/access/homr/file/nexrad-stations.txt', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    # data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
# data = pd.read_csv(nexrad-stations.txt)

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

st.subheader("Raw data pulled")
st.write(data) 