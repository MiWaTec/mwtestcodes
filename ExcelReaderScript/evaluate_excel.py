import pandas as pd
from statistics import mean
import os


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


def extractValuesFromDataframe(df: object, result_filter: dict,
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
    pass


def getAverageValue(value_list):
    pass


def getMinimumValue(value_list):
    pass


def getMaximumValue(value_list):
    pass


def getSuccessRatio(value_list):
    pass


# Test programm
result_filter = {'Testcase verdict': ['PASSED', 'FAILED']}

testcase_filter = {
    'Testcase name': ['Testcase_1', 'Testcase_5'],
}

variable_filter = ['R_Variable3', 'R_Variable4']

data_filter = {
    'First result info': (['maximum_value', 'minimum_value', 'average_value'],
                          {'Testcase_1': 'R_Variable3',
                          'Testcase_2': 'R_Variable2'}),
    'Second result info': (['maximum_value', 'minimum_value', 'average_value'],
                           {'Testcase_5': 'R_Variable4'})
}

# Legende:
#   maximum_value
#   minimum_value
#   average_value
#   amount_of_true


# Search for excel files and save them in a list
all_files = readExcelFiles()
# Filter all excel files and combine the data to a single data frame
df_all_data = None
for file in all_files:
    df = pd.read_excel(file, sheet_name='Tabelle1')
    df_all_data = merge_dataframes(df_all_data, df)
    print(df_all_data)
# Read the data frame and calculate the desired values
for info in data_filter:
    extracted_values = extractValuesFromDataframe(df_all_data, result_filter,
                                                  data_filter[info][1])
    print(extracted_values)
