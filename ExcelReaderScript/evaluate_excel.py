import pandas as pd
from statistics import mean
import os
import json


def readExcelFiles() -> list:
    """This function returns a list of all excel files that are in the same
       folder.

    Returns:
        excel_list (list): List that contains all excel file names in the
                           folder as strings.
    """
    file_list = os.listdir()
    excel_list = []
    for file in file_list:
        if file[-4:] == 'xlsx':
            excel_list.append(file)
    return excel_list


def filterExcelResults(df: object, result_filter: dict) -> object:
    """This function reads the given excel file and filters the content
       based on the given filter. The filtered data frame will be returned.

    Args:
        excel_file (str): Name of the excel file.
        result_filter (dict): Filter as dictionary with header name as key
                              and the value as value.

    Returns:
        object: Filtered data frame.
    """
    for filter_element in result_filter.items():
        header, value = filter_element
        if ' ' in header:
            header = '`' + header + '`'
        df.query('{0} in {1}'.format(header, value), inplace=True)
    return df


def merge_dataframes(df1: object, df2: object) -> object:
    """This function concatenates two data frames.

    Args:
        df1 (object): First data frame.
        df2 (object): Second data frame.

    Returns:
        object: Combined data frame of df1 and df2.
    """
    df_merged = pd.concat([df1, df2], ignore_index=True, sort=False)
    return df_merged


def extractValuesFromDf(df: object, result_filter: dict,
                        tc_var_dict: dict) -> list:
    """This function filters the dataframe based on the given filters.
       The result_filter will filter all relevant data from the dataframe.
       With the tc_var_dict the desired data of the dataframe will be extracted
       and saved into a list.

    Args:
        df (object): Dataframe from which the data will be extracted.
        result_filter (dict): Dictionary with the dataframe headers as keys and
                              desired values as values.
        tc_var_dict (dict): Dictionary with the testcase names as keys and
                            variable names as values.

    Returns:
        list: List that contains all extracted values.
    """
    value_list = []
    for testcase in list(tc_var_dict.keys()):
        result_filter['Testcase name'] = [testcase]
        df2 = df.copy()
        df_filtered = filterExcelResults(df2, result_filter)
        average = list(df_filtered[tc_var_dict[testcase]])
        value_list = value_list + average
    return value_list


def getTotalAmountOfValues(value_list):
    return len(value_list)


def getSuccessRatio(value_list: list) -> int:
    """This function calculates the percentage of values
       that indicates successful results. A value is considered
       a success if it is True or greater than 0.

    Args:
        value_list (list): List of values.

    Returns:
        int: Percentage of successful values.
    """
    total = len(value_list)
    success = 0
    for value in value_list:
        if value in [True, 'True'] or value > 0:
            success += 1
    return round(success / total * 100)


def getAverageMinMax(value_list: list) -> tuple:
    """This function calculates the average value of a list of numbers.
       In addition, the minimum and the maximum value of the list will
       be determined. Before the calculation, all values less than 0 are
       removed from the list.

    Args:
        value_list (list): List of numeric values.

    Returns:
        tuple: Tuple that contains the average value, minimum value and
               maximum value: (average, min, max)
    """
    filtered_list = [x for x in value_list if x >= 0]
    average_value = mean(filtered_list)
    min_value = min(filtered_list)
    max_value = max(filtered_list)
    return {'average': average_value, 'min': min_value, 'max': max_value}


def countListElements(value_list: list) -> dict:
    """This function combines the list of lists (the inner lists are present as
       strings which will be converted to lists) to a single list and counts
       the number of occurences of each element in the merged list.

    Args:
        value_list (list): List of lists in string format.

    Returns:
        dict: Dictionary that contains all elements of the merged list as keys
              and its occurences as values.
    """
    # Combine the list of lists to a single list
    merged_lists = []
    for list_of_values in value_list:
        if '[' in list_of_values and ']' in list_of_values:
            converted_list = list_of_values.strip('][').split(', ')
            merged_lists = merged_lists + converted_list
    # Count the occurrence of all elements in the list
    occurence_dict = {}
    all_elements = set(merged_lists)
    for element in all_elements:
        count = merged_lists.count(element)
        occurence_dict[element] = count
    return occurence_dict


