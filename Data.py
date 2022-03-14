from functools import wraps
from pathlib import Path
from csv import reader, writer
import json
from collections import Counter, OrderedDict
from statistics import mean, median, stdev
import re
import random
from Functions_new import * 

class Data:
    """
    Load input data from a CSV file with column metadata in the first row, 
     into a multi-level* nested dictionary (key: [value_list] containing dict{input_row}), 
     by zipping together a list of input data values and a list of input metadata values.
      *The CSV input data is loaded into level 0 of the value_list for the key (key:[0]) 

    The record key for the multi-level nested dictionary can either be
     a natural key from the first column in the data and metadata values,
     or an assigned surrogate key starting at 1 (which is the default).
    """

    def __init__(self, csv_file, key_option = "assign surrogate key", surrogate_seed = 1):

        with open(csv_file, 'r') as file:
            csv_reader = reader(file)
            csv_data = list(csv_reader)
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
                data_with_metadata.append([dict(zip(metadata_list, item))])
            # Zip together a nested dictionary with an assigned surrogate key starting at surrogate_seed
            self.nd = dict(zip(range(surrogate_seed, len(data_list) + surrogate_seed), data_with_metadata))
        elif key_option == "key is first column":
            metadata_list.pop(0) # Remove key column from metadata_list
            # Gather the list of key values from the first input column
            data_keys = []
            for item in data_list:
                data_keys.append(item.pop(0)) # Remove key from data_list and append to data_keys
                data_with_metadata.append([dict(zip(metadata_list, item))])
            # Zip together a nested dictionary with the key values from the first input column
            self.nd = dict(zip(data_keys, data_with_metadata))
        else:
            self.nd = {}

        self.default_regex_list = []
        self.default_regex_list.append("(?# delimiter)(ZQ)")
        self.default_regex_list.append("(?# phone)(\(?\d{3}\)?[-\.]?\d{3}[-\.]?\d{4})")
        self.default_regex_list.append("(?# phone)(\d{3}[-\.]\d{4})")
        self.default_regex_list.append("(?# area_code)(\(\d{3}\))")
        self.default_regex_list.append("(?# email)([\w.+-]+@[\w-]+\.[\w.-]+)")
        self.default_regex_list.append("(?# url)((HTTP://|HTTPS://|WWW.)(?:[A-Z]|[0-9]|[$-_@.&+#]|[!*\(\), ]|(?:%[0-9A-F][0-9A-F]))+)")
        self.default_regex_list.append("(?# date)((?P<century>19|20)(?P<year>[0-9]{2})[-/]?(?P<month>01|03|05|07|08|10|12)[-/]?(?P<day>[0-2][0-9]|3[0-1]))")
        self.default_regex_list.append("(?# date)((?P<century>19|20)(?P<year>[0-9]{2})[-/]?(?P<month>04|06|09|11)[-/]?(?P<day>[0-2][0-9]|30))")
        self.default_regex_list.append("(?# date)((?P<century>19|20)(?P<year>[0-9]{2})[-/]?(?P<month>02)[-/]?(?P<day>[0-1][0-9]|2[0-9]))")
        self.default_regex_list.append("(?# date)((?P<month>01|03|05|07|08|10|12)[-/]?(?P<day>[0-2][0-9]|3[0-1])[-/]?(?P<century>19|20)(?P<year>[0-9]{2}))")
        self.default_regex_list.append("(?# date)((?P<month>04|06|09|11)[-/]?(?P<day>[0-2][0-9]|30)[-/]?(?P<century>19|20)(?P<year>[0-9]{2}))")
        self.default_regex_list.append("(?# date)((?P<month>02)[-/]?(?P<day>[0-1][0-9]|2[0-9])[-/]?(?P<century>19|20)(?P<year>[0-9]{2}))")
        self.default_regex_list.append("(?# date)((?P<month>1|3|5|7|8|10|12)[-/]?(?P<day>[1-9]|[1-2][0-9]|3[0-1])[-/]?(?P<century>19|20)(?P<year>[0-9]{2}))")
        self.default_regex_list.append("(?# date)((?P<month>4|6|9|11)[-/]?(?P<day>[1-9]|[1-2][0-9]|30)[-/]?(?P<century>19|20)(?P<year>[0-9]{2}))")
        self.default_regex_list.append("(?# date)((?P<month>2)[-/]?(?P<day>[1-9]|[1][0-9]|2[0-9])[-/]?(?P<century>19|20)(?P<year>[0-9]{2}))")
        self.default_regex_list.append("(?# float)([0-9]+\.[0-9]+)")
        self.default_regex_list.append("(?# zip_code)(\d{5})")
        self.default_regex_list.append("(?# zip_code)(\d{5}\-\d{4})")
        self.default_regex_list.append("(?# integer)([0-9]+)")
        self.default_regex_list.append("(?# letter)([A-Z]{1})")
        self.default_regex_list.append("(?# period_terminated_letter)([A-Z]{1}\.)")
        self.default_regex_list.append("(?# alpha_code)([A-Z]{2,3})")
        self.default_regex_list.append("(?# alpha)([A-Z]+)")
        self.default_regex_list.append("(?# comma_terminated_alpha)([A-Z]+,)")
        self.default_regex_list.append("(?# hyphenated_alpha)([A-Z]+-[A-Z]+)")
        self.default_regex_list.append("(?# parenthetical_alpha)(\([A-Z]+\))")
        self.default_regex_list.append("(?# period_terminated_alpha)([A-Z]+\.)")
        self.default_regex_list.append("(?# possessive_alpha)([A-Z]+['`]S)")
        self.default_regex_list.append("(?# possessive_alpha)([A-Z]+S['`])")
        self.default_regex_list.append("(?# alpha_numeric)([A-Z]+[0-9]+)")
        self.default_regex_list.append("(?# numeric_alpha)([0-9]+[A-Z]+)")
        self.default_regex_list.append("(?# ampersand)(&)")
        self.default_regex_list.append("(?# comma)(\,)")
        self.default_regex_list.append("(?# hash)(#)")
        self.default_regex_list.append("(?# hyphen)(-)")
        self.default_regex_list.append("(?# period)(\.)")
        self.default_regex_list.append("(?# special)([\(\)$\-_@.,!%\*&\+#:;\"\'\<\>\?\/])")
        self.default_regex_list.append("(?# mixed_alpha_special)([A-Z\(\)$\-_@.,!%\*&\+#:;\"\'\<\>\?\/]+)")
        self.default_regex_list.append("(?# mixed_numeric_special)([0-9\(\)$\-_@.,!%\*&\+#:;\"\'\<\>\?\/]+)")
        self.default_regex_list.append("(?# mixed_alpha_numeric)([A-Z0-9]+)")
        self.default_regex_list.append("(?# mixed_alpha_numeric_special)([A-Z0-9\(\)$\-_@.,!%\*&\+#:;\"\'\<\>\?\/]+)")

        self.default_regex_clist = [(regex, re.compile(regex)) for regex in self.default_regex_list]
        self.pattern_regex = re.compile(r'^(\(\?\#) (?P<pattern>\w+)(\))')

    def __len__(self):
        return len(self.nd)

    def __repr__(self):
        return F"Nested dictionary containing {len(self.nd)} keys"

    def method_call_with_json(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            if kwargs and "kwargs_json" in kwargs:
                kwargs_json = load_json_file(kwargs["kwargs_json"])
                return method(self, *args, **kwargs_json)
            return method(self, *args, **kwargs)
        return wrapper

    def is_key_list(self, key_list, level = 0):
        """Uses set intersection to check if a list of keys exist.
        Checks within a level, or level 0 by default."""
        full_key_set = set(self.key_list(level))
        if type(key_list) == list:
            key_set = set(key_list)
        else:
            key_set = set([key_list])
        intersection = full_key_set & key_set
        if intersection == key_set:
            return True
        return False
    # Method Alias is_kl = is_key_list
    is_kl = is_key_list

    def is_key(self, key, level = 0):
        if level == 0:
            if key in self.nd:
                return True
            return False
        level_key_list = set(self.key_list(level))
        if key in level_key_list:
            return True
        return False
    # Method Alias is_k = is_key
    is_k = is_key

    def is_level(self, level, key = "ALL KEYS"):
        if key == "ALL KEYS":
            if self.is_key_list(self.key_list(), level):
                return True
            return False
        if self.is_key(key, level):
            return True
        return False
    # Method Alias is_l = is_level
    is_l = is_level

    def is_attribute_value(self, attribute, value, key = "ANY KEY", level = 0):
        if key == "ANY KEY":
            for key in self.nd:
                if self.is_key(key, level):
                    if attribute in self.nd[key][level]:
                        if self.nd[key][level][attribute] == value:
                            return True
        if self.is_key(key, level):
            if attribute in self.nd[key][level]:
                if self.nd[key][level][attribute] == value:
                    return True
        return False
    # Method Alias is_av = is_attribute_value
    is_av = is_attribute_value

    def is_attribute_constant(self, attribute, level = 0):
        av_dict = self.attribute_values_dict(attribute, level)
        if len(av_dict) > 0:
            value_list = av_dict[attribute]
            value_set = set(value_list)
            count_null = value_list.count("")
            if len(value_set) == 1 and count_null == 0:
                return True
        return False
    # Method Alias is_ac = is_attribute_constant
    is_ac = is_attribute_constant

    def is_attribute_unique(self, attribute, level = 0):
        av_dict = self.attribute_values_dict(attribute, level)
        if len(av_dict) > 0:
            value_list = av_dict[attribute]
            count_value = len(value_list)
            value_set = set(value_list)
            count_unique = len(value_set)
            if count_unique == count_value:
                return True
        return False
    # Method Alias is_au = is_attribute_unique
    is_au = is_attribute_unique

    def is_attribute_null(self, attribute, level = 0):
        av_dict = self.attribute_values_dict(attribute, level)
        if len(av_dict) > 0:
            value_list = av_dict[attribute]
            count_value = len(value_list)
            count_null = value_list.count("")
            if count_null == count_value:
                return True
        return False
    # Method Alias is_an = is_attribute_null
    is_an = is_attribute_null

    def is_attribute(self, attribute, key = "ANY KEY", level = 0):
        if key == "ANY KEY":
            for key in self.nd:
                if self.is_key(key, level):
                    if attribute in self.nd[key][level]:
                        return True
        if self.is_key(key, level):
            if attribute in self.nd[key][level]:
                return True
        return False
    # Method Alias is_a = is_attribute
    is_a = is_attribute

    def is_value(self, value, key = "ANY KEY", level = 0):
        if key == "ANY KEY":
            for key in self.nd:
                if self.is_key(key, level):
                    if value in self.nd[key][level].values():
                        return True
        if self.is_key(key, level):
            if value in self.nd[key][level].values():
                return True
        return False
    # Method Alias is_v = is_value
    is_v = is_value

    def count_keys(self, level = "ALL LEVELS"):
        if level == "ALL LEVELS":
            return len(self.nd)
        k_count = 0
        for key in self.nd:
            if self.is_key(key, level):
                k_count += 1
        return k_count
    # Method Alias count_k = count_keys
    count_k = count_keys

    def count_levels(self, key, level = 0):
        if self.is_key(key, level):
            return len(self.nd[key])
        return 0
    # Method Alias count_l = count_levels
    count_l = count_levels

    def count_attributes(self, key, level = 0):
        if self.is_key(key, level):
            return len(self.nd[key][level])
        return 0
    # Method Alias count_a = count_attributes
    count_a = count_attributes

    def count_attribute_value(self, attribute, value, key = "ALL KEYS", level = 0):
        value_count = 0
        if key == "ALL KEYS":
            for key in self.nd:
                if self.is_key(key, level):
                    if attribute in self.nd[key][level]:
                        if self.nd[key][level][attribute] == value:
                            value_count += 1
            return value_count
        if self.is_key(key, level):
            if attribute in self.nd[key][level]:
                if self.nd[key][level][attribute] == value:
                    value_count += 1
        return value_count
    # Method Alias count_av = count_attribute_value
    count_av = count_attribute_value

    def count_attribute_unique_values(self, attribute, level = 0):
        count_unique = 0
        av_dict = self.attribute_values_dict(attribute, level)
        if len(av_dict) > 0:
            count_unique = len(set(av_dict[attribute]))
        return count_unique
    # Method Alias count_auv = count_attribute_unique_values
    count_auv = count_attribute_unique_values

    def count_attribute_null_values(self, attribute, level = 0):
        count_null = 0
        av_dict = self.attribute_values_dict(attribute, level)
        if len(av_dict) > 0:
            value_list = av_dict[attribute]
            count_null = value_list.count("")
        return count_null
    # Method Alias count_anv = count_attribute_null_values
    count_anv = count_attribute_null_values

    def count_value(self, value, key = "ALL KEYS", level = 0):
        value_count = 0
        if key == "ALL KEYS":
            for key in self.nd:
                if self.is_key(key, level):
                    for attribute in self.nd[key][level]:
                        if self.nd[key][level][attribute] == value:
                            value_count += 1
            return value_count
        if self.is_key(key, level):
            for attribute in self.nd[key][level]:
                if self.nd[key][level][attribute] == value:
                    value_count += 1
        return value_count
    # Method Alias count_v = count_value
    count_v = count_value

    def key_list(self, level = 0):
        return [key for key in self.nd if level < len(self.nd[key])]

    def key_list_attribute_value(self, attribute, level, operator, *values):
        if type(values[0]) == list:
            values = tuple(values[0])
        if operator == "==":
            return [key for key in self.nd
                    if self.is_key(key, level)
                    if attribute in self.nd[key][level]
                    if self.nd[key][level][attribute] in values]
        elif operator == "!=":
            return [key for key in self.nd
                    if self.is_key(key, level)
                    if attribute in self.nd[key][level]
                    if self.nd[key][level][attribute] not in values]
    # Method Alias kl_av = key_list_attribute_value
    kl_av = key_list_attribute_value

    def key_list_attribute_search(self, attribute, level, search):
        return [key for key in self.nd
                if self.is_key(key, level)
                if attribute in self.nd[key][level]
                if search in self.nd[key][level][attribute]]
    # Method Alias kl_as = key_list_attribute_search
    kl_as = key_list_attribute_search

    def key_list_attribute_format(self, attribute, level, operator, *formats):
        if type(formats[0]) == list:
            formats = tuple(formats[0])
        if operator == "==":
            return [key for key in self.nd
                    if self.is_key(key, level)
                    if attribute in self.nd[key][level]
                    if self.format_for_value(self.nd[key][level][attribute]) in formats]
        elif operator == "!=":
            return [key for key in self.nd
                    if self.is_key(key, level)
                    if attribute in self.nd[key][level]
                    if self.format_for_value(self.nd[key][level][attribute]) not in formats]
    # Method Alias kl_af = key_list_attribute_format
    kl_af = key_list_attribute_format

    def key_list_attribute_pattern(self, attribute, level, operator, pfv_kwargs, *patterns):
        if type(patterns[0]) == list:
            patterns = tuple(patterns[0])
        if operator == "==":
            return [key for key in self.nd
                    if self.is_key(key, level)
                    if attribute in self.nd[key][level]
                    if self.pattern_for_value(self.nd[key][level][attribute], **pfv_kwargs) in patterns]
        elif operator == "!=":
            return [key for key in self.nd
                    if self.is_key(key, level)
                    if attribute in self.nd[key][level]
                    if self.pattern_for_value(self.nd[key][level][attribute], **pfv_kwargs) not in patterns]
    # Method Alias kl_ap = key_list_attribute_pattern
    kl_ap = key_list_attribute_pattern

    def key_list_attribute(self, level, *attributes):
        if type(attributes[0]) == list:
            attributes = tuple(attributes[0])
        k_list = [key for key in self.nd
                  if self.is_key(key, level)
                  for attribute in self.nd[key][level]
                  if attribute in attributes]
        k_list = list(set(k_list))
        k_list.sort()
        return k_list
    # Method Alias kl_a = key_list_attribute
    kl_a = key_list_attribute

    def key_list_value(self, level, *values):
        if type(values[0]) == list:
            values = tuple(values[0])
        k_list = [key for key in self.nd
                  if self.is_key(key, level)
                  for attribute in self.nd[key][level]
                  if self.nd[key][level][attribute] in values]
        k_list = list(set(k_list))
        k_list.sort()
        return k_list
    # Method Alias kl_v = key_list_value
    kl_v = key_list_value

    def key_list_attribute_with_duplicate_values(self, attribute, level = 0, duplicate = True):
        if not duplicate:
            return [key for key in self.nd
                    if self.is_key(key, level)
                    if attribute in self.nd[key][level]
                    if self.nd[key][level][attribute] != ""
                    if self.count_attribute_value(attribute, self.nd[key][level][attribute], "ALL KEYS", level) == 1]
        return [key for key in self.nd
                if self.is_key(key, level)
                if attribute in self.nd[key][level]
                if self.nd[key][level][attribute] != ""
                if self.count_attribute_value(attribute, self.nd[key][level][attribute], "ALL KEYS", level) > 1]
    # Method Alias kl_adupv = key_list_attribute_with_duplicate_values
    kl_adupv = key_list_attribute_with_duplicate_values

    def levels_list(self, key, level = 0):
        if self.is_key(key, level):
            return self.nd[key]
        return []

    def level_dict(self, key, level = 0):
        if self.is_key(key, level):
            return self.nd[key][level]
        return {}

    def attribute_list(self, key, level = 0):
        return [attribute for attribute in self.nd[key][level]
                if self.is_key(key, level)]
    # Method Alias a_list = attribute_list
    a_list = attribute_list

    def value_list(self, key, level = 0):
        return [value for value in self.nd[key][level].values()
                if self.is_key(key, level)]
    # Method Alias v_list = value_list
    v_list = value_list

    def format_for_value(self, value):
        format_value = ""
        if isinstance(value, (int, float)):
            value = str(value)
        if value == "":
            format_value = "null"
        elif isinstance(value, bool):
            format_value = value
        else:
            for char in value:
                try:
                    char_convert = int(char)
                except ValueError:
                    char_convert = char
                if type(char_convert) is int:
                    char_convert = "n"
                elif char_convert == " ":
                    char_convert = "b"
                elif char_convert in "~`!@#$%^&*()_-=+[]{}|\:;'<>?,./":
                    char_convert = char_convert
                else:
                    char_convert = "a"
                format_value += char_convert
        return format_value
    # Method Alias ffv = format_for_value
    ffv = format_for_value

    def pattern_for_value(self, value, **kwargs):
        # If pattern_dict is not specified, use default regex
        if "pattern_dict" not in kwargs:
            default = True
        else:
            pattern_dict = kwargs["pattern_dict"]
            default = False
        # If value is an integer or a float, convert it to string
        if isinstance(value, (int, float)):
            value = str(value)
        # If value is an empty string, default patterns_list to ["null"]
        if value == "":
            patterns_list = ["null"]
        # If value is a boolean, set pattern_list to boolean as string
        elif isinstance(value, bool):
            patterns_list = [str(value)]
        # Parse and pattern uppercase version of value
        else:
            value = value.upper()
            # Parse based on specified parameters
            if "separators" in kwargs and "strip_list" in kwargs:
                separators = kwargs["separators"]
                strip_list = kwargs["strip_list"]
                values_list = re.split(F"([{separators}])", value)
                values_list = [value.strip() for value in values_list if value not in strip_list]
            # Parse based on spaces
            else:
                values_list = value.split()
            # Build patterns list
            patterns_list = []
            for value in values_list:
                pattern = "unknown"
                if not default:
                    if value in pattern_dict:
                        pattern = pattern_dict[value]
                else:
                    for regex in range(len(self.default_regex_clist)):
                        match = self.default_regex_clist[regex][1].fullmatch(value)
                        if match:
                            regex_match = self.default_regex_clist[regex][0]
                            pattern_match = self.pattern_regex.search(regex_match)
                            if pattern_match:
                                pattern = pattern_match.groupdict()["pattern"]
                                break # Stops after the first (if any) matching regex
                # If non-default patterns were attempted, try default on unknown
                if not default and pattern == "unknown":
                    for regex in range(len(self.default_regex_clist)):
                        match = self.default_regex_clist[regex][1].fullmatch(value)
                        if match:
                            regex_match = self.default_regex_clist[regex][0]
                            pattern_match = self.pattern_regex.search(regex_match)
                            if pattern_match:
                                pattern = pattern_match.groupdict()["pattern"]
                                break # Stops after the first (if any) matching regex
                patterns_list.append(pattern)
        pattern = " ".join(patterns_list)
        # If pattern_regex_sub is specified, check for pattern updates
        if "pattern_regex_sub" in kwargs:
            regex_sub_clist = kwargs["pattern_regex_sub"]
            for regex_sub in range(len(regex_sub_clist)):
                updated_pattern = regex_sub_clist[regex_sub][0].sub(regex_sub_clist[regex_sub][1], pattern)
                pattern = updated_pattern
        return pattern
    # Method Alias pfv = pattern_for_value
    pfv = pattern_for_value

    def attribute_values_dict(self, attribute, level = 0):
        value_list = []
        for key in self.nd:
            if self.is_key(key, level):
                if attribute in self.nd[key][level]:
                    value_list.append(self.nd[key][level][attribute])
        if len(value_list) > 0:
            av_dict = {attribute: value_list}
        else:
            av_dict = {}
        return av_dict
    # Method Alias avd = attribute_values_dict
    avd = attribute_values_dict

    def attribute_most_common_values(self, attribute, **kwargs):
        # If level is not specified, default to level 0
        if "level" not in kwargs:
            level = 0
        else:
            level = kwargs["level"]
        # If limit is not specified, default to limit 10
        if "limit" not in kwargs:
            limit = 10
        else:
            limit = kwargs["limit"]
        # If option is not specified, default to "dict"
        if "option" not in kwargs:
            option = "dict"
        else:
            option = kwargs["option"]
        # Determine the most common values for attribute
        amcv_dict = {}
        av_dict = self.attribute_values_dict(attribute, level)
        if len(av_dict) > 0:
            value_list = av_dict[attribute]
            total = len(value_list)
            amcv_dict = {attribute: dict(Counter(av_dict[attribute]).most_common(limit))}
            # Update amcv dictionary with count (now key/value pair) and percent
            for value, count in amcv_dict[attribute].items():
                amcv_dict[attribute][value] = {"count": count, "percent": round(((count / total) * 100), 2)}
        # Based on option, return the result as a dict or a list
        if option == "dict":
            amcv_result = amcv_dict
        elif option == "list":
            amcv_list = [["Attribute", "Value", "Count", "Percent"]]
            for value in amcv_dict[attribute].keys():
                amcv_list.append([attribute, value, amcv_dict[attribute][value]["count"], amcv_dict[attribute][value]["percent"]])
            amcv_result = amcv_list
        return amcv_result
    # Method Alias amcv = attribute_most_common_values
    amcv = attribute_most_common_values

    def attribute_most_common_words(self, attribute, **kwargs):
        # If level is not specified, default to level 0
        if "level" not in kwargs:
            level = 0
        else:
            level = kwargs["level"]
        # If limit is not specified, default to limit 10
        if "limit" not in kwargs:
            limit = 10
        else:
            limit = kwargs["limit"]
        # If sample_limit is not specified, default to sample_limit 10
        if "sample_limit" not in kwargs:
            sample_limit = 10
        else:
            sample_limit = kwargs["sample_limit"]
        # If option is not specified, default to "dict"
        if "option" not in kwargs:
            option = "dict"
        else:
            option = kwargs["option"]
        # Build word_value list and word_list
        amcw_dict = {}
        av_dict = self.attribute_values_dict(attribute, level)
        if len(av_dict) > 0:
            value_list = av_dict[attribute]
            total = len(value_list)
            word_value_list = []
            for value in value_list:
                words = [word for word in value.split()]
                for word in words:
                    word_value_list.append((word, value))
            word_list = [word for value in value_list for word in value.split()]
            # Determine the most common words for attribute
            amcw_dict = {attribute: dict(Counter(word_list).most_common(limit))}
            # Generate word sample dictionary
            ws_dict = {}
            for word in amcw_dict[attribute].keys():
                sample_list = []
                sample_count = 0
                for word_value in word_value_list:
                    if word_value[0] == word:
                        sample_list.append(word_value[1])
                        sample_count += 1
                        if sample_count == sample_limit:
                            break
                ws_dict.update({word: sample_list})
            # Update amcw dictionary with count (now key/value pair), pattern, percent and samples
            for word, count in amcw_dict[attribute].items():
                # Build keyword arguments for pattern_for_value
                pfv_kwargs = {}
                if "separators" in kwargs and "strip_list" in kwargs:
                    pfv_kwargs.update({"separators": kwargs["separators"]})
                    pfv_kwargs.update({"strip_list": kwargs["strip_list"]})
                if "pattern_file" in kwargs:
                    pattern_dict = load_json_file(kwargs["pattern_file"])
                    pfv_kwargs.update({"pattern_dict": pattern_dict})
                if "pattern_regex_sub_file" in kwargs:
                    pattern_regex_sub = load_regex_sub_file(kwargs["pattern_regex_sub_file"])
                    pfv_kwargs.update({"pattern_regex_sub": pattern_regex_sub})
                pattern = self.pattern_for_value(word, **pfv_kwargs)
                amcw_dict[attribute][word] = {"pattern": pattern, "count": count, "percent": round(((count / total) * 100), 2), "samples": ws_dict[word]}
            # If pattern_inclusion is specified, include only words with pattern in pattern_inclusion
            if "pattern_inclusion" in kwargs:
                amcw_dict = {attribute: {word: metrics for word, metrics in amcw_dict[attribute].items() if metrics["pattern"] in kwargs["pattern_inclusion"]}}
        # Based on option, return the result as a dict or a list
        if option == "dict":
            amcw_result = amcw_dict
        elif option == "list":
            amcw_list = [["Attribute", "Word", "Pattern", "Count", "Percent", "Samples"]]
            for word in amcw_dict[attribute].keys():
                amcw_list.append([attribute, word, amcw_dict[attribute][word]["pattern"], amcw_dict[attribute][word]["count"], amcw_dict[attribute][word]["percent"], " | ".join(amcw_dict[attribute][word]["samples"])])
            amcw_result = amcw_list
        return amcw_result
    # Method Alias amcw = attribute_most_common_words
    amcw = attribute_most_common_words

    @method_call_with_json
    def attribute_most_common_formats(self, attribute, **kwargs):
        # If level is not specified, default to level 0
        if "level" not in kwargs:
            level = 0
        else:
            level = kwargs["level"]
        # If limit is not specified, default to limit 10
        if "limit" not in kwargs:
            limit = 10
        else:
            limit = kwargs["limit"]
        # If sample_limit is not specified, default to sample_limit 10
        if "sample_limit" not in kwargs:
            sample_limit = 10
        else:
            sample_limit = kwargs["sample_limit"]
        # If option is not specified, default to "dict"
        if "option" not in kwargs:
            option = "dict"
        else:
            option = kwargs["option"]
        # Build format_value list and format_list
        av_dict = self.attribute_values_dict(attribute, level)
        amcf_dict = {}
        if len(av_dict) > 0:
            value_list = av_dict[attribute]
            total = len(value_list)
            format_value_list = [(self.format_for_value(value), value) for value in value_list]
            format_list = [self.format_for_value(value) for value in value_list]
            # Determine the most common formats for attribute
            amcf_dict = {attribute: dict(Counter(format_list).most_common(limit))}
            # Generate format sample dictionary
            fs_dict = {}
            for format in amcf_dict[attribute].keys():
                sample_list = []
                sample_count = 0
                for format_value in format_value_list:
                    if format_value[0] == format:
                        sample_list.append(format_value[1])
                        sample_count += 1
                        if sample_count == sample_limit:
                            break
                fs_dict.update({format: sample_list})
            # Update amcf dictionary with count (now key/value pair), percent and samples
            for format, count in amcf_dict[attribute].items():
                amcf_dict[attribute][format] = {"count": count, "percent": round(((count / total) * 100), 2), "samples": fs_dict[format]}
        # Based on option, return the result as a dict or a list
        if option == "dict":
            amcf_result = amcf_dict
        elif option == "list":
            amcf_list = [["Attribute", "Format", "Count", "Percent", "Samples"]]
            for format in amcf_dict[attribute].keys():
                amcf_list.append([attribute, format, amcf_dict[attribute][format]["count"], amcf_dict[attribute][format]["percent"], " | ".join(amcf_dict[attribute][format]["samples"])])
            amcf_result = amcf_list
        return amcf_result
    # Method Alias amcf = attribute_most_common_formats
    amcf = attribute_most_common_formats

    @method_call_with_json
    def attribute_most_common_patterns(self, attribute, **kwargs):
        # If level is not specified, default to level 0
        if "level" not in kwargs:
            level = 0
        else:
            level = kwargs["level"]
        # If limit is not specified, default to limit 10
        if "limit" not in kwargs:
            limit = 10
        else:
            limit = kwargs["limit"]
        # If sample_limit is not specified, default to 10
        if "sample_limit" not in kwargs:
            sample_limit = 10
        else:
            sample_limit = kwargs["sample_limit"]
        # If mapping_file is specified, load the mapping
        if "mapping_file" in kwargs:
            mapping = load_json_file(kwargs["mapping_file"])
        # If option is not specified, default to "dict"
        if "option" not in kwargs:
            option = "dict"
        else:
            option = kwargs["option"]
        # Build pattern_value list and pattern_list
        av_dict = self.attribute_values_dict(attribute, level)
        amcp_dict = {}
        if len(av_dict) > 0:
            value_list = av_dict[attribute]
            total = len(value_list)
            # Build keyword arguments for pattern_for_value
            pfv_kwargs = {}
            if "separators" in kwargs and "strip_list" in kwargs:
                pfv_kwargs.update({"separators": kwargs["separators"]})
                pfv_kwargs.update({"strip_list": kwargs["strip_list"]})
            if "pattern_file" in kwargs:
                pattern_dict = load_json_file(kwargs["pattern_file"])
                pfv_kwargs.update({"pattern_dict": pattern_dict})
            if "pattern_regex_sub_file" in kwargs:
                pattern_regex_sub = load_regex_sub_file(kwargs["pattern_regex_sub_file"])
                pfv_kwargs.update({"pattern_regex_sub": pattern_regex_sub})
            pattern_value_list = [(self.pattern_for_value(value, **pfv_kwargs), value) for value in value_list]
            pattern_list = [self.pattern_for_value(value, **pfv_kwargs) for value in value_list]
            if "mapping_file" in kwargs:
                pattern_value_list = [pattern_value for pattern_value in pattern_value_list if pattern_value[0] not in mapping]
                pattern_list = [pattern for pattern in pattern_list if pattern not in mapping]
            # Determine the most common patterns for attribute
            amcp_dict = {attribute: dict(Counter(pattern_list).most_common(limit))}
            # Generate pattern sample dictionary
            ps_dict = {}
            for pattern in amcp_dict[attribute].keys():
                sample_list = []
                sample_count = 0
                for pattern_value in pattern_value_list:
                    if pattern_value[0] == pattern:
                        sample_list.append(pattern_value[1])
                        sample_count += 1
                        if sample_count == sample_limit:
                            break
                ps_dict.update({pattern: sample_list})
            # Update amcp dictionary with count (now key/value pair), percent and samples
            for pattern, count in amcp_dict[attribute].items():
                amcp_dict[attribute][pattern] = {"count": count, "percent": round(((count / total) * 100), 2), "samples": ps_dict[pattern]}
        # Based on option, return the result as a dict or a list
        if option == "dict":
            amcp_result = amcp_dict
        elif option == "list":
            amcp_list = [["Attribute", "Pattern", "Count", "Percent", "Samples"]]
            for pattern in amcp_dict[attribute].keys():
                amcp_list.append([attribute, pattern, amcp_dict[attribute][pattern]["count"], amcp_dict[attribute][pattern]["percent"], " | ".join(amcp_dict[attribute][pattern]["samples"])])
            amcp_result = amcp_list    
        return amcp_result
    # Method Alias amcp = attribute_most_common_patterns
    amcp = attribute_most_common_patterns

    def attribute_analysis(self, attribute, **kwargs):
        # If level is not specified, default to level 0
        if "level" not in kwargs:
            level = 0
        else:
            level = kwargs["level"]
        # If option is not specified, default to "dict"
        if "option" not in kwargs:
            option = "dict"
        else:
            option = kwargs["option"]
        # Perform attribute analysis
        av_dict = self.attribute_values_dict(attribute, level)
        aa_dict = {}
        if len(av_dict) > 0:
            value_list = av_dict[attribute]
            non_null_value_list = [value for value in value_list if value != ""]
            non_null_length_list = [len(str(value)) for value in non_null_value_list]
            count_value = len(value_list)
            value_set = set(value_list)
            count_null = value_list.count("")
            percent_null = round(((count_null / count_value) * 100), 2)
            count_unique = len(value_set)
            percent_unique = round(((count_unique / count_value) * 100), 2)
            min_max_value_list = convert_string_list_to_number_list(non_null_value_list)
            if min_max_value_list == []:
                min_value = ""
                max_value = ""
                mean_value = ""
                median_value = ""
                stdev_value = ""
                ML_datatype = "" 
            else:
                min_value = min(min_max_value_list)
                max_value = max(min_max_value_list)
                if is_list_all_numeric(min_max_value_list):
                    mean_value = mean(min_max_value_list)
                    median_value = median(min_max_value_list)
                    stdev_value = stdev(min_max_value_list)
                    ML_datatype = "Numerical"
                else:
                    mean_value = "N/A"
                    median_value = "N/A"
                    stdev_value = "N/A"
                    ML_datatype = "Categorical"
            if value_set == {0,1}:
                ML_datatype = "Label"
            length_list = [len(str(value)) for value in value_list]
            if min(length_list) == 0 and max(length_list) > 0:
                min_length = min(non_null_length_list)
            else:
                min_length = min(length_list)
            max_length = max(length_list)
            format_list = [self.format_for_value(value) for value in non_null_value_list]
            format_count = len(set(format_list))
            # Build keyword arguments for pattern_for_value
            pfv_kwargs = {}
            if "separators" in kwargs and "strip_list" in kwargs:
                pfv_kwargs.update({"separators": kwargs["separators"]})
                pfv_kwargs.update({"strip_list": kwargs["strip_list"]})
            if "pattern_file" in kwargs:
                pattern_dict = load_json_file(kwargs["pattern_file"])
                pfv_kwargs.update({"pattern_dict": pattern_dict})
            if "pattern_regex_sub_file" in kwargs:
                pattern_regex_sub = load_regex_sub_file(kwargs["pattern_regex_sub_file"])
                pfv_kwargs.update({"pattern_regex_sub": pattern_regex_sub})
            pattern_list = [self.pattern_for_value(value, **pfv_kwargs) for value in non_null_value_list]
            pattern_count = len(set(pattern_list))
            if len(value_set) == 1 and count_null == 0:
                is_constant = True
            else:
                is_constant = False
            if count_null == count_value:
                is_null = True
            else:
                is_null = False
            if count_unique == count_value:
                is_unique = True
            else:
                is_unique = False
            if not is_null:
                most_common_value = list(Counter(non_null_value_list).most_common(1))
                least_common_value = list(Counter(non_null_value_list).most_common()[:-1-1:-1])
                most_common_format = list(Counter(format_list).most_common(1))
                least_common_format = list(Counter(format_list).most_common()[:-1-1:-1])
                most_common_pattern = list(Counter(pattern_list).most_common(1))
                least_common_pattern = list(Counter(pattern_list).most_common()[:-1-1:-1])
            else:
                min_value = "null"
                max_value = "null"
                most_common_value = [("null", count_null)]
                least_common_value = [("null", count_null)]
                most_common_format = [("null", count_null)]
                least_common_format = [("null", count_null)]
                most_common_pattern = [("null", count_null)]
                least_common_pattern = [("null", count_null)]
            aa_dict = {attribute: {"value_count": count_value}}
            aa_dict[attribute].update({"unique_count": count_unique})
            aa_dict[attribute].update({"unique_percent": percent_unique})
            aa_dict[attribute].update({"null_count": count_null})
            aa_dict[attribute].update({"null_percent": percent_null})
            aa_dict[attribute].update({"min_value": min_value})
            aa_dict[attribute].update({"max_value": max_value})
            aa_dict[attribute].update({"mean_value": mean_value})
            aa_dict[attribute].update({"median_value": median_value})
            aa_dict[attribute].update({"stdev_value": stdev_value})
            aa_dict[attribute].update({"most_common_value": F"{most_common_value[0][0]} ({most_common_value[0][1]})"})
            aa_dict[attribute].update({"least_common_value": F"{least_common_value[0][0]} ({least_common_value[0][1]})"})
            aa_dict[attribute].update({"min_length": min_length})
            aa_dict[attribute].update({"max_length": max_length})
            aa_dict[attribute].update({"format_count": format_count})
            aa_dict[attribute].update({"most_common_format": F"{most_common_format[0][0]} ({most_common_format[0][1]})"})
            aa_dict[attribute].update({"least_common_format": F"{least_common_format[0][0]} ({least_common_format[0][1]})"})
            aa_dict[attribute].update({"pattern_count": pattern_count})
            aa_dict[attribute].update({"most_common_pattern": F"{most_common_pattern[0][0]} ({most_common_pattern[0][1]})"})
            aa_dict[attribute].update({"least_common_pattern": F"{least_common_pattern[0][0]} ({least_common_pattern[0][1]})"})
            aa_dict[attribute].update({"ML_datatype": ML_datatype})
            aa_dict[attribute].update({"is_null": is_null})
            aa_dict[attribute].update({"is_unique": is_unique})
            aa_dict[attribute].update({"is_constant": is_constant})
        # Based on option, return the result as a dict or a list
        if option == "dict":
            aa_result = aa_dict
        elif option == "list":
            aa_list = []
            aa_key_row = [metric_key for metric_key in aa_dict[attribute].keys()]
            aa_key_row.insert(0, "Attribute")
            aa_list.append(aa_key_row)
            aa_value_row = [metric_value for metric_value in aa_dict[attribute].values()]
            aa_value_row.insert(0, attribute)
            aa_list.append(aa_value_row)
            aa_result = aa_list
        return aa_result
    # Method Alias aa = attribute_analysis
    aa = attribute_analysis

    def profiling(self, **kwargs):
        # If level is not specified, default to level 0
        if "level" not in kwargs:
            level = 0
        else:
            level = kwargs["level"]
        # If option is not specified, default to "dict"
        if "option" not in kwargs:
            option = "dict"
        else:
            option = kwargs["option"]
        # If exclude is not specified, default to []
        if "exclude" not in kwargs:
            exclude = []
        else:
            exclude = kwargs["exclude"]
            if type(exclude) != list:
                exclude =[]
        # Perform attribute analysis for all attributes in level
        first_key = -1
        for key in self.nd:
            if self.is_key(key, level):
                first_key = key
                break
        if first_key != -1:
            level_attributes = self.attribute_list(first_key, level)
            attributes = [attribute for attribute in level_attributes if attribute not in exclude]
        profiling_dict = {}
        for attribute in attributes:
            attribute_profile = self.attribute_analysis(attribute, level = level, option = "dict")
            profiling_dict[attribute] = attribute_profile[attribute]
        # Based on option, return the result as a dict or a list
        if option == "dict":
            profiling_result = profiling_dict
        elif option == "list":
            profiling_list = convert_ndict_to_list(profiling_dict)
            profiling_result = profiling_list
        return profiling_result

    def standardize_value(self, value, sa_dict, std_attributes, mapping, **kwargs):
        pfv_kwargs = {}
        # Parse based on specified parameters
        if "separators" in kwargs and "strip_list" in kwargs:
            separators = kwargs["separators"]
            pfv_kwargs.update({"separators": kwargs["separators"]})
            strip_list = kwargs["strip_list"]
            pfv_kwargs.update({"strip_list": kwargs["strip_list"]})
            values_list = re.split(F"([{separators}])", value)
            values_list = [value.strip() for value in values_list if value not in strip_list]
        # Parse based on spaces
        else:
            values_list = value.split()
        # If specified, add pattern_dict and pattern_regex_sub to pfv_kwargs
        if "pattern_dict" in kwargs:
            pfv_kwargs.update({"pattern_dict": kwargs["pattern_dict"]})
        if "pattern_regex_sub" in kwargs:
            pfv_kwargs.update({"pattern_regex_sub": kwargs["pattern_regex_sub"]})
        pattern = self.pattern_for_value(value, **pfv_kwargs)
        sa_dict.update({"Pattern": pattern})
        sa_dict.update(std_attributes)
        sa_dict.update({"Standardized": False})
        sa_mapping = ""
        if pattern in mapping:
            sa_mapping = mapping[pattern]
            sa_dict.update({"Standardized": True})
            mapping_list = list(zip(sa_mapping, values_list))
            for sa_key in std_attributes:
                sa_value = ""
                for sa_tuple in mapping_list:
                    if sa_tuple[0] == sa_key:
                        sa_value = sa_value + " " + sa_tuple[1]
                sa_value = sa_value.strip()
                sa_dict.update({sa_key: sa_value})
        return sa_dict
    # Method Alias sv = standardize_value
    sv = standardize_value

    def standardize_attribute(self, attribute, std_attributes_file, mapping_file, level = 0, **kwargs):
        std_attributes = load_json_file(std_attributes_file)
        sv_kwargs = {"std_attributes": std_attributes}
        mapping = load_json_file(mapping_file)
        sv_kwargs.update({"mapping": mapping})
        # If specified, add separators and strip_list to sv_kwargs
        if "separators" in kwargs and "strip_list" in kwargs:
            sv_kwargs.update({"separators": kwargs["separators"]})
            sv_kwargs.update({"strip_list": kwargs["strip_list"]})
        # If pattern_file is specified, load the pattern_dict
        if "pattern_file" in kwargs:
            pattern_dict = load_json_file(kwargs["pattern_file"])
            sv_kwargs.update({"pattern_dict": pattern_dict})
        # If pattern_regex_sub_file is specified, load the pattern_regex_sub
        if "pattern_regex_sub_file" in kwargs:
            pattern_regex_sub = load_regex_sub_file(kwargs["pattern_regex_sub_file"])
            sv_kwargs.update({"pattern_regex_sub": pattern_regex_sub})
        # Perform attribute standardization
        row_counter = 0
        standardized_counter = 0
        for key in self.nd:
            if self.is_key(key, level):
                if attribute in self.nd[key][level]:
                    row_counter += 1
                    value = self.nd[key][level][attribute]
                    sa_dict = {attribute: value}
                    sa_dict = self.standardize_value(value, sa_dict, **sv_kwargs)
                    self.add_level(key, sa_dict, level)
                    if sa_dict["Standardized"]:
                        standardized_counter += 1
        print(F"Processed {row_counter} rows, {standardized_counter} were standardized ({round(((standardized_counter / row_counter) * 100), 2)} %)")
    # Method Alias sa = standardize_attribute
    sa = standardize_attribute

    def regex_value(self, value, regex_dict, regex_clist):
        for regex in range(len(regex_clist)):
            match = regex_clist[regex][1].fullmatch(value)
            if match:
                regex_dict.update(match.groupdict())
                regex_match = regex_clist[regex][0]
                pattern_match = self.pattern_regex.search(regex_match)
                if pattern_match:
                    regex_dict.update({"Regex": pattern_match.groupdict()["pattern"]})
                break # Stops after the first (if any) matching regex
        return regex_dict
    # Method Alias rv = regex_value
    rv = regex_value

    def regex_attribute(self, attribute, std_attributes_file, regex_file, **kwargs):
        std_attributes = load_json_file(std_attributes_file)
        regex_clist = load_regex_file(regex_file)
        # If level is not specified, default to level 0
        if "level" not in kwargs:
            level = 0
        else:
            level = kwargs["level"]
        # Populate std_attributes using regex
        for key in self.nd:
            if self.is_key(key, level):
                if attribute in self.nd[key][level]:
                    value = self.nd[key][level][attribute]
                    ra_dict = {attribute: value}
                    ra_dict.update(std_attributes)
                    ra_dict.update({"Regex": ""})
                    ra_dict = self.regex_value(value, ra_dict, regex_clist)
                    self.add_level(key, ra_dict, level)
    # Method Alias ra = regex_attribute
    ra = regex_attribute

    def validate_regex(self, value, regex_clist):
        for regex in range(len(regex_clist)):
            match = regex_clist[regex][1].fullmatch(value)
            if match:
                return True
        return False
    # Method Alias vr = validate_regex
    vr = validate_regex

    def attribute_validation(self, attribute, validation_file, validation_option = "value", **kwargs):
        # If level is not specified, default to level 0
        if "level" not in kwargs:
            level = 0
        else:
            level = kwargs["level"]
        # If limit is not specified, default to limit 10
        if "limit" not in kwargs:
            limit = 10
        else:
            limit = kwargs["limit"]
        # Load validation_file based on validation_option
        if validation_option == "value":
            validation = load_json_file(validation_file)
        else:
            regex_clist = load_regex_file(validation_file)
        # Perform attribute validation
        av_dict = self.attribute_values_dict(attribute, level)
        va_dict = {}
        if len(av_dict) > 0:
            value_list = av_dict[attribute]
            count_value = len(value_list)
            if validation_option == "regex":
                valid_list = [value for value in value_list if self.validate_regex(value, regex_clist)]
                invalid_list = [value for value in value_list if not self.validate_regex(value, regex_clist)]
            else:
                valid_list = [value for value in value_list if value in validation]
                invalid_list = [value for value in value_list if value not in validation]
            count_valid = len(valid_list)
            count_invalid = len(invalid_list)
            percent_valid = round(((count_valid / count_value) * 100), 2)
            percent_invalid = round(((count_invalid / count_value) * 100), 2)
            most_common_valid = dict(Counter(valid_list).most_common(limit))
            most_common_invalid = dict(Counter(invalid_list).most_common(limit))
            if count_value == count_valid:
                is_valid = True
            else:
                is_valid = False
            va_dict = {attribute: {"is_valid": is_valid}}
            va_dict[attribute].update({"count_valid": count_valid})
            va_dict[attribute].update({"percent_valid": percent_valid})
            va_dict[attribute].update({"count_invalid": count_invalid})
            va_dict[attribute].update({"percent_invalid": percent_invalid})
            va_dict[attribute].update({"most_common_valid": most_common_valid})
            va_dict[attribute].update({"most_common_invalid": most_common_invalid})
            va_dict[attribute].update({"validation_file": validation_file})
        else:
            va_dict = {}
        return va_dict
    # Method Alias av = attribute_validation
    av = attribute_validation

    def attribute_encoding(self, attribute, **kwargs):
        # If level is not specified, default to level 0
        if "level" not in kwargs:
            level = 0
        else:
            level = kwargs["level"]
        # If rank_encoding is not specified, default to False
        if "rank_encoding" not in kwargs:
            rank_encoding = False
        else:
            rank_encoding = kwargs["rank_encoding"]
        # If one_hot_encoding is not specified, default to False
        if "one_hot_encoding" not in kwargs:
            one_hot_encoding = False
        else:
            one_hot_encoding = kwargs["one_hot_encoding"]
        # Get list of all values for the attribute 
        avd_dict = self.attribute_values_dict(attribute)
        value_list = avd_dict[attribute]
        # Label Encoding
        value_sorted_unique_list = sorted(list(set(value_list)))
        label_encoding_dict = {}
        list_index = 0
        for value in value_sorted_unique_list:
            label_encoding_dict.update({value: list_index})
            list_index +=1
        label_encoding_attribute = attribute + "_label"
        # Rank Encoding (optional based on parameter)
        if rank_encoding:
            value_freqsorted_list = [item for items, c in Counter(value_list).most_common() for item in [items] * c]
            value_freqsorted_list_unduped = list(OrderedDict.fromkeys(value_freqsorted_list))
            value_freqsorted_list_unduped_reversed = value_freqsorted_list_unduped[::-1]
            rank_encoding_dict = {}
            list_index = 0
            for value in value_freqsorted_list_unduped_reversed:
                rank_encoding_dict.update({value: list_index})
                list_index +=1
            rank_encoding_attribute = attribute + "_rank"   
        # One-Hot Encoding (optional based on parameter)
        if one_hot_encoding:
            one_hot_encoding_attributes = []
            list_index = 0
            for value in value_sorted_unique_list:
                one_hot_encoding_attributes.append(attribute + "_" + str(list_index))
                list_index +=1
        # Add new encoding attributes to all keys in the level             
        for key in self.nd:
            if self.is_key(key, level):
                if attribute in self.nd[key][level]:
                    # If performed, add new rank encoding attribute
                    if rank_encoding:
                        value = rank_encoding_dict[self.nd[key][level][attribute]]
                        rank_update_dict = {rank_encoding_attribute: value}
                        self.update_level(key, rank_update_dict, level)
                    # Add new label encoding attribute
                    value = label_encoding_dict[self.nd[key][level][attribute]]
                    label_update_dict = {label_encoding_attribute: value}
                    self.update_level(key, label_update_dict, level)
                    # If performed, add new one-hot encoding attributes
                    if one_hot_encoding:
                        list_index = 0
                        for one_hot_encoding_attribute in one_hot_encoding_attributes:
                            if self.nd[key][level][attribute] == value_sorted_unique_list[list_index]:
                                value = 1
                            else:
                                value = 0
                            one_hot_update_dict = {one_hot_encoding_attribute: value}
                            self.update_level(key, one_hot_update_dict, level)
                            list_index +=1
    # Method Alias ae = attribute_encoding
    ae = attribute_encoding

    def remove_attribute(self, attribute, key = "ALL KEYS", level = 0):
        if key == "ALL KEYS":
            for key in self.nd:
                if self.is_key(key, level):
                    if attribute in self.nd[key][level]:
                        self.nd[key][level].pop(attribute)
        else:
            if self.is_key(key, level):
                if attribute in self.nd[key][level]:
                    self.nd[key][level].pop(attribute)

    def add_attribute(self, attribute, missing_value = "", key = "ALL KEYS", level = 0):
        if key == "ALL KEYS":
            for key in self.nd:
                if self.is_key(key, level):
                    if attribute not in self.nd[key][level]:
                        add_dict = {attribute: missing_value}
                        self.update_level(key, add_dict, level)
        else:
            if self.is_key(key, level):
                if attribute not in self.nd[key][level]:
                    add_dict = {attribute: missing_value}
                    self.update_level(key, add_dict, level)

    def change_attribute_value(self, attribute, value, change, key = "ALL KEYS", level = 0):
        if key == "ALL KEYS":
            for key in self.nd:
                if self.is_key(key, level):
                    if attribute in self.nd[key][level]:
                        if self.nd[key][level][attribute] == value:
                            self.nd[key][level][attribute] = change
        else:
            if self.is_key(key, level):
                if attribute in self.nd[key][level]:
                    if self.nd[key][level][attribute] == value:
                        self.nd[key][level][attribute] = change
    # Method Alias change_av = change_attribute_value
    change_av = change_attribute_value

    def change_attribute(self, attribute, change, key = "ALL KEYS", level = 0):
        if key == "ALL KEYS":
            for key in self.nd:
                if self.is_key(key, level):
                    if attribute in self.nd[key][level]:
                        self.nd[key][level][change] = self.nd[key][level].pop(attribute)
        else:
            if self.is_key(key, level):
                if attribute in self.nd[key][level]:
                    self.nd[key][level][change] = self.nd[key][level].pop(attribute)
    # Method Alias change_a = change_attribute
    change_a = change_attribute

    def change_value(self, value, change, key = "ALL KEYS", level = 0):
        if key == "ALL KEYS":
            for key in self.nd:
                if self.is_key(key, level):
                    for attribute in self.nd[key][level]:
                        if self.nd[key][level][attribute] == value:
                            self.nd[key][level][attribute] = change
        else:
            if self.is_key(key, level):
                for attribute in self.nd[key][level]:
                    if self.nd[key][level][attribute] == value:
                        self.nd[key][level][attribute] = change
    # Method Alias change_v = change_value
    change_v = change_value

    def baseline_attribute(self, attribute, baseline_value, level = 0):
        # Convert the attribute values based on comparison to baseline
        for key in self.nd:
            if self.is_key(key, level):
                if attribute in self.nd[key][level]:
                    if convert_string_to_number(self.nd[key][level][attribute]) >= convert_string_to_number(baseline_value):
                        self.nd[key][level][attribute] = 1
                    else:
                        self.nd[key][level][attribute] = 0
    # Method Alias baseline_a = baseline_attribute
    baseline_a = baseline_attribute

    def convert_attribute(self, attribute, conversion_file, **kwargs):
        # If level is not specified, default to level 0
        if "level" not in kwargs:
            level = 0
        else:
            level = kwargs["level"]
        # If default_use is not specified, default to False
        if "default_use" not in kwargs:
            default_use = False
        else:
            default_use = kwargs["default_use"]
        # If default_value is not specified, default to ""
        if "default_value" not in kwargs:
            default_value = ""
        else:
            default_value = kwargs["default_value"]
        # Convert the attribute values using the conversion file
        conversion = load_json_file(conversion_file)
        for key in self.nd:
            if self.is_key(key, level):
                if attribute in self.nd[key][level]:
                    value = self.nd[key][level][attribute]
                    if value in conversion:
                        value = conversion[value]
                        self.nd[key][level][attribute] = value
                    else:
                        if default_use:
                            self.nd[key][level][attribute] = default_value
    # Method Alias convert_a = convert_attribute
    convert_a = convert_attribute

    def convert_value(self, value, conversion_file, level = 0):
        conversion = load_json_file(conversion_file)
        for key in self.nd:
            if self.is_key(key, level):
                for attribute in self.nd[key][level]:
                    if self.nd[key][level][attribute] == value:
                        if value in conversion:
                            value = conversion[value]
                            self.nd[key][level][attribute] = value
    # Method Alias convert_v = convert_value
    convert_v = convert_value

    def transform_level(self, transformation, **kwargs):
        # If level is not specified, default to level 0
        if "level" not in kwargs:
            level = 0
        else:
            level = kwargs["level"]
        # Create a transform dictionary with the transformation
        for key in self.nd:
            if self.is_key(key, level):
                input_dict = self.level_dict(key, level)
                try: # Try to create a transform dictionary with specified Python expression
                    transform_dict = eval(transformation)
                except Exception as transformation_error:
                    print(F"Transformation failed: {transformation_error}\n")
                    break
                self.update_level(key, transform_dict, level)
    # Method Alias transform_l = transform_level
    transform_l = transform_level

    def transform_attribute_value(self, attribute, value, transformation, **kwargs):
        # If level is not specified, default to level 0
        if "level" not in kwargs:
            level = 0
        else:
            level = kwargs["level"]
        # Update, in place, the specified attribute value with the transform expression value
        for key in self.nd:
            if self.is_key(key, level):
                if attribute in self.nd[key][level]:
                    if self.nd[key][level][attribute] == value:
                        value = self.nd[key][level][attribute]
                        try: # Try to transform attribute's value with specified Python expression
                            transformed_value = eval(transformation)
                        except Exception as transformation_error:
                            print(F"Transformation failed: {transformation_error}\n")
                            break 
                        update_dict = {attribute: transformed_value}
                        self.update_level(key, update_dict, level)
    # Method Alias transform_av = transform_attribute_value
    transform_av = transform_attribute_value

    def transform_attribute(self, attribute, transformation, **kwargs):
        # If level is not specified, default to level 0
        if "level" not in kwargs:
            level = 0
        else:
            level = kwargs["level"]
        # Update all attribute values with the transform expression value
        for key in self.nd:
            if self.is_key(key, level):
                if attribute in self.nd[key][level]:
                    value = self.nd[key][level][attribute]
                    try: # Try to transform attribute's value with specified Python expression
                        transformed_value = eval(transformation)
                    except Exception as transformation_error:
                        print(F"Transformation failed: {transformation_error}\n")
                        break
                    # If new_attribute is not specified, use attribute
                    if "new_attribute" not in kwargs:
                        new_attribute = attribute
                    else:
                        new_attribute = kwargs["new_attribute"]
                    update_dict = {new_attribute: transformed_value}
                    self.update_level(key, update_dict, level)
    # Method Alias transform_a = transform_attribute
    transform_a = transform_attribute

    def transform_value(self, value, transformation, **kwargs):
        # If level is not specified, default to level 0
        if "level" not in kwargs:
            level = 0
        else:
            level = kwargs["level"]
        # Update, in place, value with the transform expression value wherever it's found in dictionary level
        for key in self.nd:
            if self.is_key(key, level):
                for attribute in self.nd[key][level]:
                    if self.nd[key][level][attribute] == value:
                        value = self.nd[key][level][attribute]
                        try: # Try to transform the value with specified Python expression
                            transformed_value = eval(transformation)
                        except Exception as transformation_error:
                            print(F"Transformation failed: {transformation_error}\n")
                            break
                        update_dict = {attribute: transformed_value}
                        self.update_level(key, update_dict, level)
    # Method Alias transform_v = transform_value
    transform_v = transform_value

    def add_level(self, key, add_dict, level = 0):
        if self.is_key(key, level):
            self.nd[key].append(add_dict)

    def update_level(self, key, update_dict, level = 0):
        if self.is_key(key, level):
            self.nd[key][level].update(update_dict)
        else:
            # New entries are identified as attempted updates at level 0
            #   for a key that does not exist in the nested dictionary
            if level == 0:
                # If using a surrogate key, new key is max(key) + 1
                if type(max(self.nd)) == int:
                    new_key = max(self.nd) + 1
                    self.nd.update({new_key: [update_dict]})
                else:
                    # If using a natural key, new key is the specified key
                    self.nd.update({key: [update_dict]})

    def merge_level(self, merge_dict, level = 0):
        for merge_key in merge_dict:
            self.update_level(merge_key, merge_dict[merge_key], level)

    def replicate_level(self, level = 0):
        for key in self.nd:
            if self.is_key(key, level):
                self.add_level(key, self.level_dict(key, level), level)

    def compare_two_levels(self, key, level_1, level_2):
        if self.is_key(key, level_1) and self.is_key(key, level_2):
            level_dict_1 = self.level_dict(key, level_1)
            level_dict_2 = self.level_dict(key, level_2)
            if level_dict_1 == level_dict_2:
                return True
            return False
        return False
    # Method Alias c2l = compare_two_levels
    c2l = compare_two_levels

    def remove_level(self, level):
        for key in self.nd:
            if self.is_key(key, level):
                self.nd[key].pop(level)           
    
    def remove_key(self, key):
        if self.is_key(key):
            self.nd.pop(key)

    def replicate_attribute(self, attribute, new_attribute, level = 0):
        for key in self.nd:
            if self.is_key(key, level):
                if attribute in self.nd[key][level]:
                    replicate_dict = {new_attribute: self.nd[key][level][attribute]}
                    self.update_level(key, replicate_dict, level)

    def concat_attributes_into_new_attribute(self, attributes, **kwargs):
        # If level is not specified, default to level 0
        if "level" not in kwargs:
            level = 0
        else:
            level = kwargs["level"]
        # Create new attribute and add it to the dictionary for specified keys
        for key in self.nd:
            if self.is_key(key, level):
                value = ""
                for attribute in attributes:
                    if attribute in self.nd[key][level] or attribute.startswith("delimiter"):
                        if len(value) == 0:
                            if attribute.startswith("delimiter"):
                                value = attribute[10::]
                                attribute_name = attribute[10::]
                            else:
                                value = self.nd[key][level][attribute]
                                attribute_name = attribute
                        else:
                            if attribute.startswith("delimiter"):
                                value = value + " " + attribute[10::]
                                attribute_name = attribute_name + "_" + attribute[10::]
                            else:
                                value = value + " " + self.nd[key][level][attribute]
                                attribute_name = attribute_name + "_" + attribute
                value = " ".join(value.split())
                # If new_attribute is not specified, use attribute_name
                if "new_attribute" not in kwargs:
                    new_attribute = attribute_name
                else:
                    new_attribute = kwargs["new_attribute"]
                update_dict = {new_attribute: value}
                self.update_level(key, update_dict, level)
    # Method Alias cana = concat_attributes_into_new_attribute
    cana = concat_attributes_into_new_attribute

    def count_attribute_diff(self, level = 0):
        attribute_diff = -1
        first_key = -1
        for key in self.nd:
            if self.is_key(key, level):
                first_key = key
                break
        if first_key != -1:
            baseline_a_list = self.attribute_list(first_key, level)
            attribute_diff = 0
            for key in self.nd:
                if self.is_key(key, level):
                    a_list = self.attribute_list(key, level)
                    if a_list != baseline_a_list:
                        attribute_diff += 1
        return attribute_diff
    # Method Alias count_a_diff = count_attribute_diff
    count_a_diff = count_attribute_diff

    def export_as_list(self, level = 0, keys = "ALL KEYS"):
        """Returns a list of CSV value lists
        for a level (default is level 0)
        and specified keys (default is 'ALL KEYS').
        Row 0 is the list of column metadata
        and each subsequent row is a list of key, value list.
        NOTE: An empty list is returned if there are attribute differences
        within the level since the exported rows would be inconsistent."""
        export_list = []
        if self.count_attribute_diff(level) == 0:
            first_key = -1
            for key in self.nd:
                if self.is_key(key, level):
                    first_key = key
                    break
            if first_key != -1:
                export_list = [self.attribute_list(first_key, level)]
                export_list[0].insert(0, "Key")
                export_row = []
                for key in self.nd:
                    if self.is_key(key, level):
                        if keys == "ALL KEYS" or (type(keys) == list and key in keys) or key == keys:
                            export_row = self.value_list(key, level)
                            export_row.insert(0, key)
                            export_list.append(export_row)
        return export_list

    def export_attributes_as_list(self, attributes, keys = "ALL KEYS", missing_value = ""):
        export_list = []
        export_key_row = ["Key"]
        for attribute in attributes:
            export_key_row.append(attribute)
        export_list.append(export_key_row)
        for key in self.nd:
            export_row = []
            if keys == "ALL KEYS" or (type(keys) == list and key in keys) or key == keys:
                export_row.append(key)
                for attribute in attributes:
                    attribute_found = False
                    for level in range(len(self.nd[key])):
                        if attribute in self.nd[key][level]:
                            export_row.append(self.nd[key][level][attribute])
                            attribute_found = True
                            break
                    if not attribute_found:
                        export_row.append(missing_value)
                export_list.append(export_row)
        return export_list

    def export_as_dict(self, level = "ALL LEVELS", keys = "ALL KEYS"):
        """Returns a dictionary
        for a specified level (default is 'ALL LEVELS')
        and specified keys (default is 'ALL KEYS')."""
        export_dict = {}
        if level == "ALL LEVELS" and keys == "ALL KEYS":
            export_dict = self.nd
        else:
            for key in self.nd:
                if self.is_key(key, level):
                    if keys == "ALL KEYS" or (type(keys) == list and key in keys) or key == keys:
                        export_dict.update({key: self.nd[key][level]})
        return export_dict

    def export_attributes_as_dict(self, attributes, keys = "ALL KEYS", missing_value = ""):
        export_dict = {}
        for key in self.nd:
            if keys == "ALL KEYS" or (type(keys) == list and key in keys) or key == keys:
                attribute_dict = {}
                for attribute in attributes:
                    attribute_found = False
                    for level in range(len(self.nd[key])):
                        if attribute in self.nd[key][level]:
                            attribute_dict.update({attribute: self.nd[key][level][attribute]})
                            attribute_found = True
                            break
                    if not attribute_found:
                        attribute_dict.update({attribute: missing_value})
                export_dict.update({key: attribute_dict})
        return export_dict

    @method_call_with_json
    def select(self, **kwargs):
        # If level is not specified, default to level 0
        if "level" not in kwargs:
            level = 0
        else:
            level = kwargs["level"]
        # If operator is not specified, default to operator "=="
        if "operator" not in kwargs:
            operator = "=="
        else:
            operator = kwargs["operator"]
        # If option is not specified, default to "dict"
        if "option" not in kwargs:
            option = "dict"
        else:
            option = kwargs["option"]
        # If attributes is not specified, default to "ALL"
        if "attributes" not in kwargs:
            attributes = "ALL"
        else:
            attributes = kwargs["attributes"]
        # If missing_value is not specified, default to ""
        if "missing_value" not in kwargs:
            missing_value = ""
        else:
            missing_value = kwargs["missing_value"]
        # If sample is not specified, default to 100
        if "sample" not in kwargs:
            sample = 100
        else:
            sample = kwargs["sample"]
        # Determine which, if any, key_list_ method should be called
        # Call key_list_attribute_value
        if "attribute" in kwargs and "value" in kwargs:
            k_list = self.key_list_attribute_value(kwargs["attribute"], level, operator, kwargs["value"])
        # Call key_list_attribute_search
        elif "attribute" in kwargs and "search" in kwargs:
            k_list = self.key_list_attribute_search(kwargs["attribute"], level, kwargs["search"])
        # Call key_list_attribute_format
        elif "attribute" in kwargs and "format" in kwargs:
            k_list = self.key_list_attribute_format(kwargs["attribute"], level, operator, kwargs["format"])
        # Call key_list_attribute_pattern
        elif "attribute" in kwargs and "pattern" in kwargs:
            # Build keyword arguments for pattern_for_value
            pfv_kwargs = {}
            if "separators" in kwargs and "strip_list" in kwargs:
                pfv_kwargs.update({"separators": kwargs["separators"]})
                pfv_kwargs.update({"strip_list": kwargs["strip_list"]})
            if "pattern_file" in kwargs:
                pattern_dict = load_json_file(kwargs["pattern_file"])
                pfv_kwargs.update({"pattern_dict": pattern_dict})
            if "pattern_regex_sub_file" in kwargs:
                pattern_regex_sub = load_regex_sub_file(kwargs["pattern_regex_sub_file"])
                pfv_kwargs.update({"pattern_regex_sub": pattern_regex_sub})
            k_list = self.key_list_attribute_pattern(kwargs["attribute"], level, operator, pfv_kwargs, kwargs["pattern"])
        # Call key_list_attribute_with_duplicate_values
        elif "attribute" in kwargs and "duplicate" in kwargs:
            k_list = self.key_list_attribute_with_duplicate_values(kwargs["attribute"], level, kwargs["duplicate"])
        # Call key_list_attribute
        elif "attribute" in kwargs:
            k_list = self.key_list_attribute(level, kwargs["attribute"])
        # Call key_list_value
        elif "value" in kwargs:
            k_list = self.key_list_value(level, kwargs["value"])
        # Use specified list of keys
        elif "keys" in kwargs:
            # For random sampling, build a random key list for the sample size 
            if kwargs["keys"] == "RANDOM":
                all_keys = self.key_list(level)
                k_list = list(set(random.sample(all_keys, k = sample)))
            else:
               k_list = kwargs["keys"]    
        # Call key_list by default
        else:
            k_list = self.key_list(level)
        # Based on option, return the selection as a dict or a list
        if option == "list":
            selection = []
        else:
            selection = {}
        if len(k_list) > 0:
            if option == "list" and attributes == "ALL":
                selection = self.export_as_list(level, k_list)
            elif option == "list":
                selection = self.export_attributes_as_list(attributes, k_list, missing_value)
            elif option == "dict" and attributes == "ALL":
                selection = self.export_as_dict(level, k_list)
            elif option == "dict":
                selection = self.export_attributes_as_dict(attributes, k_list, missing_value)
            # If specified, sort the selected list by a single attribute
            if option == "list" and "sort_attribute" in kwargs:
                selection_header = selection[0]
                selection_data = selection[1::]
                sort_key = selection_header.index(kwargs["sort_attribute"])
                if "sort_reverse" in kwargs:
                    sorted_selection_data = sorted(selection_data, key = lambda row: row[sort_key], reverse = kwargs["sort_reverse"])
                else:
                    sorted_selection_data = sorted(selection_data, key = lambda row: row[sort_key])
                sorted_selection = [selection_header]
                sorted_selection.extend(sorted_selection_data)
                selection = sorted_selection
        return selection

    def assemble(self, assembling_list, missing_value = "", option = "dict"):
        """ 
        Assemble a nested dictionary for ALL KEYS 
                                    based on assembling_list
                                    which has the following structure:
                                    [{"level": <level>, "attribute": <attribute name>, ...]
        """
        assemble_dict = {}
        for key in self.nd:
            attribute_dict = {}
            for assembly in assembling_list:
                level = assembly["level"] 
                attribute = assembly["attribute"]
                if attribute in self.nd[key][level]:
                    attribute_dict.update({attribute: self.nd[key][level][attribute]})
                # If the attribute was not found, output it with missing_value
                else:
                    attribute_dict.update({attribute: missing_value})
            assemble_dict.update({key: attribute_dict})
        # Based on option, return the result as a dict or a list
        if option == "dict":
            assemble_result = assemble_dict
        elif option == "list":
            assemble_list = convert_ndict_to_list(assemble_dict)
            assemble_result = assemble_list
        return assemble_result