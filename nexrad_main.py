from awscloud.s3 import nexrad_main as awr

print(awr.get_all_nexrad_file_name_by_filter('2023', '02', '04', 'KABR'))

print(awr.get_nexrad_aws_link_by_filename('KABR20230204_000536_V06'))

print(awr.get_nexrad_aws_link('2023', '02', '04', 'KABR', 'KABR20230204_000536_V06'))