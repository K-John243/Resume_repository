'''
This program takes in a host name (from a list of accepted names)
and a gene name from the command line, opens the downloaded
unigene data file storing the host and gene data, finds the list
of tissues it is expressed in, and prints this out to the command line
'''
import sys
import os
import argparse
import re
from assignment5 import config
from assignment5 import io_utils


def main():
    '''
    The main program that runs all of the functions
    :return: The list of tissues the host expresses the gene in
    '''
    args = get_cli_args()
    host_name = args.host.lower()
    gene_name = args.gene.upper()
    if '_' in host_name:
        host_name = host_name.replace('_', ' ')
    host = update_host_name(host_name)
    gene = gene_name
    file = os.path.join(config.get_directory_for_unigene(), host,
                        gene + "." + config.get_extension_for_unigene())
    if io_utils.is_gene_file_valid(file):
        # using f-strings
        print(f"\nFound Gene {gene} for {host.replace('_', ' ')}")
    else:
        print("Not found")
        print(f"Gene {gene} does not exist for {host.replace('_',' ')}. \
        exiting now...", file=sys.stderr)
        sys.exit(1)

    get_data_for_gene_file(file)
    print_host_to_gene_name_output(host, gene, get_data_for_gene_file(file))


def get_cli_args():
    """
    Getting the command line interface arguments using argparse
    :return: Instance of the argparse arguments
    """
    parser = argparse.ArgumentParser(description='Give the Host and Gene name',
                                     prog='get_gene_level_information.py')
    parser.add_argument('--host',
                        dest='host',
                        type=str,
                        help='Name of Host',
                        required=False,
                        nargs='?',
                        default="Human")
    parser.add_argument('-g', '--gene',
                        dest='gene',
                        type=str,
                        help='Name of Gene',
                        required=False,
                        nargs='?',
                        default='TGM1')

    return parser.parse_args()


def update_host_name(host):
    '''
    Checks to see if the host is in the data set
    if it's not in the set, it will call the helper function that
    prints out a message and the available hosts
    :param host: the host input from the command line
    :return: the host scientific name, or the list of available host names
    '''
    if host in config.get_keywords_for_hosts():
        return config.get_keywords_for_hosts()[host]
    else:
        return _print_directories_for_hosts()


def _print_directories_for_hosts():
    '''
    helper function that is called by update_host_name().
    This function simply prints a message for the user followed
    by a list of available hosts by their scientific names.
    :return: simply prints the message and list out, and then exits the program
    '''
    print('Either the Host Name you are searching for is not in the database\n\n'
          'or If you are trying to use the scientific name please put the name in double quotes:\n\n'
          '"Scientific name"\n\n'
          'Here is a (non-case sensitive) list of available Hosts by scientific name\n')
    temp_list = list(set(list(config.get_keywords_for_hosts().values())))
    num = 1
    for item in sorted(temp_list):
        print(f'\t{num}.{item}')
        num += 1
    print('\n')

    print('Here is a (non-case sensitive) list of available Hosts by common name')
    print('')
    temp_list_2 = sorted(list(config.get_keywords_for_hosts().keys()))
    num = 1
    for item in temp_list_2:
        item = item.capitalize()
        print(f'\t{num}.{item}')
        num += 1
    print('')
    sys.exit(1)


def get_data_for_gene_file(file):
    '''
    calls the function get_filehandle() to open the data file input into the function.
    Parses the data out line by line, using a regular expression to
    look for the line containing al of the tissue. Assembles a list of
    tissues and sorts the list alphabetically.
    :param file: the path to the data file for the host and gene
    :return: list of tissues
    '''
    in_fh = io_utils.get_filehandle(file, 'r')
    list_tissues = []
    for line in in_fh:
        line = line.rstrip()
        match = re.search(("^EXPRESS + (.*)"), line)
        if match:
            tissue_strig = match.group(1)
            list_tissues = tissue_strig.split('|')
            for item in range(len(list_tissues)):
                list_tissues[item] = list_tissues[item].lstrip()
            list_tissues = sorted(list_tissues)

    return list_tissues


def print_host_to_gene_name_output(host_name, gene_name, list_tissues):
    '''
    Takes the host name, gene name, and list of tissues and prints them out in a message
    to the user. Also prints the list of tissues out orderly and in a numbered list.
    :param host_name: the name of the host
    :param gene_name: name of the gene
    :param list_tissues: list of tissues
    :return: nothing, just prints a message and list
    '''
    length_tissues = len(list_tissues)
    print(f"In {host_name.replace('_',' ')}, There are {length_tissues} tissues\
 that {gene_name} is expressed in:\n")

    num = 1
    for item in list_tissues:
        item = item.capitalize()
        print(f'\t{num}.{item}')
        num += 1


if __name__ == '__main__':
    main()
