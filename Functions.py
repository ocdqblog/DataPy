from pathlib import Path
from csv import reader, writer
import json
import random

def convert_string_to_int(value):
    try:
        int(value)
    except ValueError:
        return value
    return int(value)

def convert_string_to_float(value):
    try:
        float(value)
    except ValueError:
        return value
    return float(value)

def convert_string_to_number(value):
    try:
        int(value)
    except ValueError:
        try:
            float(value)
        except ValueError:
            return value
        return float(value) 
    return int(value)

def is_list_all_int(input_list):
    for item in input_list:
        try:
            int(item)
        except ValueError:
            return False
    return True

def convert_list_to_int(input_list):
    if is_list_all_int(input_list):
        return [int(item) for item in input_list]
    return input_list
    
def is_list_all_float(input_list):
    for item in input_list:
        try:
            float(item)
        except ValueError:
            return False
    return True

def is_list_all_numeric(input_list):
    if is_list_all_int(input_list):
        return True
    if is_list_all_float(input_list):
        return True
    return False

def convert_list_to_float(input_list):
    if is_list_all_float(input_list):
        return [float(item) for item in input_list]
    return input_list

def convert_string_list_to_number_list(input_list):
    if is_list_all_int(input_list):
        return convert_list_to_int(input_list)
    if is_list_all_float(input_list):
        return convert_list_to_float(input_list)
    return input_list

def load_csv_file(csv_file, key_option = "assign surrogate key", surrogate_seed = 1):
    with open(csv_file, 'r') as file:
        csv_reader = reader(file)
        csv_data = list(csv_reader)
    # Assumes the first row is metadata (column names)
    metadata_list = csv_data[0]
    csv_data_list = csv_data[1::]
    # Strip leading and trailing spaces from input data values
    data_list = []
    for row in csv_data_list:
        data_list.append([value.strip() for value in row])
    data_with_metadata = []
    if key_option == "assign surrogate key":
        # Zip metadata and data together into a list of key:value pairs 
        for item in data_list:
            data_with_metadata.append(dict(zip(metadata_list, item)))
        # Zip together a nested dictionary with an assigned surrogate key starting at surrogate_seed
        csv_data = dict(zip(range(surrogate_seed, len(data_list) + surrogate_seed), data_with_metadata))
    elif key_option == "key is first column":
        metadata_list.pop(0) # Remove key column from metadata_list
        # Gather the list of key values from the first input column 
        data_keys = []
        for item in data_list:
            data_keys.append(item.pop(0)) # Remove key from data_list and append to data_keys
            data_with_metadata.append(dict(zip(metadata_list, item)))
        # Zip together a nested dictionary with the key values from the first input column  
        csv_data = dict(zip(data_keys, data_with_metadata))
    else:
        csv_data = {}    
    return csv_data
# Function Alias lcf = load_csv_file
lcf = load_csv_file

def load_csv_file_as_ldict(csv_file):
    with open(csv_file, 'r') as file:
        csv_reader = reader(file)
        csv_data = list(csv_reader)
    # Strip leading and trailing spaces from input data values
    data_list = []
    for row in csv_data:
        data_list.append([value.strip() for value in row])
    # Create a lookup dictionary (ldict)
    ldict = {}
    for row in data_list:
        ldict.update({row[0]: row[1]})
    return ldict
# Function Alias lcf = load_csv_file_as_ldict
lcfald = load_csv_file_as_ldict

def load_json_file(json_file):
    with open(json_file, 'r') as file:
        json_data = json.load(file)
    return json_data
# Function Alias ljf = load_json_file
ljf = load_json_file

def load_regex_file(regex_file):
    with open(regex_file, 'r') as file:
        regex_reader = reader(file)
        regex_data = [regex[0] for regex in list(regex_reader)]
        regex_clist = [(regex, re.compile(regex)) for regex in regex_data]
    return regex_clist
# Function Alias lrf = load_regex_file
lrf = load_regex_file

def load_regex_sub_file(regex_sub_file):
    with open(regex_sub_file, 'r') as file:
        regex_sub_reader = reader(file)
        regex_sub_data = list(regex_sub_reader)
        regex_sub_clist = [(re.compile(regex_sub[0]), regex_sub[1]) for regex_sub in regex_sub_data]
    return regex_sub_clist
# Function Alias lrsf = load_regex_sub_file
lrsf = load_regex_sub_file

