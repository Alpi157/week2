from itertools import groupby



#1
array = int (input('The lenght of array: '))
x = []
max_num = 0
for i in range (array):
    print('Enter ',i,'number: ')
    x.append(int(input()))
max_num = max(x)
print ('1. ', x)
print ("The max number in array: ", max_num)
for i in range (array):
    if x[i] == 0:
        x[i] = sum(x)
    else: pass
print('2. ', x)
x.reverse()
print ("Reverse:", x)



#2
array2 = int(input('\n Enter the length of array: '))
x2 = []
min_num = 0
for i in range (array2):
    print('enter ',i,'number: ')
    x2.append(int(input()))
min_number = min(x2)
minpos = x2.index(min(x2))
print('2. the minimum element:', min_number, 'and its position:' ,minpos)

#2.2          
array3 = int (input('\n Enter the lenght of array: '))
first = []
second = []
third = []
for i in range (array3):
    print('enter ',i,'number: ')
    first.append(int(input()))
print ("the first array:" ,first)
for i in range (array3):
    if first[i] >= 0:
        second.append(first[i])
        
    else:
        third.append(first[i])

print ('array with only negative numbers' ,third)
print ('array with others', second)



#3
D = [1, 2, 3, 4, 5, 6, 7, 8]
print ("\task The original array:" ,D)
print ("the original:",D)
for i in range (len(D)):
    if (D[i]) <15 :
        (D[i])*=(D[i])
print ("the converted", D)



#4
def get_suffix(num):
    if num in [10,11,12,13]:
        return 'th'
    else:
        rem = num & 10
        if rem == 1:
            return 'st'
        elif rem == 2:
            return 'nd'
        elif rem == 3:
            return 'rd'
        else:
            return 'th'
array4 = int (input('\n Please enter the lenght of array from 1-30: '))
x4 = []
max_num4 = 0
for i in range (array4):
    print('Enter ',i,'number: ')
    x4.append(int(input()))
max_num4 = max(x4)
print (x4)
print ("1. the max number in array: ", max_num4)
print (f" {max_num4}{get_suffix(max_num4)}")
oddar = []
for i in range (array4):
    if (x4[i]%2) == 0:
        oddar.append(x4[i])
print ("2. odd numbers: ", oddar)
x4.sort(reverse = True)
print(x4)



#5
print ("\n [1, 2, -4, 5, -1, 6, 7, -8, 9, -10]")
x = [1, 2, -4, 5, -1, 6, 7, -8, 9, -10]
neg = []
for i in range (len(x)):
    if (x[i]) < 0:
        neg.append(x[i])
print ("Negative numbers:" ,neg)
print ("\n 2): [1, 1, 2, 4, 5, 5, 3, 2, 3, 7]")
t = [1, 1, 2, 4, 5, 5, 3, 2, 3, 7]
new_t = [el for el, _ in groupby(t)]

print(new_t)



#6
print ("\n [1, 2, -4, 5, -1, 6, 7, -8, 9, -10]")
n = [1, 2, -4, 5, -1, 6, 7, -8, 9, -10]
max_num = max(n)
y = []
x = []
index = n.index(max_num)
for i in range(len(n)):
    if i > index:
        y.append(n[i])
    elif i < index:
        x.append(n[i])
print("Max number of array: " ,max_num)
print ("Number/s greater than the max element: " ,y)
print("Numbers less than the max element: ", x)

print ("\n 2): [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]")
array6 = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]
sum_num = 0
for c in array6:
    if c>5:
        sum_num+=c
print("The sum of numbers bigger than 5: ", sum_num)



#7
print ("\n [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]")
array7 = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]
sum_even = 0
product_odd = 1
for h in array7:
    if h%2==0:
        sum_even+=h
    else:
        product_odd*=h
print("the sum of even numbers in array" ,sum_even, """
and the product of odd numbers in array""" ,product_odd)
max_numb=max(array7)
min_numb=min(array7)
for i in range(len(array7)):
    if array7[i]==max_numb:
        array7[i]=min_numb
    elif array7[i]==min_numb:
        array7[i]=max_numb
