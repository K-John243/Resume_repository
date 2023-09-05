'''
This program is a config file for get_gene_level_information.py.
It contains variables and functions that assist in the program.
Functions such as getting access to these unigene constants are all
stored here
'''
_DIRECTORY_FOR_UNIGENE = "./assignment5_data/assignment5_data"
_FILE_ENDING_FOR_UNIGENE = "unigene"


def get_directory_for_unigene():
    '''
    returns the directory the unigene data is stored in
    :return: the directory the unigene data is stored in
    '''
    return _DIRECTORY_FOR_UNIGENE


def get_extension_for_unigene():
    '''
    gets the file ending for unigene data
    :return: the file ending for unigene data
    '''
    return _FILE_ENDING_FOR_UNIGENE


def get_keywords_for_hosts():
    '''
    gets the dictionary containing the hosts and their accepted names
    :return: the dictionary containing the hosts
    '''
    bos_taurus = "Bos_taurus"
    equus_caballus = "Equus_caballus"
    homo_sapiens = "Homo_sapiens"
    mus_musculus = "Mus_musculus"
    ovis_aries = "Ovis_aries"
    rattus_norvegicus = "Rattus_norvegicus"

    host_keywords = {
        "bos taurus": bos_taurus,
        "cow": bos_taurus,
        "cows": bos_taurus,
        "equus caballus": equus_caballus,
        "horse": equus_caballus,
        "horses": equus_caballus,
        "homo sapiens": homo_sapiens,
        "human": homo_sapiens,
        "humans": homo_sapiens,
        "mus musculus": mus_musculus,
        "mouse": mus_musculus,
        "mice": mus_musculus,
        "ovis aries": ovis_aries,
        "sheep": ovis_aries,
        "sheeps": ovis_aries,
        "rattus_norvegicus": rattus_norvegicus,
        "rat": rattus_norvegicus,
        "rats": rattus_norvegicus,
    }
    return host_keywords
