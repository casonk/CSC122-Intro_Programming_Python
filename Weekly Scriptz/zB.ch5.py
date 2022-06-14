# 5.17.1
'''
g = float(9.8)

def fallingDistance(t):
    d = float(g*t*t/2.0)
    return d

def fallingSpeed(t):
    s = float(g*t)
    return s


if __name__ == '__main__':
    print('Falling Distance Calculator\n')
    st = float(input('Enter the start time: '))
    t = st
    et = float(input('Enter the end time: '))
    ti = float(input('Enter the time interval: '))
    print('\n   Seconds   Speed   Distance')
    print('   -------   -----   --------')
    while st<=t<=et or st>=t>et:
        d = fallingDistance(t)
        s = fallingSpeed(t)
        print('    {:<6}    {:<6}  {:>7}'.format(int(t),int(s),int(d)))
        t += ti
'''
###########################################################

# 5.19.1
'''
def coinCalc(cents):
    q = 0
    d = 0
    n = 0
    p = 0

    while cents >= 25:
        cents -= 25
        q += 1

    while cents >= 10:
        cents -= 10
        d += 1

    while cents >= 5:
        cents -= 5
        n += 1

    while cents >= 1:
        cents -= 1
        p += 1

    ret = ''
    if q > 0:
        ret += '{} Quarter(s),  '.format(q)
    if d > 0:
        ret += '{} Dime(s),  '.format(d)
    if n > 0:
        ret += '{} Nickel(s),  '.format(n)
    if p > 0:
        ret += '{} Penny(Pennies)\n'.format(p)

    return ret

if __name__ == '__main__':
    again = 'Y'

    while again == 'Y':
        print()
        change = int(input('Enter an amount of change to return: '))
        print('\n' + coinCalc(change))
        again = input('Want to try another amount? (y/n):')
        print()
'''