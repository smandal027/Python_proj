def file_write(fname, fmode):
    fhandle=open(fname,fmode)
    while True:
        line=input('Enter a line-> ')
        if line == 'end':
            break
        fhandle.write(line + '\n')
    fhandle.close()

def file_read(fname,fmode):
    with open(fname, fmode) as fread:
        all_lines = fread.readlines()
    return all_lines
        #print(all_lines, '->', type(all_lines))






