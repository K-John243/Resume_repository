'''
This program acts as a module for get_gene_level_information.py.
It stores functions such as get_filehandle() that help in the program.
'''
import os.path


def get_filehandle(file=None, mode=None):
    '''
    takes in a file path and mode (writing 'w' or reading 'r') and opens the file handle
    :param file: the path to the file
    :param mode: either read 'r' or write 'w'
    :return: the file handle to either read or write to
    '''

    try:

        fobj = open(file, mode)

        return fobj
    except OSError:

        print(f"Could not open the file: {file} for type '{mode}'")

        raise
    except ValueError:
        print(f"Could not open the file: {file} for type '{mode}'")

        raise


def is_gene_file_valid(file_name):
    '''
    checks to see if the file for the host and the gene exists
    :param file_name: the path to the file
    :return: True if the path exists, False if the path does not exist
    '''
    return bool(os.path.exists(file_name))
