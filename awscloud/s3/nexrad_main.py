# %%
import os
import boto3
import boto3.s3
import botocore
from dotenv import load_dotenv
import re

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
def get_all_nexrad_file_name_by_filter(year, day, date, station):
    files_available = []

    for object_summary in src_bucket.objects.filter(Prefix=f'{year}/{day}/{date}/{station}/'):
        files_available.append(object_summary.key.split('/')[-1])

    return files_available


# %%
def get_nexrad_aws_link(year, day, date, station, filename):
    # Stations, Year, Day, Hour
    copy_source = {
        'Bucket': nexrad_source_bucket,
        'Key': f'{year}/{day}/{date}/{station}/{filename}'
    }

    target_bucket.copy(copy_source, str(year) + '/' + str(day) + '/' + str(date) + '/' + str(station) + '/' + str(filename))

    return f'https://damg7245-team-5.s3.amazonaws.com/{year}/{day}/{date}/{station}/{filename}', f'https://noaa-nexrad-level2.s3.amazonaws.com/{year}/{day}/{date}/{station}/{filename}'


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