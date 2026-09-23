# student perfomance analyzer
import matplotlib.pyplot as plt
import pandas as pd
data= {
    'Name':["Sushmita","Sammu","Nishmi","Sharanya"],
    'English':[99,100,78,25],
    'Maths':[100,99,95,87],
    'ADA':[65,56,32,74],
    'DBMS':[45,65,78,25],
    'Mongodb':[47,66,28,96],
    'Study_hours':[12,14,13,15]
}
data=pd.DataFrame(data)
data['total_marks']=data[['English','Maths','ADA','DBMS','Mongodb']].sum(axis=1)
print(data)
plt.xlabel("Study_hours")
plt.ylabel("total_marks")
plt.scatter(data['Study_hours'],data['total_marks'])
plt.title("Study hours vs Total marks")
plt.show()
def get_grade(total_marks):
    if total_marks >= 350:
        return 'Sammu'
    elif total_marks >= 400:
        return 'Sushmita'
    else:
        return 'Sharanya'
data['Grade']=data['total_marks'].apply(get_grade)
avg_marks_per_subject=data[['English','Maths','ADA','DBMS','Mongodb']].mean(axis=1)
print(data)
plt.bar(avg_marks_per_subject.index,avg_marks_per_subject.values)
plt.xlabel("Subjects")
plt.ylabel("Average marks")
plt.title("Average marks per subject")
plt.show()