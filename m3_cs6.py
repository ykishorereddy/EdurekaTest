
def calculate(s,e):
    res = []
    for i in range(s,e):
        if (i % 7 == 0) and  (i % 5 != 0):
            res.append(i)
    print res

def factorial(num):

    if num == 1:
        return num
    else:
        return num*factorial(num-1)


if __name__ == "__main__":
    start = int(raw_input('Enter Starting Range:'))
    end = int(raw_input('Enter Ending Range:'))
    calculate(start,end)
    #casestudy #7
    num = 1
    while num > 0:
        num = int(raw_input('Enter the number:'))
        print('Factorial for a number %d is:' %num,factorial(num))