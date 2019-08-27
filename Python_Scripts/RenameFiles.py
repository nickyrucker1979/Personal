import os

# Function to rename multiple files in a subfolder
def rename_files(folder):
    for filename in os.listdir(folder):
        fn = filename.split(".",1)[0]
        fncsv = fn + '.csv'
        # print renaming
        print(filename + ' renamed to ' + fncsv)

        src = folder + '/' +  filename
        dst = folder + '/' + fncsv
        os.rename(src, dst)

# Driver Code
if __name__ == '__main__':

    subfolder = 'oldnames'
    rename_files(subfolder)
