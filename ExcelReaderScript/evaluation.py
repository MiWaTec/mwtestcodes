import pandas as pd
import statistics

cols = [0, 1, 2, 3, 4, 5, 6, 7]
df = pd.read_excel('Testcase_1_date.xlsx', sheet_name='Tabelle1', usecols=cols)
a = df.head()
print(df)

a = df.query('`Testcase verdict` in ["PASSED", "FAILED"]')
writer = pd.ExcelWriter('Output2.xlsx', engine='xlsxwriter')
a.to_excel(writer, sheet_name="Tabelle1", index=False)
writer.save()


#df_filtered = df["Testcase verdict"] != "ERROR"
#df_filtered_2 = df.R_Variable1.isin(["PASSED", "FAILED"])
#print(df_filtered_2)

value_list = []

for row in a.iterrows():
    pos, d = row
    print(pos)
    print(d["Testcase verdict"])
    print(d["R_Variable3"])
    value_list.append(d["R_Variable3"])

print(value_list)
print(sum(value_list) / len(value_list))
print(statistics.mean(value_list))

