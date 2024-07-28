a = int(input())
b = int(input())
if a < b:
    print(b)
elif b < a:
    print(a)


a = int(input())
b = int(input())
if (a - b) >= 135 or (b-a)>=135:
    print('yes')
else:
    print('no')


god = int(input())
if 1 <= god <= 2 or god == 12:
    print('zima')
elif 3 <= god <= 5:
    print('vesna')
elif 6 <= god <= 8:
    print('leto')
elif 9 <= god <= 11:
    print('oseni')
else:
    print('ne to chislo')


a = int(input())
b = int(input())
c = int(input())
if a >= 10 and b>= 10 and c >=10:
    print('yes')
else:
    print('no')


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a >= 10 and b>= 10 and c >=10:
    print('yes')
else:
    print('no')

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
p=[a,b,c,d,e]
digit_counter = 0
for i in p:
    if i >= 0:
        digit_counter+=1
if digit_counter == 0:
    print("числа не обнаружены")
else:
    print(digit_counter)



d = 29 #days
l = int(input()) #let
m = int(input()) #month 1-12
L1 = l * (12 * 29) #348
M1 = d * m
D = L1 + M1
print(D)


