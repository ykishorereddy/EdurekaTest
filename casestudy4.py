import re
import base64


def Validate(passwd):
    """
    case study -3, accepts user and password as input. validates the password against defined rules.
    Also , encrypt and decrypt the password.
    :param passwd:
    :return:
    """

    SpecialSym = ['$', '@', '#']
    return_val = True
    if len(passwd) < 6:
        print('the length of password should be at least 6 char long')
        return_val = False
    if len(passwd) > 12:
        print('the length of password should be not be greater than 12')
        return_val = False
    if not any(char.isdigit() for char in passwd):
        print('the password should have at least one numeric')
        return_val = False
    if not any(char.isupper() for char in passwd):
        print('the password should have at least one uppercase letter')
        return_val = False
    if not any(char.islower() for char in passwd):
        print('the password should have at least one lowercase letter')
        return_val = False
    if not any(char in SpecialSym for char in passwd):
        print('the password should have at least one of the symbols $,@,#')
        return_val = False
    if return_val:
        print('validation passed')
    return return_val

def EncryptPass(passwd):
    return base64.b64encode(passwd)
def Decryptass(passwd):
    return base64.b64decode(passwd)


if __name__ == "__main__":
    User = raw_input('Enter User Name:')
    print('User name is:',User)
    check  = True
    while check:
        Password = raw_input('Enter password:')
        result = Validate(Password)
        if result is True:
            print('password is fine, password Encryption is in progress')
            encryptpass = EncryptPass(Password)
            print('Password Successfully Encrypted %s',encryptpass)

            check = False
        else:
            print('Password didnt meet standards, pls re-enter')
    ans = raw_input('Do you want to decrypt the password:')
    if ans == 'y' or 'Y':
        decpass = Decryptass(encryptpass)
        print(decpass)


