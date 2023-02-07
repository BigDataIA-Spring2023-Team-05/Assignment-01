import awscloud.s3.main as aw


# print(aw.get_all_geos_file_name_by_filter('ABI-L1b-RadC', 2023, '029', '01'))

print(aw.get_geos_aws_link('ABI-L1b-RadC', 2023, '029', '01', 'OR_ABI-L1b-RadC-M6C01_G18_s20230290131183_e20230290133559_c20230290134003.nc'))