def select_from_ndict(ndict, **kwargs):
    # If sample is not specified, default to 100
    if "sample" not in kwargs:
        sample = 100
    else:
        sample = kwargs["sample"]
    # If keys is not specified, default to a list of all keys in ndict
    if "keys" not in kwargs:
        keys = [key for key in ndict]
    else:
        # For random sampling, build a random key list for the sample size 
        if kwargs["keys"] == "RANDOM":
            all_keys = [key for key in ndict]
            keys = list(set(random.sample(all_keys, k = sample)))
        else:
            keys = kwargs["keys"]
    # If columns is not specified, default to a list of all columns in ndict
    if "columns" not in kwargs:
        first_key = list(ndict)[:1][0]
        columns = [nested_key for nested_key in ndict[first_key].keys()]
    else:
        columns = kwargs["columns"]
    # If missing_value is not specified, default to ""
    if "missing_value" not in kwargs:
        missing_value = ""
    else:
        missing_value = kwargs["missing_value"]    
    # If where is not specified, default to "NO WHERE"
    if "where" not in kwargs:
        where = "NO WHERE"
    else:
        where = kwargs["where"]
    # Check for a where clause to apply to the selection
    if where == "NO WHERE":
        keys = keys
    # If specified, where should be a nested dictionary with the following structure:
    #              {"column": <column name>, 
    #               "values": <value list>, 
    #              "operator": <"==" or "IN" or "!=" or "NOT IN" or "CONTAINS" or "NOT CONTAINS">} 
    else:
        if (where["operator"] == "==") or (where["operator"] == "IN"):
            keys = [key for key in ndict if where["column"] in ndict[key] 
                    if ndict[key][where["column"]] in where["values"]]
        elif (where["operator"] == "!=") or (where["operator"] == "NOT IN"):
            keys = [key for key in ndict if where["column"] in ndict[key] 
                    if ndict[key][where["column"]] not in where["values"]]
        elif where["operator"] == "CONTAINS":
            keys = [key for key in ndict if where["column"] in ndict[key] 
                    if where["values"][0] in ndict[key][where["column"]]]
        elif where["operator"] == "NOT CONTAINS":
            keys = [key for key in ndict if where["column"] in ndict[key] 
                    if where["values"][0] not in ndict[key][where["column"]]]
        else:
            keys = keys
    # Select data from ndict
    selected_ndict = {}
    for key in ndict:
        if key in keys:
            column_dict = {}
            for column in columns:
                if column in ndict[key]:
                    column_dict.update({column: ndict[key][column]})
                # If the column was not found, output it with missing_value
                else:
                    column_dict.update({column: missing_value})
            selected_ndict.update({key: column_dict})
    return selected_ndict
# Function Alias sfnd = select_from_ndict
sfnd = select_from_ndict 

def export_dict_as_json(export_dict, json_file, file_option = "w"):
    if file_option == "a":
        check_file = Path(json_file)
        if check_file.is_file():
            json_dict = load_json_file(json_file)
            json_dict.update(export_dict)
            export_dict = json_dict
    with open(json_file, 'w') as file:
        json.dump(export_dict, file)
    print(F"\nExported {len(export_dict)} keys to file: {json_file}")
# Function Alias edaj = export_dict_as_json
edaj = export_dict_as_json

def convert_mldict_to_list(convert_mldict, key_name = "Key"):
    mldict_as_list = []
    first_key = list(convert_mldict.keys())[0]
    mldict_key_row = [nested_key for nested_key in convert_mldict[first_key][0]]
    mldict_key_row.insert(0, "Level")
    mldict_key_row.insert(0, key_name)
    mldict_as_list.append(mldict_key_row)
    mldict_as_nk = {}
    for key in convert_mldict:
        mldict_as_nk.update({key: {}})
    for key in convert_mldict:
        # Convert convert_mldict to ndict with level as nested key
        level_ndict = {}
        for level in range(len(convert_mldict[key])):
            level_ndict.update({level: convert_mldict[key][level]})
        mldict_as_nk[key].update(level_ndict)
    for key in mldict_as_nk:    
        for level in range(len(mldict_as_nk[key])):
            mldict_value_row = [nested_value for nested_value in mldict_as_nk[key][level].values()]
            mldict_value_row.insert(0, level)
            mldict_value_row.insert(0, key)
            mldict_as_list.append(mldict_value_row)
    return mldict_as_list
# Function Alias cmldtl = convert_mldict_to_list
cmldtl = convert_mldict_to_list 

def convert_ndict_to_list(convert_ndict, key_name = "Key"):
	ndict_as_list = []
	first_key = list(convert_ndict)[:1][0]
	ndict_key_row = [nested_key for nested_key in convert_ndict[first_key].keys()]
	ndict_key_row.insert(0, key_name)
	ndict_as_list.append(ndict_key_row)
	for key in convert_ndict:
		ndict_value_row = [nested_value for nested_value in convert_ndict[key].values()]
		ndict_value_row.insert(0, key)
		ndict_as_list.append(ndict_value_row)
	return ndict_as_list
# Function Alias cndtl = convert_ndict_to_list
cndtl = convert_ndict_to_list  

def export_list_as_csv(export_list, csv_file, file_option = "w"):
    if file_option == "a":
        check_file = Path(csv_file)
        if check_file.is_file():
            export_list.pop(0) # Remove metadata from export_list
        else:
            file_option = "w"
    with open(csv_file, file_option) as file:
        csv_writer = writer(file)
        csv_writer.writerows(export_list)
    print(F"\nExported {len(export_list)} rows to file: {csv_file}")
# Function Alias elac = export_list_as_csv
elac = export_list_as_csv

def print_rows_in_dict(print_dict, print_limit = 0):
    if print_limit > 0:
        print_counter = 0
        for key, value in print_dict.items():
            if print_counter == print_limit:
                break
            print(F"{key}: {value}")
            print_counter += 1
    else:
        for key, value in print_dict.items():
            print(F"{key}: {value}")
# Function Alias prid = print_rows_in_dict
prid = print_rows_in_dict

def print_rows_in_list(print_list, print_limit = 0):
    if print_limit > 0:
        print_counter = 0
        for row in range(len(print_list)):
            if print_counter > print_limit:
                break
            print(print_list[row])
            print_counter += 1
    else:
        for row in range(len(print_list)):
            print(print_list[row])
# Function Alias pril = print_rows_in_list
pril = print_rows_in_list