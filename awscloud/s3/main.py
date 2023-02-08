# %%
import os
import boto3
import boto3.s3
import botocore
import re
from dotenv import load_dotenv

# %%
load_dotenv()

# %%
goes_source_bucket = 'noaa-goes18'
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
src_bucket = s3.Bucket(goes_source_bucket)
target_bucket = s3.Bucket(team_source_bucket)


# %%
def get_all_geos_file_name_by_filter(station, year, day, hour):
    files_available=[]
    
    for object_summary in src_bucket.objects.filter(Prefix=  f'{station}/{year}/{day}/{hour}/'):
        files_available.append(object_summary.key.split('/')[-1])

    return files_available


# %%
def get_geos_aws_link(station, year, day, hour, filename):
    # Stations, Year, Day, Hour
    copy_source = {
        'Bucket': goes_source_bucket,
        'Key': f'{station}/{year}/{day}/{hour}/{filename}'
    }

    target_bucket.copy(copy_source, station + '/' + str(year) + '/' + day +'/' + hour + '/' + filename)

    return f'https://damg7245-team-5.s3.amazonaws.com/{station}/{year}/{day}/{hour}/{filename}', f'https://noaa-goes18.s3.amazonaws.com/{station}/{year}/{day}/{hour}/{filename}'


def get_aws_link_by_filename(filename):
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
    date = time[8:10]

    #combining all pieces of url
    output = "https://noaa-goes18.s3.amazonaws.com/" + res + '/' + year + '/' + day + '/' + date + '/' + filename
    
    return output