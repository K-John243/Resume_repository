'''
Unit testing for the config.py module
'''

from assignment5 import config


def test_functions_getting_global_vars_extension():
    '''
    testing that the get_directory_for_unigene() function returns the directory variable
    :return: assert
    '''
    assert config.get_directory_for_unigene() == "./assignment5_data/assignment5_data"


def test_functions_getting_global_vars_file_ending():
    '''
    testing that get_extension_for_unigene() function returns the extension for unigene files
    :return:
    '''
    assert config.get_extension_for_unigene() == "unigene"


def test_get_host_keywords():
    '''
    testing that the get_host_keywords() function returns the correct host_keywords dictionary
    :return:
    '''
    bos_taurus = "Bos_taurus"
    equus_caballus = "Equus_caballus"
    homo_sapiens = "Homo_sapiens"
    mus_musculus = "Mus_musculus"
    ovis_aries = "Ovis_aries"
    rattus_norvegicus = "Rattus_norvegicus"

    host_dict = {
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

    assert config.get_keywords_for_hosts() == host_dict
