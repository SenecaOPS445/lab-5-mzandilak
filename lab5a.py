#!/usr/bin/env python3
# Author ID:mzandilak

def read_file_string(file_name):    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')
    contents = f.read()
    f.close()
    return contents

def read_file_list(file_name):    # Takes a file_name as string for a file name,     # returns its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')
    read_data = f.read()
    f.close()
    list_of_lines = read_data.split('\n') 
    filtered_lines = []  

    for line in  list_of_lines:
        if line != '': 
            filtered_lines.append(line) 
    return filtered_lines

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))