
from numpy import loadtxt
expense_report = loadtxt("day1_Expense.txt", unpack=False)
len_expense = len(expense_report)
print ("length is %s " % len_expense)
# part 1
for i in (range(len_expense)):
    x = expense_report[i]
    for j in range(len_expense):
        y = expense_report[j]
        sum_now = x+y
        print(sum_now)
        if (sum_now == 2020.0):
            print('answer found')
            product = x*y
            print(product)
        break

#part 2
expense_report = loadtxt("day1_Expense.txt", unpack=False)
len_expense = len(expense_report)
print ("length is %s " % len_expense)
for i in (range(len_expense)):
    j =i+1
    for j in range(len_expense):
        k = j+1
        for k in range(len_expense):
            if(expense_report[i]+expense_report[j]+expense_report[k] == 2020):
                print("answer found")
                print(expense_report[i]*expense_report[j]*expense_report[k])
                break



