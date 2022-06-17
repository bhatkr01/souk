# import pandas as pd
# technologies   = ({
#     'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python"],
#     'Fee' :[22000,25000,23000,24000,26000,25000,25000,22000],
#     'Duration':['30days','50days','35days','40days','60days','35days','55days','50days'],
#     'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
#                 })
# df = pd.DataFrame(technologies, columns=['Courses','Fee','Duration','Discount'])
# df1 = df.groupby(['Courses'])['Courses'].count()
# a=[1,2,3,4,5]
# for i,row in df1.items():
#     print(i,row)
#     # print(row/a[i])
# df2 = df.groupby(['Courses'])['Courses'].count()/2
# print(df1)
# print(df2)
import re
txt="8-12 hours"
print(re.split('-| ',txt))
print(txt)
print(max([int(s) for s in re.split('-| ',txt) if s.isdigit()]))
