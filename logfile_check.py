import datetime,time
current_timestamp = datetime.datetime.now()
current_timestamp_mili = current_timestamp.timestamp()*1000
#print('Current date and time ->', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
with open('application.log','r') as fread:
    all_lines=fread.readlines()
    #print(all_lines)
line_list=[]
for line in all_lines:
    line_list=line.split('=>')
    log_timestamp=line_list[0]
    date_time_obj = datetime.datetime.strptime(log_timestamp, '%Y-%m-%d %H:%M:%S')
    date_time_obj_mili = date_time_obj.timestamp()*1000
    #print(date_time_obj_mili)
    if (current_timestamp_mili - date_time_obj_mili < 86400000):
        if 'ERROR' in line or 'FAIL' in line:
            print(line)
#datetime_str = '09/19/18 13:55:26'
#datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')


