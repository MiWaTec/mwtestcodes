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
    return mean(filtered_list)


def getMinValue(value_list, *args):
    filtered_list = [float(x) for x in value_list if float(x) >= 0]
    return min(filtered_list)


def getMaxValue(value_list, *args):
    filtered_list = [float(x) for x in value_list if float(x) >= 0]
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


def OccurenceValueInList(value_list, key):
    occurence_dict = countListElements(value_list)
    total = occurence_dict.get(key)
    return total


def getLengthOfList(value_list, *args):
    return len(value_list)


def extractValuesFromListOfLists():
    pass
