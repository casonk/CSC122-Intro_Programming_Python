# 6.18.1
'''
magik = [ [0,0,0], [0,0,0], [0,0,0] ]
used = []
countinpts = 0

def getinpt(i, ii):
    status = True
    inpt = 0
    global countinpts
    countinpts += 1

    try:
        inpt = int(input('Enter a value (1-9) for row {} column {}: '.format(i, ii)))

        if inpt not in range(1,10):
            status = False
            print('Error! Out of range! Try again.')

        elif inpt in used:
            print('Error! Duplicate value entered! Try again.')
            status = False

    except:
        status = False
        print('\nError! Invalid data entered! Try again!')
    
    if countinpts > 100:
        exit()

    return inpt, status 

def display():
    for row in magik:

        for num in row:
            print(num, end='')

        print()

def build():
    for i in range(3):

        for ii in range(3):
            inpt, status = getinpt(i, ii)

            while status == False:
                inpt, status = getinpt(i, ii)

            magik[i][ii] = inpt
            used.append(inpt)
            print()
    print()
    display()

def checkMatrix(magik):
    status = True
    magiksum = 15
    tmp0 = 0
    tmp1 = 0
    tmp2 = 0
    tmpd0 = 0
    tmpd1 = 0

    for row in magik:
        if magiksum != sum(row):
            status = False
        tmp0 += row[0]
        tmp1 += row[1]
        tmp2 += row[2]

    if tmp0 != magiksum:
        status = False

    if tmp1 != magiksum:
        status = False

    if tmp2 != magiksum:
        status = False

    tmpd0 = magik[0][0] + magik[1][1] + magik[2][2]
    tmpd1 = magik[0][2] + magik[1][1] + magik[2][0]

    if tmpd0 != magiksum:
        status = False
    if tmpd1 != magiksum:
        status = False

    if __name__ == '__main__':
        if status:
            print('The square is magic!')
        else:
            print('The square is not magic!')
    else:
        if status:
            print('Your function did not find a square that is magic')
        else:
            print('Your function failed to find a square that is not magic')

if __name__ == '__main__':
    print()
    build()
    print()
    checkMatrix(magik)
'''
