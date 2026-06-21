	print("YOU HAVE THREE ATTEMPTS TO ENTER YOUR PIN")
attempts = 3
pin = input("Enter your pin : ")
if pin == "1234" :
           print("LOGIN SUCCESSFUL") 
while pin != "1234" and attempts > 0:
        attempts-=1 
        print(f"INCORRECT PIN. {attempts} attempts left.")
        pin = input("Enter your pin : ")
        if pin == "1234" :
           print("LOGIN SUCCESSFUL")
if attempts == 0:
      print("ACCOUNT BLOCKED")

balance = 5000
print("1.Check balance")
print("2.Deposit")
print("3.Withdraw")
print("4.Exit")
while True :
      choice = input("Enter your choice: ")
      if choice == "1" :
         print(f"Your balance is {balance}.")
      elif choice == "2" :
         deposit_amount = int(input("Enter amount to deposit : "))
         print("Deposit Successful")
         balance += deposit_amount
         print(f"Your current balance is {balance}.")
      elif choice == "3" :
            withdraw =  int(input("Enter amount to withdraw : "))
            if withdraw <= balance :
              print("Withdrawal successful")
              balance -= withdraw
              print(f"Your current balance after your withdrawal is {balance}.")
            else :
             print("Insufficient balance")  
      elif choice == "4" :
            print("Thank you!")
            break
      else :
            print("Invalid choice")
