'''
    PYTHON 3.4.4v
    Author: John Andrie Pareja
'''

from os import path
import pprint
import json

# parent root directory
parent_dir = path.dirname(
                  path.dirname(
                  path.abspath(__file__)))

''' Description:
        loads the json_data data from a JSON file. Checks if the JSON
        file exists; if false prints error then exits the program
        execution.
'''
def read_json_file(file):
    json_data = []
    file_loc = parent_dir + "\\data\\" + file + ".json"
    if path.isfile(file_loc):
        try:
            with open(file_loc) as data:
                json_data = json.load(data)
                print("Successfully loaded:",file)
        except IOError:
            print("An Error has occured while reading the",file,"File")
            exit()
    else:
        print("[Error] \'" + file_loc +"\' could not be found!")
        exit()
    return json_data


'''Description:
        Writes or creates a json file
        this function is used on python dictionaries
'''
def write_dict_json_file(file_name,data):
    output_file_loc = parent_dir + "\\output\\" + file_name +".json"
    try:
        if(isinstance(data,dict)):
            print("generating file:",file_name+".json")
            with open(output_file_loc,"w+") as output:
                json.dump(data,output)
    except TypeError:
        print("Error: expected dictionary, non-dictionary given")


'''Description:
        Writes or creates a json file
        this function is used on python lists
'''
def write_list_json_file(file_name,data):
    output_file_loc = parent_dir + "\\output\\" + file_name +".json"
    try:
        if(isinstance(data,list)):
            print("generating file:",file_name+".json")
            with open(output_file_loc,"w+") as output:
                json.dump(data,output)
    except TypeError:
        print("Error: expected list, non-list given")



'''Description
        creates/rewrites json file for chart data
'''
def write_to_file_json(file_name,data):
    output_file_loc = parent_dir + "\\json-score\\" + file_name +".json"
    temp_list = "["

    print("generating file:",file_name+".json")
    try:
        if(isinstance(data,dict)):
            for keys in data:
                temp_list += "{ y : "+str(data[keys])+", label : '"+keys+"'},"
            a = temp_list.strip(',') + ']'
            with open(output_file_loc,"w+") as output:
                 output.write(a)
    except TypeError:
        print("Error: expected dictionary, non-dictionary given")
