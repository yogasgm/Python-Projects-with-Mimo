data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

def print_transactions(transactions):
  for transaction in transactions:
    amount = transaction[0]
    statement = transaction[1]
    print(f"${amount} - {statement}")

def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposited = sum(deposits)
  print(f"Total Deposited: {total_deposited}")

  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdrawn = sum(withdrawals)
  print(f"Total Withdrawn: {total_withdrawn}")

  balance = total_deposited + total_withdrawn
  print(f"Balance: {balance}")

def analyze_transactions(transactions):
  transactions.sort()
  largest_withdrawal = transactions[0]
  largest_deposit = transactions[-1]
  print(f"Your Largest Withdrawal: {largest_withdrawal}")
  print(f"Your Largest Deposit: {largest_deposit}")

  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposit = sum(deposits)
  try:
    average_deposit = total_deposit/len(deposits)
  except:
    average_deposit = 0
  print(f"Average Deposit: {average_deposit}")

  withdrawals = [transaction[0] for transaction in transactions if transaction[0] <= 0]
  total_withdrawals = sum(withdrawals)
  try:
    average_withdrawals = total_withdrawals/len(withdrawals)
  except:
    average_withdrawals = 0
  print(f"Average Withdrawal: {average_withdrawals}")

while True:
  print("\nOptions: print/analyze/stop")
  choice = input("Type: ").strip().lower()

  if choice == "print":
    print("\nOutput:")
    print_summary(data)
  elif choice == "analyze":
    print("\nOutput:")
    analyze_transactions(data)
  elif choice == "stop":
    print("\nThank You")
    break
  else:
    print("\nInvalid choice")