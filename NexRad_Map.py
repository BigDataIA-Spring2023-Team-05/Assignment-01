## Imports
import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
# st.title('This is a title')
st.title('A title with _italics_ :blue[colors] and emojis :sunglasses:')
def load_data(nrows):
    data = pd.read_fwf('https://www.ncei.noaa.gov/access/homr/file/nexrad-stations.txt', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data = data.drop(index = 0,axis = 0)
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

df = pd.DataFrame()
df['name']=data['name']
df['county']=data['county']
df['lat'] = data['lat']
df['lon'] = data['lon']
df['elev'] = data['elev']

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
