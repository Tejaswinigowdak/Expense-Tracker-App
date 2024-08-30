def search_by_date(transaction,target_date):
  for transaction in transaction:
    if transaction["date"] == target_date:
      return transaction
  return"transaction not found"

def sort_amount(transaction):
  n=len(transaction)
  for i in range(n):
    for j in range(0,n-i-1):
      if transaction[j]['amount'] > transaction[j+1]['amount']:
        transaction[j],transaction[j+1] = transaction[j+1],transction[j]
  return transaction

def add_data(transaction):
   date = input("enter date: ")
   amount = int(input("enter amount: "))
   description = input("enter description: ")
   transaction.append({"date":date,"amount":amount,"description":description})
   return transaction

def remove_data(transaction):
   date = input("enter date: ")
   amount = int(input("enter amount: "))
   description = input("enter description: ")
   transaction.remove({"date":date,"amount":amount,"description":description})
   return transaction

def sum_amount(transaction):
  sum = 0
  year = input("enter year: ")
  for i in transaction:
    if i['date'][0:4] == year:
      sum += i['amount']
  return sum
