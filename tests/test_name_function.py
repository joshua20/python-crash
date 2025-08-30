#writing our first test
from name_function import get_formatted_name

def test_first_last_name():
    '''do names like 'Joshua Nyakundi' work'''
    formatted_name=get_formatted_name('joshua','nyakundi')
    assert formatted_name=='Joshua Nyakundi'

def test_first_middle_last_name():
    '''do names joshua ariemba nyakundi work'''

    formatted_name=get_formatted_name('joshua','ariemba','nyakundi')
    assert formatted_name=='Joshua Ariemba Nyakundi'

