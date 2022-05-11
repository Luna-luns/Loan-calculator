import math
import argparse


def count_number_of_payments(annuity_payment: float, rate: float, loan_principal: int) -> int:
    return math.ceil(math.log((annuity_payment / (annuity_payment - rate * loan_principal)), 1 + rate))


def count_loan_principal(annuity_payment: float, rate: float, months: int) -> float:
    return annuity_payment / ((rate * ((1 + rate) ** months)) / ((1 + rate) ** months - 1))


def count_ordinary_annuity(loan_principal: int, rate: float, months: int) -> float:
    return loan_principal * rate * (1 + rate) ** months / ((1 + rate) ** months - 1)


def count_differentiate_payment(loan_principal: int, rate: float, month: int) -> str:
    interest_amount = 0
    result = ''
    for current_month in range(1, month + 1):
        payment = math.ceil(loan_principal / month + rate * (loan_principal - (loan_principal * (current_month - 1)) / month))
        interest_amount += payment
        result += f'Month {current_month}: payment is {payment}\n'

    overpayment = int(interest_amount - loan_principal)
    result = f'{result}\nOverpayment = {overpayment}'

    return result


def print_result(args) -> str:
    payment = float(args.payment) if args.payment is not None else None
    interest = float(args.interest) / 100 / 12 if args.interest is not None else None
    periods = int(args.periods) if args.periods is not None else None
    principal = int(args.principal) if args.principal is not None else None
    if args.type == 'annuity' and payment is None:
        _monthly_payment = math.ceil(count_ordinary_annuity(principal, interest, periods))
        overpayment = int((_monthly_payment * periods) - principal)
        return f'Your annuity payment = {_monthly_payment}!\nOverpayment = {overpayment}'
    if args.type == 'annuity' and principal is None:
        _loan_principal = round(count_loan_principal(payment, interest, periods))
        overpayment = int(payment * periods - _loan_principal)
        return f'Your loan principal = {_loan_principal}!\nOverpayment = {overpayment}'
    if args.type == 'annuity' and periods is None:
        number_of_monthly_payments = count_number_of_payments(payment, interest, principal)
        year = math.floor(number_of_monthly_payments / 12)
        month = number_of_monthly_payments % 12
        if number_of_monthly_payments == 1:
            overpayment = int(number_of_monthly_payments * payment - principal)
            return f'It will take 1 month to repay this loan!\nOverpayment = {overpayment}'
        if 1 < number_of_monthly_payments < 12:
            overpayment = int(number_of_monthly_payments * payment - principal)
            return f'It will take {number_of_monthly_payments} months to repay this loan!\nOverpayment = {overpayment}'
        if number_of_monthly_payments == 12:
            overpayment = int(number_of_monthly_payments * payment - principal)
            return f'It will take 1 year to repay this loan!\nOverpayment = {overpayment}'
        if number_of_monthly_payments >= 13:
            if month == 1:
                overpayment = int(number_of_monthly_payments * payment - principal)
                return f'It will take {year} years and {month} month to repay this loan!\nOverpayment = {overpayment}'
            else:
                overpayment = int(number_of_monthly_payments * payment - principal)
                return f'It will take {year} years and {month} months to repay this loan!\nOverpayment = {overpayment}'
    if args.type == 'diff' and payment is None:
        return count_differentiate_payment(principal, interest, periods)


def check_errors(args) -> bool:
    if args.type != 'annuity' and args.type != 'diff':
        return False
    if args.type == 'diff' and args.payment is not None:
        return False
    if args.interest is None:
        return False
    if args.type == 'diff':
        if not (args.principal is not None and args.periods is not None and args.interest is not None):
            return False
    if args.type == 'annuity':
        if not ((args.principal is not None and args.periods is not None and args.interest is not None) or
                (args.principal is not None and args.payment is not None and args.interest is not None) or
                (args.payment is not None and args.periods is not None and args.interest is not None)):
            return False
    return not (args.principal is not None and int(args.principal) < 0 or
                args.periods is not None and int(args.periods) < 0 or
                args.interest is not None and float(args.interest) < 0 or
                args.payment is not None and int(args.payment) < 0)


parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')
parser.add_argument('--payment')
args = parser.parse_args()
is_valid_args = check_errors(args)
if not is_valid_args:
    print('Incorrect parameters')
    exit()
print(print_result(args))
