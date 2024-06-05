bank_account = {'bank account' : '15700$'}
login = input('Login: ')

def account():
    print(bank_account['bank account'])

def check_login(func):
    def wrapper():
        if login == 'admin':
            func()
        else:
            print('Доступ запрещён')
    return wrapper

account = check_login(account)
account()
