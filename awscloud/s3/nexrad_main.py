# %%
import os
import boto3
import boto3.s3
import botocore
from dotenv import load_dotenv
import re
from data.sql_aws_metadata import Metadata

# %%
load_dotenv()

# %%
nexrad_source_bucket = 'noaa-nexrad-level2'
team_source_bucket = os.environ.get('TARGET_BUCKET_NAME')

# %%
session = boto3.Session(
    region_name='us-east-1',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.environ.get('AWS_ACCESS_KEY_SECRET')
)

# %%
s3 = session.resource('s3')

# %%
src_bucket = s3.Bucket(nexrad_source_bucket)
target_bucket = s3.Bucket(team_source_bucket)


# %%
def get_all_nexrad_file_name_by_filter(year, month, day, station):
    files_available = []

    for object_summary in src_bucket.objects.filter(Prefix=f'{year}/{month}/{day}/{station}/'):
        files_available.append(object_summary.key.split('/')[-1])

    return files_available


# %%
def get_nexrad_aws_link(year, month, day, station_id, filename):
    # Stations, Year, Day, Hour
    copy_source = {
        'Bucket': nexrad_source_bucket,
        'Key': f'{year}/{month}/{day}/{station_id}/{filename}'
    }

    target_bucket.copy(copy_source, str(year) + '/' + str(month) + '/' + str(day) + '/' + str(station_id) + '/' + str(filename))

    metadata = Metadata()
    metadata.insert_data_into_nexrad(station_id=station_id, year=year, month=month, day_of_year=day)

    return f'https://damg7245-team-5.s3.amazonaws.com/{year}/{month}/{day}/{station_id}/{filename}', f'https://noaa-nexrad-level2.s3.amazonaws.com/{year}/{month}/{day}/{station_id}/{filename}'


def get_nexrad_aws_link_by_filename(filename):
    y = filename.split('_')[0]
    # print(y)
    res = y[:4]
    year = y[4:8]
    day = y[8:10]
    date = y[10:12]
    # print(res, year, day, date)

    # combining all pieces of url
    output = "https://noaa-nexrad-level2.s3.amazonaws.com/" + year + '/' + day + '/' + date + '/' + res + '/' + filename

    return output