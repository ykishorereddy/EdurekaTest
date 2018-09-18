import math

def robotMovement(u,d,l,r):
    startHeight = 0
    startWidth = 0
    robopos = (startHeight,startWidth)
    print('start position:',robopos)
    if u > 0:
        startHeight += u
    if  d > 0:
        startHeight -= d
    if l > 0 :
        startWidth += l
    if r > 0:
        startWidth -= r

    robopos = (startHeight,startWidth)
    print('Position after movement:',robopos)

if __name__ == "__main__":
    up = 5
    down = 3
    left = 3
    right = 2

    robotMovement(up,down,left,right)