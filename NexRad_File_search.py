base_url="https://noaa-nexrad-level2.s3.amazonaws.com/"
# base_url="https://noaa-goes18.s3.amazonaws.com/ABI-L2-BRFF/2022/315/02/OR_ABI-L2-BRFF-M6_G18_s20223150230207_e20223150239515_c20223150241087.nc"


# def get_file_url(filename):
#   timestamp = filename.split('_')[-3].split(".")[0]
#   timestamp

#   file_type = filename.split('_')[1][0:-3]
#   end_name = file_type.split("-")[2]
#   for i in end_name:
#     if i.isnumeric():
#         end_name = end_name.replace(i,"") 

#   file_type = file_type.split("-")[0] + '-' +file_type.split("-")[1] + '-' + end_name
#   # file_type
  
#   year = timestamp[1:5]
#   day_of_the_year = timestamp[5:8]
#   time_of_day = timestamp[8:10]
#   final_url = base_url + file_type + '/' + year + '/' + day_of_the_year + '/' + time_of_day + '/' + filename

#   return final_url

name = 'KCCX20120203_013605_V03.gz'
year  = name.split('_')[0][4:8]
print(year)
month = name.split('_')[0][8:10]
print(month)
day = name.split('_')[0][10:12]
print(day)
loc = name.split('_')[0][0:4]
print(loc)
link = base_url + year + '/' + month +'/'+ day + '/' + loc + '/' + name
print(link)
