import pandas as pd
import statistics

cols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# df = pd.read_excel('Testcase_1_date.xlsx', sheet_name='Tabelle1', usecols=cols)
df = pd.read_excel('Testcase_1_date.xlsx')
a = df.head()
print(df)

a = df.query('`Testcase verdict` in ["PASSED", "FAILED"]')
b = df.query('`Testcase verdict` in ["PASSED"]')
a._set_value(16, 'File name', 14)
writer = pd.ExcelWriter('Output2.xlsx', engine='xlsxwriter')
a.to_excel(writer, sheet_name="Tabelle1", index=False)
b.to_excel(writer, sheet_name="Tabelle1", startrow=20, header=False, index=False)
writer.save()


# df_filtered = df["Testcase verdict"] != "ERROR"
# df_filtered_2 = df.R_Variable1.isin(["PASSED", "FAILED"])
# print(df_filtered_2)

value_list = []

for row in a.iterrows():
    pos, d = row
    print(pos)
    print(d)
    print(d["Testcase verdict"])
    print(d["R_Variable6"])
    value_list.append(d["R_Variable6"])

print(value_list)
print(sum(value_list) / len(value_list))
print(statistics.mean(value_list))
