# %%
import os
import boto3
import boto3.s3
import botocore
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
def get_all_files_name_by_filter(station, year, day, hour):
    files_available=[]
    
    for object_summary in src_bucket.objects.filter(Prefix=  station + '/' + str(year) + '/' + day +'/' + hour + '/'):
        files_available.append(object_summary.key.split('/')[-1])

    return files_available


# %%
def get_all_aws_link(station, year, day, hour, filename):
    # Stations, Year, Day, Hour
    copy_source = {
        'Bucket': goes_source_bucket,
        'Key': station + '/' + str(year) + '/' + day +'/' + hour + '/' + filename
    }

    target_bucket.copy(copy_source, station + '/' + str(year) + '/' + day +'/' + hour + '/' + filename)

    return f'https://damg7245-team-5.s3.amazonaws.com/{station}/{year}/{day}/{hour}/{filename}'

