import pandas as pd
from statistics import mean
import os


def readExcelFiles() -> list:
    """This function returns a list of all excel files that are in the same
       folder.

    Returns:
        list: List that contains all excel file names in the folder as strings.
    """
    file_list = os.listdir()
    excel_list = []
    for file in file_list:
        if file[-4:] == 'xlsx':
            excel_list.append(file)
    return excel_list


def filterExcelResults(df, result_filter) -> object:
    """This function reads the given excel file and filters the content
       based on the given filter. The filtered data frame will be returned.

    Args:
        excel_file (str): Name of the excel file.
        filter (dict): Filter as dictionary with header name as key and
                       the value as value.

    Returns:
        object: Filtered data frame.
    """
    for filter_element in result_filter.items():
        header, value = filter_element
        if ' ' in header:
            header = '`' + header + '`'
        df.query('{0} in {1}'.format(header, value), inplace=True)
    return df


def merge_exel_files_to_dataframe(df1, df2):
    df_merged = pd.concat([df1, df2], ignore_index=True, sort=False)
    return df_merged


def getSuccessRatio(df, variable_filter):
    pass


def getAverageValue(df, testcase_filter, variable_filter):
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


all_files = readExcelFiles()
print(all_files)
df_all_data = None
for file in all_files:
    df = pd.read_excel(file, sheet_name='Tabelle1')
    df = filterExcelResults(df, result_filter)
    df_all_data = merge_exel_files_to_dataframe(df_all_data, df)
print(df_all_data)
getAverageValue(df_all_data, testcase_filter, variable_filter)
