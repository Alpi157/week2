#1
s = str(input('Введите строку на русском: '))
t = s.split()
count = 0
for words in t:
    if words[0] == 'е' or words[0] == 'Е':
        count += 1
print(count)



#2
s = str(input('Enter a string: '))
count = 0
while s.find(':') != -1:
    s = s.replace(':', '%', 1)
    count += 1
print(s)
print(count)



#3
s = str(input('Enter a string: '))
count = 0
while s.find('.') != -1:
    s = s.replace('.', '', 1)
    count += 1
print(s)
print(count)



#4
s= str(input('Enter a string: '))
count = 0
while s.find('a') != -1:
    s = s.replace('a', 'o', 1)
    count += 1
print(s)
print(count)
print(len(s))



#5
s = str(input('Enter a string: '))
for letters in s:
    if ord(letters) > 64 and ord(letters) < 91:
        s = s.replace(letters, chr(ord(letters)+32))
print(s)




#6
s = str(input('Enter a string: '))
count = 0
while s.find('a') != -1:
    s = s.replace('a', '', 1)
    count += 1
print(s)
print(count)



#8
s = str(input('Enter a string: '))
t = s.split()
count = 0
while True:
    if t[count][len(t[count]) - 1] == '.':
        break
    else:
        count += 1
print(count)



#9
s1 = str(input('Enter the text: '))
s2 = str(input('Enter the word: '))
print(s1.count(s2))



#10
s1 = str(input('Enter the text: '))
s2 = s1.split()
t = list()
for i in s2:
    t = list(i)
    t[0] = t[0].upper()
    print("".join(t))



#11
s1 = str(input("Enter the text: "))
s2 = s1.split()
m = max(s2)
m = m.replace("!", ".")
m = m.replace("?", ".")
print(m)



#12
s1 = str(input('Enter the text: '))
s2 = s1.split()
t = list()
for i in s2:
    t = list(i)
    if t[len(t) - 1] == 'I':
        print(i)



#13
s1 = str(input('Enter the text: '))
i = []
count = 0
for char in s1:
    count += 1
    if char == '"':
                i.append(count)
s1 = s1[i[0]:i[1] - 1]
print(s1)



#14
s1 = str(input('Enter the text: '))
s2 = s1.split()
for i in s2:
    if i[len(i) - 1] == 'i':
        if i[0] == 'a':
            print(i)



#15
s = str(input('Enter a string: '))
count = 0
while s.find('t') != -1:
    s = s.replace('t', '', 1)
    count += 1
print(count)
                    



















