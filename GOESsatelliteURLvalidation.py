# #unit test cases for GOES satellite dataset
# # The filenames of the data are formatted as follows:
# # SEVIR_<IMG_TYPE>_<EVENT_TYPE>_<YEAR>_<START>_<END>.h5
# #filename_1 = "OR_ABI-L2-BRFF-M6_G18_s20223150230207_e20223150239515_c20223150241087.nc"
# #filename_2 = 'OR_ABI-L1b-RadM1-M6C01_G18_s20230030201252_e20230030201311_c20230030201340.nc'

import unittest
import re
import streamlit as st
import sqlite3 as sql


def get_aws_file_url(base_url, filename):
    y = filename.split('_')
    # print(y)
    filename_pattern = r'(.*)-(.*)'
    regex_pattern = re.compile(filename_pattern)
    res_fn = regex_pattern.findall(y[1])
    res = str(res_fn[0][0])
    end = res[-1]
    if end.isnumeric():
        res = res[:-1]
    # print(res)
    # get timestamp
    time = y[3]
    year = time[1:5]
    day = time[5:8]
    hour = time[8:10]
    # combining all pieces of url
    output = base_url + res + '/' + year + '/' + day + '/' + hour + '/' + filename
    return output


def main():
    st.title("Dataset Explorer")
    st.subheader("Data Science project with Streamlit")
    html_temp = """
        <div style="background-color:tomato;"><p>Choose dataset you wish to Explore</p></div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    options = st.selectbox('GOES or NEXRAD?', ('GOES', 'NEXRAD'))
    st.write('You selected:', options)
    filename = ''

    if options == 'GOES':
        st.write('happy exploring GOES satellite data!')
        st.write('please entire the file name in the text input box below')
        filename = st.text_input('please entire the file name in the text input box below:',
                                 'OR_ABI-L1b-RadM1-M6C01_G18_s20230030201252_e20230030201311_c20230030201340.nc')
    else:
        st.write('happy exploring NEXGRAD satellite data!')

    return filename


def db_env_create():
    # create sql lite 3 database
    conn = sql.connect('GOESmetadata.db')
    cursor = conn.cursor()
    cursor.execute('''DROP TABLE IF EXISTS GOESmetadataTable''')
    cursor.execute(''' CREATE TABLE GOESmetadataTable (
             year INTEGER NOT NULL, 
             day INTEGER NOT NULL, 
             hour INTEGER NOT NULL
             ); ''')
    return conn, cursor

def insert_data_in_table(cursor, year, day, hour):
    insert_str = "INSERT INTO GOESmetadataTable(year,day,hour) \
        VALUES ('" + year + "','" + day + "','" + hour + "'); "
    cursor.execute(insert_str)


def take_input_from_user():
    year = st.text_input('Year:', '')
    day = st.text_input('Day:', '')
    hour = st.text_input('Hour:', '')

    return year, day, hour

def print_data_from_sql(cursor):
    select = cursor.execute("SELECT year, day, hour FROM GOESmetadataTable limit 5")
    for row in select:
        print("YEAR=", row[0], "DAY=", row[1], "HOUR=", row[2])

def db_conn_close(conn):
    conn.commit()
    print('Data entered successfully.')
    conn.close()
    if (conn):
        conn.close()
        print("The SQLite connection is closed.")

# declarations
base_url = "https://noaa-goes18.s3.amazonaws.com/"
# create table in database
conn, cursor = db_env_create()
filename1 = main()
x = get_aws_file_url(base_url, filename1)
st.write('Click on the link below to download this file!')
st.write(x)
print()
print()
st.write('test case 2: take metadata input from file')
year, day, hour = take_input_from_user()
#add metadata into sqlite3
insert_data_in_table(cursor, year, day, hour)
#print data on console from sql db
print_data_from_sql(cursor)
#stop
db_conn_close(conn)

# test_files = ['OR_ABI-L1b-RadC-M6C01_G18_s20230020101172_e20230020103548_c20230020103594.nc',
#              'OR_ABI-L2-ACMM1-M6_G18_s20230090504262_e20230090504319_c20230090505026.nc',
#              'OR_ABI-L2-ACTPM1-M6_G18_s20230090408262_e20230090408319_c20230090409174.nc',
#              'OR_ABI-L2-DSIM1-M6_G18_s20230110608251_e20230110608308_c20230110609126.nc',
#              'OR_ABI-L2-ACHTM1-M6_G18_s20223560805242_e20223560805300_c20223560806526.nc',
#              'OR_ABI-L2-BRFF-M6_G18_s20223150230207_e20223150239515_c20223150241087.nc',
#              'OR_ABI-L2-ADPM2-M6_G18_s20230061310557_e20230061311015_c20230061311402.nc',
#              'OR_ABI-L1b-RadM1-M6C01_G18_s20230030201252_e20230030201311_c20230030201340.nc',
#              'OR_ABI-L2-ACHTF-M6_G18_s20223532240210_e20223532249518_c20223532252164.nc',
#              'OR_ABI-L2-DSRC-M6_G18_s20223180501179_e20223180503552_c20223180508262.nc',
#              'OR_ABI-L2-DMWVM1-M6C08_G18_s20223552050271_e20223552050328_c20223552122197.nc',
#              'OR_ABI-L2-ACMC-M6_G18_s20222800931164_e20222800933537_c20222800934574.nc',
#              'OR_ABI-L2-DMWC-M6C07_G18_s20223510516174_e20223510518559_c20223510527449.nc']

# if __name__ == 'main':

# for i in test_files:
#     print(TestGOESSatelliteLink.get_awsfile_url(base_url, i))
