# %%
import awscloud.s3.main as s3
import pytest

# def func(x):
#     return x + 1


# def test_answer():
#     assert func(3) == 5

# %%
def test_generate_geos_link_by_filename_and_parameter():
    assert s3.get_geos_aws_link('ABI-L1b-RadC', 2023, '029', '01', 'OR_ABI-L1b-RadC-M6C01_G18_s20230290131183_e20230290133559_c20230290134003.nc') == ('https://damg7245-team-5.s3.amazonaws.com/ABI-L1b-RadC/2023/029/01/OR_ABI-L1b-RadC-M6C01_G18_s20230290131183_e20230290133559_c20230290134003.nc', 'https://noaa-goes18.s3.amazonaws.com/ABI-L1b-RadC/2023/029/01/OR_ABI-L1b-RadC-M6C01_G18_s20230290131183_e20230290133559_c20230290134003.nc')
# %%
