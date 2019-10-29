'''
    PYTHON 3.4.4v
    Author: John Andrie Pareja
'''

from bin import data_handler
from bin import json_handler
import pprint

# load keywords dataset
keywords_set = data_handler.keywords.get_all()

# load search terms dataset
searchTerms_set = data_handler.search_term.get_all()

# load categories dataset
st_categories_set = data_handler.keywords.temp_category_holder().copy()


''' Description:
        Processes each search term word for word and assigns a
        category if there is a match from a keyword in that
        category.
'''
def process():
    global st_categories_set
    score_board = {}
    #print("-----------------------------------------------")
    print("\nProcessing Search Term Data....")
    for terms in searchTerms_set:
        #print("[searching on]",terms['SearchTerm'])
        for category in keywords_set:
            # add a category to the scoreboard with default
            # value of 0
            score_board[category] = 0
            for item in keywords_set[category]:
                if data_handler.has_match(item,terms['SearchTerm']):
                    score_board[category] += 1
        temp = {"SearchTerm":terms['SearchTerm'],
                "Requests":terms['Requests']}
        ctgry = data_handler.calc_score(score_board)
        st_categories_set[ctgry].append(temp.copy())


'''Description
        summation of each Request Data from json file.
        returns a dictionary that contains the total Request
        of each search terms per categories.
'''
def count_reqs():
    temp_scoreboard = {}
    for category in st_categories_set:
        temp_scoreboard[category] = sum(itm['Requests']
                for itm in st_categories_set[category])
    return temp_scoreboard


'''Description

'''
def generate_chart_data():
    json_handler.write_to_file_json("category-score",
            {'Educational': 415,
             'Enternainment': 62,
             'Social Media': 36,
             'Sports': 7,
             'Uncategorized': 285})
