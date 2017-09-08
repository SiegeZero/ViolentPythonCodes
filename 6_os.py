import os
def osMethod( file_name):
    if not os.path.isfile( file_name):
        print file_name + " file not exists"
        return
    if not os.access( file_name, os.R_OK):
        print file_name + " access denied"
        return
    print file_name + " is opened success"
    return

file_name = "5_normal_file.txt"
osMethod( file_name)
file_name = "5_not_exists_file.txt"
osMethod( file_name)
file_name = "5_access_denied_file.txt"
osMethod( file_name)
