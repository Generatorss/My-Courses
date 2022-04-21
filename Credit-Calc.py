import math
import argparse


def user_arguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description='''\
                                     Credit calculator
                                     -----------------
                                     ''')
    parser.add_argument('-t', '--type', type=str, choices=['annuity', 'diff'],
                        help='Type of payment annuity or differentiated')
    parser.add_argument('-pay', '--payment', type=int,
                        help='Annuity payment')
    parser.add_argument('-pr', '--principal', type=int,
                        help='Amount of credit')
    parser.add_argument('-p', '--periods', type=int,
                        help='Payment period')
    parser.add_argument('-i', '--interest', type=float,
                        help='Interest rate, enter only in numbers')
    args = parser.parse_args()
    return args


def user_data(args):
    t = args.type
    a = args.payment
    p = args.principal
    n = args.periods
    i = args.interest
    user_verify(t, a, p, n, i)


def user_verify(t, a, p, n, i):
    if t != 'diff' and t != 'annuity':
        print('Incorrect parameters 1')
    elif not (a is None) and t == 'diff':
        print('Incorrect parameters 2')
    elif i is None:
        print('Incorrect parameters 3')
    elif (type(a) == int and a < 0) or (type(p) == int and p < 0) or (type(n) == int and n < 0) or (i < 0):
        print('Incorrect parameters 4')
    elif (t == 'annuity' or t == 'diff') and (
            (not a and not p) or (not a and not n) or
            (not a and not i) or (not p and not n) or
            (not p and not i) or (not n and not i)
    ):
        print('Incorrect parameters 5')
    else:
        i = i / (12 * 100)
        run_function(t, a, p, n, i)


def run_function(t, a, p, n, i):
    if t == 'diff' and not a:
        diff(p, n, i)
    elif t == 'annuity' and not a:
        annuity(p, n, i)
    elif t == 'annuity' and not p:
        principal(a, n, i)
    elif t == 'annuity' and not n:
        periods(p, a, i)


def periods(p, a, i):
    n = math.log((a / (a - (i * p))), (1 + i))
    print_periods(math.ceil(n))
    print('Overpayment = ' + str(a * math.ceil(n) - p))


def print_periods(n):
    if n == 1:
        print('It will take ' + n + ' month to repay this loan!')
    elif 12 >= n >= 2:
        print('It will take ' + n + ' months to repay this loan!')
    elif n > 12:
        num_years = math.floor(n / 12)
        num_mounts = n - (math.floor(n / 12) * 12)
        if num_years == 1 and num_mounts == 0:
            print('It will take ' + str(num_years) + ' year to repay this loan!')
        elif num_years == 1 and num_mounts == 1:
            print('It will take ' + str(num_years) + ' year and ' + str(num_mounts) + ' month to repay this loan!')
        elif num_years == 1 and num_mounts > 1:
            print('It will take ' + str(num_years) + ' year and ' + str(num_mounts) + ' months to repay this loan!')
        elif num_years > 1 and num_mounts == 0:
            print('It will take ' + str(num_years) + ' years to repay this loan!')
        elif num_years > 1 and num_mounts == 1:
            print('It will take ' + str(num_years) + ' years and ' + str(num_mounts) + ' month to repay this loan!')
        elif num_years > 1 and num_mounts > 1:
            print('It will take ' + str(num_years) + ' years and ' + str(num_mounts) + ' months to repay this loan!')
        else:
            print(
                'It will take ' + str(num_years) + ' year(s) and ' + str(num_mounts) + ' month(s) to repay this loan!')


def annuity(p, n, i):
    a = p * ((i * (math.pow((1 + i), n))) / ((math.pow((1 + i), n)) - 1))
    print("Your monthly payment = " + str(math.ceil(a)) + '!')
    print('Overpayment = ' + str(math.ceil(a) * n - p))


def diff(p, n, i):
    m = 1
    s = 0
    while m < (n + 1):
        d = (p / n) + (i * (p - ((p * (m - 1)) / n)))
        print('Month ' + str(m) + ': payment is ' + str(math.ceil(d)))
        m = m + 1
        s = s + math.ceil(d)
    print()
    print('Overpayment = ' + str(s - p))


def principal(a, n, i):
    p = a / ((i * (math.pow((1 + i), n))) / ((math.pow((1 + i), n)) - 1))
    print('Your loan principal = ' + str(math.floor(p)) + '!')
    print('Overpayment = ' + str(int((a * n)) - int((math.floor(p)))))


user_data(user_arguments())
