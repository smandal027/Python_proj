from filehandling import file_read
content=file_read('employee.txt','r')
line_count=int(len(content))
print(content[0])
print(content[line_count//2])
#print(content[-2:])
for line in content[-2:]:
    print(line)