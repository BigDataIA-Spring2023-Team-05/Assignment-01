## Library Imports
import pandas as pd
import numpy as mp
import streamlit as st


import streamlit as st

# Check if 'key' already exists in session_state
# If not, then initialize it
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports the attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'
# st.title('This is a title')
st.title('Search By _File_ : :blue[GOES] Data')
st.subheader("Please select your Search Criteria")

## Data for the dropdown
data = [10,20,21,22,15,60]
  
# Create the pandas DataFrame with column name is provided explicitly
df = pd.DataFrame(data, columns=['Numbers'])
list_df = df['Numbers'].tolist()

#----------------------------------------------------------
# df = pd.read_csv('data.csv')
# col_one_list = df['one'].tolist()
# selectbox_01 = st.selectbox('Select', col_one_list)
#----------------------------------------------------------
station = st.selectbox(
    'Select the required Station',
    list_df)

st.write('You selected:', station)

year = st.selectbox(
    'Select the required Year',
    list_df)

st.write('You selected:', year)

day = st.selectbox(
    'Select the required Day',
    list_df)

st.write('You selected:', day)

hour = st.selectbox(
    'Select the required Hour',
    list_df)

st.write('You selected:', hour)

## Button code :

if st.button('Generate the link'):
    st.write('EXAMPLE__LINK')
else:
    st.write('Look at me :::)) ')




##############################################################
st.title('Search By _FileName_ : :blue[GOES] Data')
st.subheader("Please input your File Name")
# Text input :

file_input = st.text_input(
        "Enter some text 👇",
         label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )

if file_input:
        st.write("You entered: ", file_input)


