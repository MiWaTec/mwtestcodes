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

def transform_strings_to_list(lst_string):
    value_list = []
    lst_string = lst_string[1:-1]
    start = 0
    end = 0
    while end != len(lst_string)-1:
        start = lst_string.find('[')
        end = lst_string.find(']')
        if end == -1:
            break
        string = lst_string[start+2:end].replace("'", "").split(',')
        value_list.append(string)
        lst_string = lst_string[end+1:]
        print(lst_string)
    return value_list


lists = []
list_yo = ["[['Willkommen', 3.786], ['Test', 1.234]]", "[['Willkommen', 5.786]]", "[['Willkommen', 2.786]]"]
for lst_string in list_yo:
    value_list = transform_strings_to_list(lst_string)
    print(value_list)
    lists += value_list
print(lists)
