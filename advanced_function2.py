# p26
# l = ['a','b','c','d']
# a = list(map(lambda x:int(x)*2,l))
# print(a)

# p27
# l = [10,20,70,80]
# a = list(map(lambda x:int(x)*1.2,l))
# print(a)

# p28
# a = [10,20,70,'80']
# l = list(map(lambda x:int(x)-7,a))
# print(l)

# p29
# n = [34, 68, 102, '136']
# l = list(map(lambda x: int(x)/34,n))
# print(l)

# p30
# a = [10,20,70,'80']
# l = list(map(lambda x:int(x)**3,a))
# print(l)

# p31
# l = ["apple banana cherry","dog cat mouse",]
#
# a = list(map(lambda x:x.split()[0],l))
# print(a)


# p32
# l = [5,10]
# a = [2,4]
# n = list(map(lambda x,y:x+y,l,a))
# print(n)


# p33
# a = [10,27,90,'80']
# l = list(map(lambda x: int(x)*2 if int(x)%2==0  else  int(x)*3,a))
# print(l)

# p34
# a = [-10,27,-90,'80']
# l = list(map(lambda x:abs(int(x)),a))
# print(l)

# p35
# l =  ['aram','hello']
# a = list(map(lambda x:x[::-1],l))
# print(a)

# p36
# a = ['hello','125','ASA15']
# l = list(map(lambda x: x.isdigit(),a))
# print(l)

# p37
# a = [10,27,'aram',15.5]
# l = list(map(lambda x:isinstance(x,int),a))
# print(l)

# p38
# l = ['Leo Messi','Luka Modrich']
# a = list(map(lambda x: f"{x.split()[0][0]}. {x.split()[1]}" ,l))
# print(a)


# p39
# l = ['Leo Messi','Luka Modrich']
# a = list(map(lambda x:f'hargeli {x}' ,l))
# print(a)




# p41
# l = [40,30,80,90]
# a = list(map(lambda x:f'{x} - anbavarar' if 0<=x<=40 else f'{x} - bavarar' if 41<=x<=60 else  f'{x} - lav' if 61<=x<=80 else  f'{x} - gerazanc',l ))
#
# print(*a,sep = ',')



# p42
# from functools import reduce
# n = [1,2,3,5]
#
# l = reduce(lambda x,y:x*y,n)
# print(l)


# p43
# from functools import reduce
# n = ['Ararat','Vedi','Kapan']
# l = reduce(lambda x,y:f'{x} {y}',n)
# print(l)

# p44
# from functools import reduce
# n = [1,-2,3,-5]
# l =  reduce(lambda x,y:abs(x) + abs(y),n)
# print(l)

# p45
# from functools import reduce
# n = [1,-2,3,-5]
# l =  reduce(lambda  x,y:x if x<y else y,n)
# print(l)

# p46
# from functools import reduce
# n = ['Ararat','Vedi','Kapan']
# l = reduce(lambda x, y: x if len(x) > len(y) else y, n)
# print(l)


# p48
# from functools import reduce
# l = [1,2,3,4]
# k = reduce(lambda x,y:x + 3 * y,l,0)
# print(k)

# 49
# from functools import reduce
# l = [11,18,5,19]
# k = reduce(lambda x,y:x%5 + y % 5 ,l)
# print(k)

# p50
# from functools import reduce
# l = [1,2,3,4]
# k = reduce(lambda x,y:x + y **2,l,0)
# print(k)

# p51
# from functools import reduce
# n = ['Ararat','Vedi','Kapan']
# l = reduce(lambda x,y:x+len(y),n,0)
# print(l)


# # p52
#
# from functools import reduce
#
# l = [1, 5, 7, 12, -2]
#
# a = reduce(lambda x, y: x + y if (l.index(y) % 2 != 0) else x - y , l)
# print(a)


