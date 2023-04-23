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


def getSuccessRatio(df, variable_filter):
    pass


def getAverageValue(df: object, data_filter: dict) -> float:
    """_summary_

    Args:
        df (object): Data frame from which the data will be taken.
        data_filter (dict): Contains the testcases as keys and the
                            necessary variables as values.

    Returns:
        float: Calculated average value of the given variable.
    """
    testcase_filter = {}
    df_filtered = filterExcelResults(df, testcase_filter)
    average = list(df_filtered[variable_filter].mean())
    return print(mean(average))


def getMinimumValue(df, variable_filter):
    pass


def getMaximumValue(df, variable_filter):
    pass


def extract_results_from_dataframe(df, variable_filter):
    pass


# Test programm
result_filter = {'Testcase verdict': ['PASSED', 'FAILED'],
                 'Testcase name': ['Testcase_1', 'Testcase_2', 'Testcase_5'],
                 'R_Variable3': list(range(0, 20))
                 }

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
print(all_files)
# Filter all excel files and combine the data to a single data frame
df_all_data = None
for file in all_files:
    df = pd.read_excel(file, sheet_name='Tabelle1')
    df = filterExcelResults(df, result_filter)
    df_all_data = merge_dataframes(df_all_data, df)
print(df_all_data)
# Read the data frame and calculate the desired values
for info in data_filter.items():
    print(info)
getAverageValue(df_all_data, testcase_filter, variable_filter)
