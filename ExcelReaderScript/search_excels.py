import os


def readExcelFiles(folder_path) -> list:
    """This function returns a list of all excel files that are in the same
       folder.

    Returns:
        excel_list (list): List that contains all excel file names in the
                           folder as strings.
    """
    excel_list = []
    for folder, subfolder, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.xlsx') or file.endswith('.xls'):
                excel_list.append(os.path.join(folder, file))
    return excel_list


excels = readExcelFiles(r"C:\Users\Michael\Desktop\mwtestcodes\ExcelReaderScript")
print(excels)