def read_filter_json(json_file_name: str) -> dict:
    """This function opens a given json file and returns the filter data
       as dictionary.

    Args:
        json_file_name (str): Name of the json file or path of the file.

    Returns:
        dict: Dictionary provided by the json file that contains the filters.
    """
    with open(json_file_name) as f:
        data = json.load(f)
    return data


def save_filter(filter_file: str, filter_type: str, key: str, value: str,
                state: int):
    """This function reads the filter json file and compares the value of
       the given key of the given filter type with the current value state
       in the UI and changes the value in the filter json file according to
       the value in the UI.

    Args:
        filter_file (str): Name or path of the json file.
        filter_type (str): Name of the filter type which is a key of the
                           dictionary that is provided from the json file.
        key (str): Key of the dictionary of the choosen filter type.
        value (str): Value of the choosen key.
        state (int): Desired or current state of the UI element. If the state
                     is 0, the key will be removed from the filter json file.
                     If the state is 1, the key will be left in the filter
                     json file.
    """
    # Read json file
    data = read_filter_json(filter_file)
    # Modify data of the json file
    value_list = data[filter_type][key]
    print(value_list)
    if value in value_list and state == 0:
        value_list.remove(value)
        print(value_list)
    elif value not in value_list and state == 1:
        value_list.append(value)
    print(value_list)
    data[filter_type][key] = value_list
    print(data)
    # Overwrite json file with new data
    with open('filter.json', 'w') as f:
        json.dump(data, f, indent=4)


def save_default_settings(settings_file: str, key: str, val):
    """This function opens the given settings file and converts the
       json data into a dict. The value of the given key will be
       overwritten with the given value. Afterwards the changed data
       will be converted to a json file again.

    Args:
        settings_file (str): File name or file path that will be used.
        key (str): Key of the dictionary whose value will be changed.
        val (_type_): New value that will overwrite the value of the
                      given key.
    """
    # Read json file
    settings_dict = read_filter_json(settings_file)
    # Modify data of the json file
    settings_dict[key] = val
    with open(settings_file, 'w') as f:
        json.dump(settings_dict, f, indent=4)


def calculate_results(filter_data: dict) -> dict:
    """This function calculates the desired values that are given by the
       filter_data dictionary. The calculated results will be returned as
       a dictionary.

    Args:
        filter_data (dict): Dictionary that contains the infos to be
                            calculated.

    Returns:
        dict: Dictionary that contains a dictionary with the calculared values
              for each info.
    """
    # Mapping of the info names and their functions
    func_mapping = {'average_min_max': getAverageMinMax,
                    'value_occurence': countListElements,
                    'experienceable_ratio': getSuccessRatio,
                    'total': len}
    # Search for excel files and save them in a list
    all_files = readExcelFiles()
    # Filter all excel files and combine the data to a single data frame
    df_all_data = None
    for file in all_files:
        df = pd.read_excel(file)
        df_all_data = merge_dataframes(df_all_data, df)
        print(df_all_data)
    # Read the data frame and calculate the desired values
    result_dict = {}
    for info in filter_data['data_filter']:
        # Filter the data necessery for the calculation of current info
        extracted = extractValuesFromDf(df_all_data,
                                        filter_data['result_filter'],
                                        filter_data['data_filter'][info][1])
        # Create a dict that will contain the calculated values of the info
        info_dict = {}
        # Create a list of functions that will be used for the calculations
        list_of_desired_values = filter_data['data_filter'][info][0]
        print(list_of_desired_values)
        # Calculate all values of list_of_desired_values
        for val in list_of_desired_values:
            calculated_result = func_mapping[val](extracted)
            print(calculated_result)
            info_dict[val] = calculated_result
        # Add the calculated results of the info to the return dict
        result_dict[info] = info_dict
    print(result_dict)
    return result_dict
