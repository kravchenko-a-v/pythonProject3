# #Пешка
# x1 = int(input())
# y1 = int(input())
#
# x2 = int(input())
# y2 = int(input())
#
# if y2 == y1 + 1 and x2 == x1 + 1:
#     print('Бьёт')
# elif y2 == y1 + 1 and x2 == x1 - 1:
#     print('Бьёт')
# else:
#     print('Не бьёт')
#
# # Треугольник
#
# a = int(input())
# b = int(input())
# c = int(input())
# if a<b+c and b<a+c and c<a+b:
#     print('YES')
# else:
#     print('NO')
#
# # Числа
#
# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print(3)
# elif a==b!=c or a==c!=b or b==c!=a:
#     print(2)
# else:
#     print(0)
#
# # # Коробки
# #
# # A1 = int(input())
# # B1 = int(input())
# # C1 = int(input())
# # A2 = int(input())
# # B2 = int(input())
# # C2 = int(input())
# #
# # if A1+B1+C1 > A2+B2+C2:
# #     print('Коробку 2 можно разместить в коробку 1')
# # elif A1+B1+C1 > A2+B2+C2:
# #     print('Коробку 1 можно разместить в коробку 2')
# # else:
# #     print('Коробки 1 и 2 равны')
# #
# # if (A1>A2 and B1>B2) or (A1>A2 and C1>C2) or (B1>B2 and C1>C2):
# #     print('Коробку 2 можно разместить в коробку 1')
# # elif (A1<A2 and B1<B2) or (A1<A2 and C1<C2) or (B1<B2 and C1<C2):
# #     print('Коробку 1 можно разместить в коробку 2')
# # else:
# #     print('Коробки 1 и 2 равны')
#
# a = int(input())
# b = int(input())
# c = int(input())
# if a>b:
#     a,b = b,a
# if b>c:
#     b,c = c,b
# if a>b:
#     a,b = b,a
# print(a,b,c)

# a = 1
# while a<=10:
#     print(a)
#     a = a+1

# a = int(input())
# n = int(input())
#
# temp = a
# count = 1
# while count < n:
#     a = a*temp
#     count = count+1
# print(a)

# a = int(input())
#
# count = 2
# while count<a:
#     print(count)
#     count = count+2

# a = int(input())
#
# count = a-1
# while count >=1:
#     if a%count == 0:
#         print(count)
#         break
#     count = count - 1

# a = 16**2
# print(a)

# a = int(input())
#
# count = 2
# while count < a:
#     print(count)
#     count = count + 2

# # Кароль
# x1 = int(input())
# y1 = int(input())
#
# x2 = int(input())
# y2 = int(input())
#
# if x2 == x1 + 1 and y2 == y1 + 1 or y2 == y1 - 1 or y2 == y1:
#     print('Бьёт')
# if x2 == x1 - 1 and y2 == y1 + 1 or y2 == y1 - 1 or y2 == y1:
#     print('Бьёт')
# if x2 == x1  and y2 == y1 + 1 or y2 == y1 - 1:
#     print('Бьёт')
# else:
#     print('Не бьёт')

# # Слон
# x1 = int(input())
# y1 = int(input())
#
# x2 = int(input())
# y2 = int(input())
#
# if abs(x1 - x2) == abs(y1 - y2):
#     print('da')
# else:
#     print('no')

# s = 'python'
# for i in range (len(s)):
#     print(s[i])

# s = input()
# upper = 0
# lower = 0
# for i in range(len(s)):
#     if s[i].islower():
#         lower = lower+1
#     if s[i].isupper():
#         upper = upper + 1
# print(upper)
# print(lower)

# s = input()
# count = 0
# for i in range(len(s)):
#     if s[i]== ' ':
#         count = count + 1
# print(count+1)

# s = input()
# c = input()
# count = 0
# for i in  s:
#     if i == c:
#         count=count+1
# print(count)

# s = input()
#
# digit = 0
# alpha = 0
#
# for i in s:
#     if i.isdigit():
#         digit += 1
#     if i.isalpha():
#         alpha += 1
# print(digit)
# print(alpha)

# li = []
# size = int(input())
# for i in range (size):
#     li.append(input())
# print(li)
#
# max = li[0]
# for i in li:
#     if len(i) > len(max):
#         max = i
# print(max)

# li = [1,2,3,4,5]
# print(li[::-1])

# li = [1, 'sasd', 45, 5]
# a = 0
# for i in li:
#     if isinstance(i, int) :
#         a = a+1
# print(a)

# li = [55, 6, 7, 88]
# min = li[0]
# for i in li:
#     if i < min:
#         min = i
# print(min)

# li = []
# size = int(input())
# for i in range (size):
#     li.append(int(input()))
# print(li)
# a = int(input())
# print(li.count(a))

# li = []
# size = int(input())
# for i in range(size):
#     li.append(int(input()))
# a = int(input())
# count = 0
# for i in li:
#     if i == a:
#         count = count + 1
# if count == 0:
#     print('НЕТ')
# else:
#     print('ЕСТЬ')

# li = [1, 23, 2, 5, 4, 6]
# count = 0
# for i in li:
#     if i % 2 == 0:
#         count = count + 1
# print(count)
#
# li = ['hgjhg', 'fuuu', 'hj', 'uu']
# a = input()
# count = 0
# for i in li:
#     if i[0] == a:
#         count += 1
# print(count)

# li = []
# size = int(input())
# for i in range(size):
#     li.append(input())
# min = li[0]
# for i in li:
#     if len(i)<len(min):
#         min = i
# print(min)


