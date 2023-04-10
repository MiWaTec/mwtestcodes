import pandas as pd
import statistics
import os

def readExcelFiles():
    file_list = os.listdir()
    excel_list = []
    for file in file_list:
        if file[-4:] == 'xlsx':
            excel_list.append(file)
    return excel_list

def filterExcelResults():
    pass

    

readExcelFiles()

filterExcelResults()