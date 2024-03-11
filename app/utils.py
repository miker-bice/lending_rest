BASE_INTEREST_RATE = 24
ONE_YEAR = 12


def calculate_interest_rate() -> float:
    '''
    returns a float

    formula:
    r = (BASE_INTEREST_RATE / 12) / 100
    '''
    interest_rate_per_year = BASE_INTEREST_RATE/ONE_YEAR
    interest_rate_per_period = interest_rate_per_year/100

    return interest_rate_per_period


def calculate_number_of_payments(loan_term:int) -> float:
    '''
    returns a float

    formula:
    n = (loan_term/12) * 12
    '''
    year = loan_term/ONE_YEAR
    number_of_payments = year * ONE_YEAR

    return number_of_payments


def calculate_payment_amount(loan_amount, interest_rate, number_of_payments) -> float:
    '''
    returns a float

    formula:
    A = loan_amount * (upper_result / lower_result)
    '''

    upper_result = interest_rate * (1 + interest_rate)**number_of_payments
    lower_result = (1 + interest_rate)**number_of_payments - 1
    monthly_payment_amount = loan_amount * (upper_result / lower_result)

    return round(monthly_payment_amount, 2)


def calculate_total_interest(principal_loan_amount, interest_rate, loan_term) -> float:
    '''
    returns a float

    formula:
    total_interest = principal_loan_amount * interest_rate * loan_term
    '''
    total_interest = principal_loan_amount * interest_rate * loan_term
    
    return total_interest


def calculate_total_sum_payments(principal_loan_amount, total_interest_amount) -> float:
    '''
    returns a float

    formula:
    total_sum_payments = principal_loan_amount + total_interest_amount
    '''

    total_sum_payments = principal_loan_amount + total_interest_amount

    return total_sum_payments