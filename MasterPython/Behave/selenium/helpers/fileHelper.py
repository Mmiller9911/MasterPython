#from utilitiesHelper import UtilitiesHelper  # uncomment this when running from MAIN
from helpers.utilitiesHelper import UtilitiesHelper


class FileHelper(object):

    def __init__(self):
        pass

    def make_a_file(self, data, sep=','):

        with open('users.csv', 'w') as users_file:
            newstring = ""
            for line in data:
                this_line = ''
                for el in line:
                    this_line += str(el)
                    this_line += sep
                    this_line.strip('[')
                newstring += this_line
                newstring += '\n'
            print(newstring, file=users_file)
            users_file.close()

    def read_a_file(self, filename):
        file = open(filename)

        line = file.readline()
        while line != '':  # exit when no more lines
            print(line)
            line = file.readline()

        file.close()

    def read_a_file_and_return(self, filename):
        file = open(filename)
        #import pdb; pdb.set_trace()
        all_lines = []
        line = file.readline()
        while line != '':  # exit when no more lines
            line = file.readline()
            splitline = line.split(",")
            all_lines += splitline
        file.close()
        return all_lines



if __name__ == '__main__':
    bill = UtilitiesHelper()
    bill.generate_group_of_test_users(10)
    file_data = bill.return_all_users()

    bernard = FileHelper()
    bernard.make_a_file(file_data, ',')
    bernard.read_a_file('users.csv')
