import os
import sys



# A function that will read the files in the folder and sorts them in alphabetical order
# Returns the sorted list of files as a list
def read_files(path):
    files = os.listdir(path)
    files.sort()
    return files

# A function that will copy the files from one folder to another
# It copies only the files for the given range of a list
def copy_files(sorted_files, start, end, source_path, destination_path):
    for file in sorted_files[start:end]:
        os.system('cp ' + source_path + file + ' ' + destination_path)


if __name__ == '__main__':

    if ( len(sys.argv) < 3 ):
        print('Usage: python '+sys.argv[0]+ ' <src_path> <dest_path>')
        print('\t src_path: the folder containing the images to be copied')
        print('\t dest_path: the folder where the images will be copied')
        sys.exit(0)
    
    # Parse the arguments
    src_path = sys.argv[1]
    dest_path = sys.argv[2]

    sorted_files = read_files(src_path)

    # Create the train, test and val folders if they don't exist
    if not os.path.exists(dest_path + 'train/'):
        os.makedirs(dest_path + 'train/')
    if not os.path.exists(dest_path + 'test/'):
        os.makedirs(dest_path + 'test/')
    if not os.path.exists(dest_path + 'val/'):
        os.makedirs(dest_path + 'val/')

    # Reapeat the following steps for train, test and val
    # Copy the files from the source folder to the destination folder
    copy_files(sorted_files, 0, 2000, src_path, dest_path + 'train/')
    copy_files(sorted_files, 30000, 30100, src_path, dest_path + 'val/')
    copy_files(sorted_files, 40000, 50000, src_path, dest_path + 'test/')