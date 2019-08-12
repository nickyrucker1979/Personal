
import os

# directory_path = '/documents/github/data-integrations/eab_ssc/sql/'
directory_path = 'SQL'
output_file = 'eab_files.txt'

for file in os.listdir(directory_path):
    # removes the .txt from file_name
    file_name = os.path.splitext(file)[0]
    myfile = open(output_file, 'a')
    # write file_name to a new line in the file
    myfile.writelines(file_name + '\n')
    myfile.close()
