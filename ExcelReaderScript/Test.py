
import pandas as pd


# def write_dataframes_to_excel(df1, df2, file_name):
#     # Erstelle einen Excel-Writer
#     writer = pd.ExcelWriter(file_name, engine='xlsxwriter')

#     # Schreibe die DataFrames in separate Arbeitsblätter
#     df1.to_excel(writer, sheet_name='DataFrame1', index=False)
#     df2.to_excel(writer, sheet_name='DataFrame1', index=False, startrow=len(df1) + 2)  # Starte unterhalb von df1

#     # Erhalte das xlsxwriter-Objekt, um die Arbeitsblätter anzupassen
#     # workbook = writer.book
#     # worksheet1 = writer.sheets['DataFrame1']
#     # worksheet2 = writer.sheets['DataFrame2']

#     # Füge Formatierungen hinzu, um die Überschrift zu betonen
#     # header_format = workbook.add_format({'bold': True, 'text_wrap': True, 'align': 'center', 'valign': 'vcenter'})
#     # worksheet1.set_row(0, None, header_format)
#     # worksheet2.set_row(0, None, header_format)

#     # Schließe den Excel-Writer
#     writer.save()

# # Beispiel DataFrames
# data1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
# data2 = {'X': [7, 8, 9], 'Y': [10, 11, 12]}
# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)

# # Dateinamen
# excel_file_name = 'dataframes_combined.xlsx'

# # Rufe die Funktion auf, um die DataFrames in die Excel-Datei zu schreiben
# write_dataframes_to_excel(df1, df2, excel_file_name)

# def transform_strings_to_list(lst_string):
#     value_list = []
#     lst_string = lst_string[1:-1]
#     start = 0
#     end = 0
#     while end != len(lst_string)-1:
#         start = lst_string.find('[')
#         end = lst_string.find(']')
#         if end == -1:
#             break
#         string = lst_string[start+2:end].replace("'", "").split(',')
#         value_list.append(string)
#         lst_string = lst_string[end+1:]
#     print(value_list)
#     return value_list
def extractValuesFromListOfStringLists(value_list, key, *args):
    # Extract lists from the string lists and combine them to a single list
    extracted_value_list = []
    for string_value in value_list:
        transformed_list = transformStringListsToList(string_value)
        for list_value in transformed_list:
            if list_value[0] == key:
                extracted_value_list.append(float(list_value[1]))
            else:
                extracted_value_list.append(None)
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


lists = []
key = 'Test'
list_yo = ["[['Willkommen', 3.786], ['Test', 1.234]]", "[['Willkommen', 5.786]]", "[['Willkommen', 2.786]]"]
print(isinstance(list_yo[0], str))
print(list_yo[0][:2])
val_list = extractValuesFromListOfStringLists(list_yo, key)
print(val_list)

import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))