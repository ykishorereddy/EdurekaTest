def casestudy1(nums):
    print('case Study#1 results')
    print len(nums)

def casestudy2(dict):
    print('case Study#2 results')
    print(list(d.keys()))

def casestudy4(a):
    print('input list is',a)
    print('case Study#4 results')
    for i in a:
        print('List Element is',i, 'position its position ',a.index(i))

def casestudy5(str):
  s = ''
  for c in str:
      if c.isalpha():
          s = s + c
  print(s)

def casestudy6(inp):
    print('Original string',inp)
    print('Reverse String method#1',inp[::-1])
    print('Reverse String method#2',''.join(reversed(inp)))

def casestudy7(inp):
    print('input string',inp)
    for i in inp:
        print("%s,%d" % (i,inp.count(i)))

def casestudy8(l1,l2):

    a = set(l1) & set(l2)
    print('common in both list',list(a))

if __name__ == "__main__":
    # case study #1
    nums = set([1, 1, 2, 3, 3, 3, 4, 4])
    casestudy1(nums)
    # case study #2
    d = {"john": 40, "peter": 45}
    print(list(d.keys()))

    #casestudy #4
    a  = [4,7,3,2,5,9]
    casestudy4(a)

    str = 'H1e2l3l4o5w6o7r8l9d'
    casestudy5(str)

    #Casestudy #6
    inp = raw_input('Enter the input:')
    casestudy6(inp)

    #casestudy #7
    inp = raw_input('Enter the string:')
    casestudy7(inp)

    #casestufy #8
    l1 = [1,3,6,78,35,55,12]
    l2 = [12,24,35,24,88,120,155]
    casestudy8(l1,l2)