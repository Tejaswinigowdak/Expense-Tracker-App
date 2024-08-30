from feature import search_by_date, sort_amount, add_data, remove_data,sum_amount

transaction =[
    {"date":"2024-08-28","amount":1000,"description":"Fruits"},
    {"date":"2024-08-29","amount":2000,"description":"Dress"},
    {"date":"2024-08-30","amount":3000,"description":"Shoes"},
    {"date":"2024-08-31","amount":5000,"description":"Ear Podes"},
    {"date":"2024-09-01","amount":80000,"description":"Laptop"},
]


flag=True
while flag:
  print("Expense Tracker App")
  print("1.Add Transaction")
  print("2.Search Transaction")
  print("3.Sort Transaction")
  print("4.Delete Transaction")
  print("5.Display Transaction")
  print("6.sum amount")
  print("7.Exit")
  print("-"*50)
  choice = int(input("enter your choice: "))
  if choice == 1:
    print("-"*50)
    print("adding data")
    print("-"*50)
    transaction = add_data(transaction)
    print("-"*50)
  elif choice ==2:
    print("-"*50)
    print("searching data")
    print("-"*50)
    transaction = search_by_amount(transaction)
    print("-"*50)
  elif choice == 3:
    print("-"*50)
    print("removing data")
    print("-"*50)
    transaction = remove_data(transaction)
    print("-"*50)
  elif choice == 4:
    print("-"*50)
    print("sorting data")
    print("-"*50)
    transaction = sort_amount(transaction)
    print("-"*50)
  elif choice == 5:
    print("-"*50)
    print("displaying data")
    print("-"*50)
    print(transaction)
  elif choice == 6:
    print("-"*50)
    print("sum of amount of a given year")
    print(sum_amount(transaction))
    print("-"*50)
  elif choice == 7:
    print("-"*50)
    print("exiting data")
    print("-"*50)
    flag = False
  else:
    print("invalid choice")
    print("-"*50)
