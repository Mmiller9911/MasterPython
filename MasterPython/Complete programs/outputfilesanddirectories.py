import os


def list_directories(s):

    def dir_list(d):
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_directory = os.path.join(d, f)
            if os.path.isdir(current_directory):
                print('\t' * tab_stop + 'Directory ' + f)
                tab_stop += 1
                dir_list(current_directory)
                tab_stop -= 1
            else:
                print('\t' * tab_stop + f)

    tab_stop = 0

    if os.path.exists(s):
        print('Directory listing of ' + s)
        dir_list(s)
    else:
        print('Directory does not exist - ' + s)


list_directories('.')
print('+_+' * 10)
#  Print all files in the current directory
# listing = os.walk('.')  # returns a tuple
# for root, directories, files in listing:
#     print(root)
#     for d in directories:
#         print(d)
#     for f in files:
#         print(f)

