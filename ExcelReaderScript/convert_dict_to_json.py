import json

default_settings = {
    'Setting_1': {
                 "json_file": "C:/Users/Michael/Desktop/mwtestcodes/ExcelReaderScript/filter.json",
                 "results_folder": "C:/Users/Michael/Desktop/mwtestcodes/ExcelReaderScript",
                 "template_file": "C:/Users/Michael/Desktop/mwtestcodes/ExcelReaderScript/EvaluationExcel.xlsx",
                 "location_report": "C:/Users/Michael/Desktop/mwtestcodes/Report_Folder",
                 "report_name": "Report_1",
                 "testbenches": ["SYS-112.tbc", "SYS-110.tbc"]
    },
    'Setting_2': {
                 "json_file": "",
                 "results_folder": "",
                 "template_file": "",
                 "location_report": "",
                 "report_name": "",
                 "testbenches": [""]
    }
}


filters = {
    'result_filter': {
        'Testcase verdict': ['PASSED', 'FAILED'],
        'testbench': ['SYS-110.tbc', 'SYS-112.tbc']
        },
    'data_filter': {
        'First result info': (['average_min_max', 'experienceable_ratio'],
                              {'Testcase_1': 'R_Variable3',
                               'Testcase_2': 'R_Variable2'}),
        'Second result info': (['average_min_max', 'experienceable_ratio'],
                               {'Testcase_5': 'R_Variable4'}),
        'Third result info': (['value_occurence'],
                              {'Testcase_8': 'R_Variable5'})
        }
}


with open('default_settings.json', 'w') as f:
    json.dump(default_settings, f, indent=4)
    print(f)

# with open('filter.json', 'r') as rf:
#     data = json.load(rf)
#     print(data)
#     data['result_filter']['Test_Key'] = 'test_value'
#     print(data)


# with open('filter.json', 'r') as rf:
#     filter_data = rf.read()
#     json_data = json.loads(filter_data)

# pprint.pprint(json_data)
