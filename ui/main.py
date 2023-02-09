import streamlit as st
import goes_ui as gu
import nexrad_ui as nu
import nexrad_map as nm
from awscloud.s3 import main as s3

## Library Imports
import pandas as pd
import numpy as mp
import streamlit as st
import datetime
import streamlit as st

def goes_ui():
   
    # Check if 'key' already exists in session_state
    # If not, then initialize it
    if 'key' not in st.session_state:
        st.session_state['key'] = 'value'

    # Session State also supports the attribute based syntax
    if 'key' not in st.session_state:
        st.session_state.key = 'value'

    # Store the initial value of widgets in session state
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False

    # st.title('This is a title')
    st.title('Search By _File_ : :blue[GOES] Data')
    st.sidebar.markdown("# :blue[GOES] Search")
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

    d = st.date_input(
        "Select the date",
        datetime.date(2022, 7, 6))
    st.write('Your Selection is:', d)
    hour = st.selectbox(
        'Select the required Hour',
        list_df)

    st.write('You selected:', hour)

    ## Button code :

    if st.button('Generate the link',key = 'goes_field_search'):
        st.write(' ')
    else:
        st.write('Look at me :::)) ')




    ##############################################################
    st.title('Search By _FileName_ : :blue[GOES] Data')
    st.subheader("Please input your File Name")
    # Text input :

    file_input = st.text_input('File Name','' )


    if file_input:
            st.write("File name entered: ", file_input)
    else:
            st.write('')

    ## Button code :

    if st.button('Generate the link',key = 'goes_file_search'):
        file_name = s3.get_aws_link_by_filename(file_input)
        st.write(file_name)
    else:
        st.write('Look at me :::)) ')

## Library Imports
import pandas as pd
import numpy as mp
import streamlit as st
import datetime

import streamlit as st

def nexrad_ui():

    # Check if 'key' already exists in session_state
    # If not, then initialize it
    if 'key' not in st.session_state:
        st.session_state['key'] = 'value'

    # Session State also supports the attribute based syntax
    if 'key' not in st.session_state:
        st.session_state.key = 'value'

    # Store the initial value of widgets in session state
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False

    # st.title('This is a title')
    st.title('Search By _File_ : :blue[NEXRAD] Data')
    st.sidebar.markdown("# :blue[NexRad] Search")
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

    d = st.date_input(
        "Select the date",
        datetime.date(2022, 7, 6))
    st.write('Your Selection is:', d)


    station = st.selectbox(
        'Select the required Station',
        list_df)

    st.write('You selected:', station)

    ## Button code :

    if st.button('Generate the link',key = 'nexrad_field_search'):
        st.write(' ')
    else:
        st.write('Look at me :::)) ')




    ##############################################################
    st.title('Search your NEXRAD file : :NEXRAD Data')
    st.subheader("Please input your File Name")
    # Text input :

    file_input = st.text_input('File Name','' )


    if file_input:
            st.write("File name entered: ", file_input)
    else:
            st.write('')

    ## Button code :

    if st.button('Generate the link',key = 'nexrad_file_search'):
        st.write(' ')
    else:
        st.write('Look at me :::)) ')


## Imports
import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
from data import Map_data_table_creation as ck
# st.title('This is a title')

def nexrad_map():
    st.markdown("# NexRad Map")
    st.sidebar.markdown("# NexRad Map")
    ### Call the function to pull Map data : 
    conn, cursor = ck.map_data_tbl()

    df = pd.read_sql_query("SELECT * from Mapdata", conn) 
    data = df
    st.subheader("Req data :")
    st.write(df) 

    st.subheader("Graph")
    fig = go.Figure(data=go.Scattergeo(
            locationmode = 'USA-states',
            lon = df['lon'],
            lat = df['lat'],
            text = df['name']+ ',' + df['county'],
            mode = 'markers',
            marker = dict(
                size = 8,
                opacity = 0.8,
                reversescale = True,
                autocolorscale = False,
                symbol = 'square',
                line = dict(
                    width=1,
                    color='rgba(102, 102, 102)'
                ),
                colorscale = 'Blues',
                cmin = 0,
                color = df['elev'].astype(int),
                cmax = df['elev'].astype(int).max(),
                colorbar_title="Elevation"
            )))

    fig.update_layout(
            title = 'NexRad Location Across USA',
            geo = dict(
                scope='usa',
                projection_type='albers usa',
                showland = True,
                landcolor = "rgb(250, 250, 250)",
                subunitcolor = "rgb(217, 217, 217)",
                countrycolor = "rgb(217, 217, 217)",
                countrywidth = 0.5,
                subunitwidth = 0.5
            ),
        )
    # Plot!
    st.plotly_chart(fig, use_container_width=False)
    # Plot!
    st.plotly_chart(fig, use_container_width=False)


page_names_to_funcs = {
    "GOES Search": goes_ui,
    "NexRad Search": nexrad_ui,
    "NexRad Map": nexrad_map,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()