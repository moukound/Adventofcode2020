from numpy import loadtxt
expense_report = loadtxt("C:\\CVE\\Python_stuff\\Advent_Of_Code\\day1_Expense.txt", unpack=False)
len_expense = len(expense_report)
print ("length is %s " % len_expense)
for i in (range(len_expense)):
    x = expense_report[i]
    needed_ans = 2020 - x
    for j in range(len_expense):
        y = expense_report[j]
        if(y == needed_ans) :
            product = x*y
            print(product)
            break


