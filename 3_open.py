file_name = "3_open_py_text.txt"
try:
    file = open( file_name, "r")
    for line in file.readlines():
        print line.strip('\n')
    pass
except Exception as e:
    print "Error:" + str( e)
    raise
