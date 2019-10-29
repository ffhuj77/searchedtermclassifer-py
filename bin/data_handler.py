'''
    PYTHON 3.4.4v
    Author: John Andrie Pareja
'''

import re
from bin import json_handler

# keywords data placeholder
kw_data = json_handler.read_json_file("keywords");

# search terms data placeholder
st_data = json_handler.read_json_file("searchTerms")


''' Description:
        Checks the searchterm for a keyword match
        returns true if a keyword matches otherwise false
'''
def has_match(kw,st):
    if kw == "":
        return False
    else:
        return re.search(r'\b'+kw+r'\b',st,re.I)

''' Description:
        Checks the searchterm for a keyword match
        returns true if a keyword matches otherwise false
'''
def calc_score(soreboard):
    try:
        if(isinstance(soreboard,dict)):
            # get MAXIMUM values of each items in the dictionary
            max_key_val = max(soreboard,key=soreboard.get);
            if(soreboard[max_key_val] == 0):
                return 'Uncategorized'
            else:
                return max_key_val
    except TypeError:
        print("Error: expected dictionary, non-dictionary given")


''' Description:
        returns keyword dataset
'''
class keywords():
    ''' Description:
            returns all categories and keywords dataset
    '''
    def get_all():
        return kw_data["keywords"]

    ''' Description:
            returns categories as list
    '''
    def get_categories():
        return list(kw_data["keywords"].keys())

    ''' Description:
            returns categories as dictionary
    '''
    def temp_category_holder():
        category = {}

        for key in kw_data["keywords"]:
            category[key] = []

        return category

''' Description:
        returns searcrh terms dataset
'''
class search_term():
    ''' Description:
            returns a specific via numeric index searcrhterms
    '''
    def get_term(key,keyvalue):
        term_data = []
        for index in range(len(st_data["searches"])):
            for item in st_data["searches"][index]:
                if item == "SearchTerm":
                    term_data.append(st_data["searches"][index][item])
        return term_data

    ''' Description:
            returns all searchtem dataset
    '''
    def get_all():
        return st_data["searches"]
