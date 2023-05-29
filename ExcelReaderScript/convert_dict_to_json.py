import json

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


with open('filter.json', 'w') as f:
    json.dump(filters, f, indent=4)
    print(f)

with open('filter.json', 'r') as rf:
    data = json.load(rf)
    print(data)
    data['result_filter']['Test_Key'] = 'test_value'
    print(data)


# with open('filter.json', 'r') as rf:
#     filter_data = rf.read()
#     json_data = json.loads(filter_data)

# pprint.pprint(json_data)
