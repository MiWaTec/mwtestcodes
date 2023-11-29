from statistics import mean


def getFunctionDict():
    functions = {'Average value': getAverageValue,
                 'Minimum value': getMinValue,
                 'Maximum value': getMaxValue,
                 'Occurrence of each value': countListElements,
                 'Experienceable ratio': getSuccessRatio,
                 'Number of success': getSuccessNumber,
                 'Total number of values': getLengthOfList,
                 'Occurrence of selected value': OccurenceValueInList}
    return functions


def getFunctionDesciption(func_name):
    desciptions = {'Average value': 'Calculates the average value.',
                   'Minimum value': 'Returns the minimum value.',
                   'Maximum value': 'Returns the maximum value.',
                   'Occurrence of each value': 'Counts the number of\
                                                occurrences of each element\
                                                and returns a dictionary with\
                                                the elements as keys and the\
                                                number of occurrences as\
                                                values. This function should\
                                                be used only for the\
                                                calculation of the not reached\
                                                menues in the main menue\
                                                testcase.',
                   'Experienceable ratio': 'Calculates the percentage of\
                                            values that indicates succesful\
                                            results. A value is considered a\
                                            success if it is True or greater\
                                            than 0.',
                   'Number of success': 'Calculates the number of values that\
                                         indicates succesful results. A value\
                                         is considered a success if it is True\
                                         or greater than 0.',
                   'Total number of values': 'Returns the total number of\
                                              values.',
                   'Occurrence of selected value': 'Returns the number of\
                                                    occurences of a selected\
                                                    value. This function is\
                                                    made for the output values\
                                                    of the HandlePopups.pkg'}
    return desciptions[func_name]


def getSuccessRatio(value_list: list, *args) -> int:
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
        try:
            value = float(value)
        except ValueError:
            pass
        if value in [True, 'True', '[]']:
            success += 1
        elif value in [None, 'None', False, 'False']:
            continue
        elif value > 0:
            success += 1
    return round(success / total * 100)


def getSuccessNumber(value_list: list, *args) -> int:
    """This function calculates the number of values
       that indicates successful results. A value is considered
       a success if it is True or greater than 0.

    Args:
        value_list (list): List of values.

    Returns:
        int: Number of successful values.
    """
    success = 0
    for value in value_list:
        try:
            value = float(value)
        except ValueError:
            pass
        if value in [True, 'True', '[]']:
            success += 1
        elif value in [None, 'None', False, 'False']:
            continue
        elif value > 0:
            success += 1
    return success


def getAverageMinMax(value_list: list, *args) -> tuple:
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


def getAverageValue(value_list, *args):
    filtered_list = [float(x) for x in value_list if float(x) >= 0]
    if len(filtered_list) == 0:
        return None
    else:
        return mean(filtered_list)


def getMinValue(value_list, *args):
    filtered_list = [float(x) for x in value_list if float(x) >= 0]
    if len(filtered_list) == 0:
        return None
    else:
        return min(filtered_list)


def getMaxValue(value_list, *args):
    filtered_list = [float(x) for x in value_list if float(x) >= 0]
    if len(filtered_list) == 0:
        return None
    else:
        return max(filtered_list)


def countListElements(value_list: list, *args) -> dict:
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


def OccurenceValueInList(value_list, key, *args):
    occurence_dict = countListElements(value_list)
    total = occurence_dict.get(key)
    return total


def getLengthOfList(value_list, *args):
    return len(value_list)


def extractValuesFromListOfStringLists(value_list, key, *args):
    # Transform string lists to lists and combine them to a single list
    extracted_value_list = []
    for string_value in value_list:
        transformed_list = transformStringListsToList(string_value)
        # Add None to list if transformed_list is empty
        if len(transformed_list) < 1:
            extracted_value_list.append(-1)
            continue
        # Extract the values of the given key from the transformed list
        for list_value in transformed_list:
            if list_value[0] == key.replace("'", ""):
                extracted_value_list.append(float(list_value[1]))
            else:
                extracted_value_list.append(-1)
    return extracted_value_list


def transformStringListsToList(string_list):
    value_list = []
    string_list = string_list[1:-1]
    start = 0
    end = 0
    while end != len(string_list)-1:
        start = string_list.find('[')
        end = string_list.find(']')
        if end == -1:
            break
        string = string_list[start+2:end].replace("'", "").split(',')
        value_list.append(string)
        string_list = string_list[end+1:]
    return value_list