print('2) array with swapping: ',array7)



#8
x8 = int (input('Enter the lenght of array: '))
array8 = []
for i in range (x8):
    print('enter ',i,'number: ')
    array8.append(int(input()))
print (array8)
print(sum(array8))
multiply = 1
for i in array8:
    multiply = multiply*i
print ("multiply", multiply)
x8n = int (input('Enter the lenght of array with zero numbers: '))
array8_new = []
for i in range (x8n):
    print('enter ',i,'number: ')
    array8_new.append(int(input()))
print ("2) array with zero numbers", array8_new)
for i in range (len( array8_new)):
    if array8_new[i] == 0:
        array8_new[i] = sum(array8_new)/len(array8_new)
    else: pass
print ("array without zero: ",array8_new)



#9
x9 = int (input('Enter the lenght of array: '))
array9 = []
for i in range (x9):
    print('Enter ',i,'number: ')
    array9.append(int(input()))
print (array9)
print('min modulo number:', min(x, key = abs))

#2
A = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
B = [2, 3, 7, 8, 8, 9, 10, 11, 14]
print('original array A: ', A)
print('original array B: ', B)
A,B=B,A
print('new array A: ',A)
print('new array B: ',B)



#10
mylist = []
num = int(input("\n Enter the number of elements: "))
for i in range(0,num):
    ele = int(input("element: "))
    mylist.append(ele)
newlist = [] 
replist = []
for i in mylist:
    if i not in newlist:
        newlist.append(i)
    else:
        replist.append(i)
print("list of duplicates", replist)
print("unique item", newlist)

A10 = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 21, 22, 23, 24, 25]
print ("\n(2) original array: " ,A10)
for i in range (len(A10)):
    if A10[i] < 10:
        A10[i] = 0
    elif A10[i] > 20:
        A10[i] = 1
print ("converted array: ",A10)



#11
A11 = [1, 2, 3 ,4, 5 ,6 ,7 ,8, 10, 11]
max_num = 0
for i in range (len(A11)):
    if A11[i]%2==0 and max_num < A11[i]: 
        max_num = A11[i]
print('\n The largest even number is: ' ,max_num)
A1 = [1, 2, 3 ,4, 5 ,6 ,7 ,8, 10, 11]
B2 = []
for i in range (len(A1)):
    if  A1[i]%2 == 0 and A1[i]<10:
        B2.append(A1[i])
    else:
        continue
print ("(2) new array: ",B2)



#12
A12 = [1, 2 ,3 ,4 ,5 ,6 ,7,8 ,9 ,10]
small_num = 11
for i in range (len(A12)):
    if A12[i]%2!=0 and small_num>A12[i]:
        small_num = A12[i]
        print('\n The smallest odd number is: ' ,small_num)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
B = [2, 3, 7, 8, 8, 9, 10, 11, 14]
print('original array A: ', A)
print('original array B: ', B)
A,B=B,A
print('New array A: ',A)
print('New array B: ',B)



#13
mylist = []
array = int(input("\n Enter the number of elements: "))
for i in range(0,array):
    x = int(input("Element: "))
    mylist.append(x)
newlist = [] 
dublist = []
for i in mylist:
    if i not in newlist:
        newlist.append(i)
    else:
        dublist.append(i)
print("list of duplicates", dublist)
print("unique item", newlist)
print("Same elements: ", i, "first appearing indices: ", mylist.index(i))

num = 8
x=[]
for i in range(n):
    print('(2) Enter the element ',i)
    x.append(int(input()))
for i in range(len(x)):
    if x[i]<15: x[i]*=2
print('New array: ', x)



#14
n=int(input("\nArray length: "))
x=[]
for i in range(n):
    print('Enter the element ',i)
    x.append(int(input()))
max_numb = max(x)
min_numb = min(x)
for i in range(len(x)):
    if x[i]== max_numb: x[i]= min_numb
    elif x[i]== min_numb: x[i] = max_numb
print('New array: ',x)













