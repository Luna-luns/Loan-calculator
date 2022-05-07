import math


def ask_loan() -> int:
    print('Enter the loan principal:')
    return int(input())


def ask_monthly_payment() -> int:
    print('Enter the monthly payment:')
    return int(input())


def ask_number_of_periods() -> int:
    print('Enter the number of periods:')
    return int(input())


def ask_loan_interest() -> float:
    print('Enter the loan interest:')
    return float(input()) / (12 * 100)


def ask_annuity_payment() -> float:
    print('Enter the annuity payment:')
    return float(input())


def define_what_calculate() -> str:
    print('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:''')
    return input()


def choose_parameter(_type: str) -> list:
    if _type == 'p':
        return [ask_annuity_payment(), ask_number_of_periods(), ask_loan_interest()]
    if _type == 'a':
        return [ask_loan(), ask_number_of_periods(), ask_loan_interest()]
    return [ask_loan(), ask_monthly_payment(), ask_loan_interest()]


def count_number_of_payments(annuity_payment: float, rate: float, loan_principal: int) -> int:
    return math.ceil(math.log((annuity_payment / (annuity_payment - rate * loan_principal)), 1 + rate))


def count_loan_principal(annuity_payment: float, rate: float, months: int) -> float:
    return annuity_payment / ((rate * ((1 + rate) ** months)) / ((1 + rate) ** months - 1))


def count_ordinary_annuity(loan_principal: int, rate: float, months: int) -> float:
    return loan_principal * rate * (1 + rate) ** months / ((1 + rate) ** months - 1)


def print_result(char: str) -> str:
    if char == 'a':
        _monthly_payment = math.ceil(count_ordinary_annuity(parameter_to_calculate[0], parameter_to_calculate[2], parameter_to_calculate[1]))
        return f'Your monthly payment = {_monthly_payment}!'
    if char == 'p':
        _loan_principal = round(count_loan_principal(parameter_to_calculate[0], parameter_to_calculate[2], parameter_to_calculate[1]))
        return f'Your loan principal = {_loan_principal}!'
    else:
        number_of_monthly_payments = count_number_of_payments(parameter_to_calculate[1], parameter_to_calculate[2], parameter_to_calculate[0])
        year = math.floor(number_of_monthly_payments / 12)
        month = number_of_monthly_payments % 12
        if number_of_monthly_payments == 1:
            return 'It will take 1 month to repay this loan!'
        if 1 < number_of_monthly_payments < 12:
            return f'It will take {number_of_monthly_payments} months to repay this loan!'
        if number_of_monthly_payments == 12:
            return 'It will take 1 year to repay this loan!'
        if number_of_monthly_payments >= 13:
            if month == 1:
                return f'It will take {year} years and {month} month to repay this loan!'
            else:
                return f'It will take {year} years and {month} months to repay this loan!'


type_char = define_what_calculate()
parameter_to_calculate = choose_parameter(type_char)
print(print_result(type_char))
