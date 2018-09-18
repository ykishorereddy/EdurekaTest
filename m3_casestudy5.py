

def cashwithdraw():
    print('cash withdrawal in progress')

def cashcredit():
    print('cash credit in progress')

def changepassword():
    print('password change in progress')


if __name__ == "__main__":

    print('******************************')
    print('1.Cash Withdrawl')
    print('2.Cash Credit')
    print('3.Change Password')
    print('******************************')
    print('Choose option to proceed...')
    option = int(raw_input('Choose Option: '))

    if option == 1:
        cashwithdraw()
    elif option == 2:
        cashcredit()
    else:
        changepassword()
