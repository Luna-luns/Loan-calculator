import math


def ask_loan() -> int:
    print('Enter the loan principal:')
    return int(input())


def define_what_calculate() -> str:
    print('''What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:''')
    return input()


def choose_parameter(_type) -> int:
    if _type == 'm':
        print('Enter the monthly payment:')
    else:
        print('Enter the number of months:')
    return int(input())


def evaluate_monthly_payment(principal: int, months: int) -> int:
    return math.ceil(principal / months)


def evaluate_last_payment(principal: int, months: int, payment: int) -> int:
    return principal - (months - 1) * math.ceil(payment)


def evaluate_month_number(principal: int, payment: int) -> int:
    return math.ceil(principal / payment)


user_loan = ask_loan()
type_char = define_what_calculate()
parameter_to_calculate = choose_parameter(type_char)
if type_char == 'm':
    month_number = evaluate_month_number(user_loan, parameter_to_calculate)
    if month_number == 1:
        print('It will take 1 month to repay the loan')
    else:
        print('It will take', month_number, 'months to repay the loan', sep=' ')
else:
    monthly_payment = evaluate_monthly_payment(user_loan, parameter_to_calculate)
    last_payment = evaluate_last_payment(user_loan, parameter_to_calculate, monthly_payment)
    if monthly_payment == last_payment:
        print('Your monthly payment =', monthly_payment, sep=' ')
    else:
        print('Your monthly payment =', monthly_payment, 'and the last payment =', last_payment)
