
def invalid_loan(number) -> bool:
    if float(number) == 0.0 or float(number) < 0:
        print("Loan cannot be 0 or negative number.")
        return False 
    try: 
        float(number)
    except (TypeError, ValueError):
        return True # invalid number
    
    return False # Valid number

def invalid_loan_or_apr(number) -> bool:
    if float(number) < 0:
        print("This cannot be a negative number.")
        return False 
    try:
        float(number)
    except (TypeError, ValueError):
        return True # invalid number
    
    return False # Valid number

while True:
    # cannot be a negative number, str, or 0 
    loan_amt = input("Enter loan amount: ")
    while invalid_loan(loan_amt):
        print("Invalid number entered. Try again.")
        loan_amt = input("Enter loan amount: ")

    # cannot be a negative number, str
    apr_rate = input("Enter your APR rate in percent (ex: 5%, enter 5): ") 
    while invalid_loan_or_apr(apr_rate):
        print("Invalid number entered. Try again.")
        apr_rate = input("Enter your APR rate in percent (ex: 5%, enter 5): ")

    # cannot be a negative number, str
    loan_duration = input("Enter the loan duration in months: ")
    while invalid_loan_or_apr(loan_duration):
        print("Invalid number entered. Try again.")
        loan_duration = input("Enter the loan duration in months: ")

    monthly_interest_rate = float(apr_rate) / 12 / 100

    monthly_pay = float(loan_amt) * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-1 * int(loan_duration))))
    print(f"Monthly payment will be {monthly_pay}")

    print("Another calculation?")
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break 
        
        print('Please enter "y" or "n".')
        answer = input().lower()
        
    if answer[0] == 'n':
        break