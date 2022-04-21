import pandas as pd 
import matplotlib.pyplot as plt 

headers = ["Date","Category","Expense","Type"]
df = pd.read_csv('Sample data.csv', usecols=headers)

#Insert Month
print("Insert Month")
month=input()

#storing data
data_plot = []
label_plot = []
amount_of_data = len(df.Date)

for row in range(len(df.Date)):
    if month == df.Date[row][3:5]:
        if df.Expense[row] <= 0:
            selected_Category = df.Category[row]
            selected_Expense = abs(int((df.Expense[row])))

            data_plot.append(selected_Expense)
            label_plot.append(selected_Category)

            print (selected_Category)
            print (selected_Expense)
        else :
            pass
#setting graph.
plt.pie(data_plot, labels = label_plot, autopct='%d%%')

#show graph
plt.show()

print (df)