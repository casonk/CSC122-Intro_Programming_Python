# 3.10
'''
int1 = int(input())
int2 = int(input())
int3 = int(input())
if int1 < int2 and int1 < int3:
   print(int1)
elif int2 < int3 and int2 < int1:
   print(int2)
else:
   print(int3)
'''
###########################################################

# 3.11
'''
print('Enter the 1st primary color to mix (red, green, or blue): ', end = '')
input1=str(input())
print('Enter the 2nd primary color to mix (red, green, or blue): ', end = '')
input2=str(input())
input1=input1.lower()
input2=input2.lower()
print()
if (input1==input2) or (input1!='red' and input1!='green' and input1!='blue') or (input2!='red' and input2!='green' and input2!='blue'):
   print('Error! Invalid color(s) entered!')
elif (input1=='red' and input2=='blue') or (input2=='red' and input1=='blue'):
   print('The secondary color mixed is magenta.')
elif (input1=='red' and input2=='green') or (input2=='red' and input1=='green'):
   print('The secondary color mixed is yellow.')
elif (input1=='blue' and input2=='green') or (input2=='blue' and input1=='green'):
   print('The secondary color mixed is cyan.')
'''
###########################################################

# 3.12
'''
print('Freshman (F), Sophomore (O), Junior (J), Senior (S):', end='')
grade=str(input())
grade=grade.upper()
print()
print('Had tickets last year? Yes (Y) or No (N)? ', end='')
roll=str(input())
roll=roll.upper()
print()
print('Please enter your GPA as a value between 0 and 4: ', end='')
gpa=float(input())
print('\n')
points=0
if gpa<=2.0:
    if grade=='S':
        points=135
    else:
        points=90
elif gpa<=3.0 and roll=='N':
    if grade=='F':
        points=95
    elif grade=='O':
        points=115
    else:
        points=130
elif gpa<=3.0 and roll=='Y':
    if grade=='F':
        points=110
    elif grade=='O':
        points=130
    else:
        points=150
elif gpa>3.0 and roll=='N':
    if grade=='F':
        points=120
    elif grade=='S':
        points=175
    else:
        points=160
elif gpa>3.0 and roll=='Y':
    if grade=='F':
        points=135
    elif grade=='S':
        points=195
    else:
        points=170
print('Your available points are', points)
'''