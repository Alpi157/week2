#1
a = [2, 4, 3, 1, 5]
print(a[::-1])



#2
def change(a):
    a[0], a[len(a) - 1] = a[len(a) - 1], a[0]
a = [1, 2, 3]
change(a)
print(a)



#3
def to_list(*a):
    return list(a)
print(to_list(2, 4, 3, 1, 5))



#4
def uselessNumber(llst):
    return max(llst)/len(llst)
print(uselessNumber(a))



#5
def list_sort(a):
    return sorted(map(abs, a), reverse = True)
temp = [1, -2, 3, -4, 5]
print(list_sort(temp))



#6
a = ["short", "shr", "soooooooooooo"]
print([i.rjust(len(max(a, key = len)), '_') for i in a])
