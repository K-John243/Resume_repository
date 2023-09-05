'''
Unit testing for io_utils.py module
'''
import os
import pytest
from assignment5 import io_utils

FILE_TO_TEST = "test_file.txt"
FILE_TO_TEST_PARSING = "test_file.fasta"
FASTA_STR_TO_TEST = """\
>TEST1 A/TEST/TEST/2006 2006// 4 (HA)
TACAGCACGGCAACGCTGTGCCTTGGGCACCANGCAGTACCAAACGGAACGATAGTGAAAACAATCACGA
TTGACCAAATTGAAGTTACTAATGCTACTGAGCTGGTTCAGAGTTCCTCAACAGGTGAAATATGCGACAG
ACCTCATCAGATCCTTGATGGAGAAAACTGCACACTAATAGATGCTCTATTGGGAGACCCTCAGTGTGAT
"""


def _create_file_for_testing(file):
    '''
    temporarily creates a file that is used for testing
    :param file: file name
    :return: nothing
    '''
    open(file, "w").close()


def test_existing_get_filehandle_for_reading():
    '''
    tests if get_filehandle() works for creating a file for reading
    :return: assert
    '''
    _create_file_for_testing(FILE_TO_TEST)
    test = io_utils.get_filehandle(FILE_TO_TEST, "r")
    assert hasattr(test, "readline") is True
    test.close()
    os.remove(FILE_TO_TEST)


def test_existing_get_filehandle_for_writing():
    '''
    tests that get_filehandle() works for creating a file for writing
    :return: assert
    '''
    test = io_utils.get_filehandle(FILE_TO_TEST, 'w')
    assert hasattr(test, "write") is True
    test.close()
    os.remove(FILE_TO_TEST)


def test_get_file_handle_for_oserror():
    '''
    tests that get_filehandle() will throw an OSError if you give
    the function a file that doesn't exist
    :return: pytest.raises error
    '''
    with pytest.raises(OSError):
        io_utils.get_filehandle("does_not_exist.txt", "r")


def test_get_filehandle_for_valueerror():
    '''
    tests that get_filehandle() will throw a ValueError when you don't give
    it either 'w' or 'r' for the mode input
    :return: pytest.raises error
    '''
    _create_file_for_testing(FILE_TO_TEST)
    with pytest.raises(ValueError):
        io_utils.get_filehandle("does_not_exist.txt", "rrr")
    os.remove(FILE_TO_TEST)
