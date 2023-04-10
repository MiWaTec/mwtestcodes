import pandas as pd
# import statistics
import os


def readExcelFiles():
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


def filterExcelResults(excel_file, filter):
    df = pd.read_excel(excel_file, sheet_name='Tabelle1')
    for filter_element in filter.items():
        header, value = filter_element
        if ' ' in header:
            header = '`' + header + '`'
        df.query('{0} in {1}'.format(header, value), inplace=True)
    return df


result_filter = {'Testcase verdict': ['PASSED', 'FAILED'],
                 'Testcase name': ['Testcase_1', 'Testcase_2', 'Testcase_5'],
                 'R_Variable3': list(range(0, 3))
                 }

readExcelFiles()
df_test = filterExcelResults('Testcase_1_date.xlsx', result_filter)
print(df_test)
