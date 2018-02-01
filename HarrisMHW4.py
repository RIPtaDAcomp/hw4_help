#===================================================================================================
# Program:      ATM Program
# Programmer:   Matthew Harris
# Date:         01/29/2018
# Abstract:     This program is a simulation of an ATM. It will process deposits,
#               withdrawls, and invalid transaction codes, and provide a current
#               balance.
#===================================================================================================


# The main function definition.
def main():
    
    # These statements ask for user inputs and will display and use in calculations.
    name = input("What is your name? ")
    account_id = input("What is your account ID? ")
    transaction_code = input("Press W or w for withdrawal, Press D or d for deposit. ")
    previous_balance = float(input("What is your previous balance? "))
    transaction_amount = float(input("How much is the transaction amount? "))
    
    # This if condition allows for a withdrawl and calls the process_withdrawal function.
    if transaction_code == "W" or transaction_code == "w":
        process_withdrawal(name, account_id, transaction_code, transaction_amount, previous_balance)
    
    # This elif condition allows for a deposit and it calls the process_deposit function.
    elif transaction_code == "D" or transaction_code == "d":
        process_deposit(name, account_id, previous_balance, transaction_code, transaction_amount)
     
    # This else condition is if they do not meet the previous if or elif condition and calls the 
    # process_invalid_transaction function.
    else:
        process_invalid_transaction(name, account_id, previous_balance)
    
# This definition function defines the withdrawl process  
def process_withdrawal(name, account_id, transaction_code, transaction_amount, previous_balance):
    
    # This if condition describes what happens when there are not enough funds for the transaction
    if transaction_amount > previous_balance:
        print("Withdrawal exceeds previous balance. ")
        new_balance = previous_balance
        print_balance(name, account_id, new_balance)
    
    # This else condition will allow a person to do a withdrawal since they did not meet the prior 
    # if condition in this function.
    else:
        new_balance = previous_balance - transaction_amount
        print_balance(name, account_id, new_balance)
    
# This function takes the user through the proces of procesing a deposit.         
def process_deposit(name, account_id, transaction_code, previous_balance, transaction_amount):
    new_balance = previous_balance + transaction_amount
    print_balance(name, account_id, new_balance)

# This function takes the user to a error message if they type invalid input for doing a withdrawal
# or a deposit.
def process_invalid_transaction(name, account_id, previous_balance):
    print("Invalid transaction type")
    new_balance = previous_balance
    print_balance(name, account_id, new_balance)
        
# This function will show the user their input of their name and account id. It also displays their new
# balance after the transaction. 

def print_balance(name, account_id, new_balance):
    print("Hello", name)
    print("Your account ID is", account_id)
    print("Your new balance is $",
          format(new_balance, ',.2f'), \
          sep='')

# Call the main function.         
main ()

input('Press Enter to continue')
