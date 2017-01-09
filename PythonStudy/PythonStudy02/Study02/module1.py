#List
list1 =[1,"hi there", 10, 10.1]
print(list1)        # [1,"hi there", 10, 10.1]

print(list1[0])     # 1
print(list1[1])     # hi there
print(list1[2])     # 10
print(list1[3])     # 10.1


print(list1[0:0+1]) # [1]
print(list1[0:1+1]) # [1, 'hi there']
print(list1[0:2+1]) # [1, 'hi there', 10]
print(list1[0:3+1]) # [1, 'hi there', 10, 10.1]


#List - append
list1 =[1,"hi there", 10, 10.1]

list1.append("Append01")
print(list1)                # [1, 'hi there', 10, 10.1, 'Append01']


#List - insert
list1 =[1,"hi there", 10, 10.1]

list1.insert(1,"Insert01")
list1.insert(2,"Insert02")
list1.insert(3,"Insert03")
list1.insert(4,"Insert04")
print(list1)                # [1, 'Insert01', 'Insert02', 'Insert03', 'Insert04', 'hi there', 10, 10.1]

#List - del, remove
list1 =[1,"hi there", 10, 10.1]
print(list1)                # [1, 'Insert01', 'Insert02', 'Insert03', 'Insert04', 'hi there', 10, 10.1]
del list1[2]                
print(list1)                # [1, 'Insert01', 'Insert03', 'Insert04', 'hi there', 10, 10.1]
list1.append("AppendXX")
list1.append("AppendXX")
print(list1)                # [1, 'Insert01', 'Insert03', 'Insert04', 'hi there', 10, 10.1, 'AppendXX', 'AppendXX']
list1.remove("AppendXX")
print(list1)                # [1, 'hi there', 10.1, 'AppendXX']


#List - number sort, reverse

num = [1,3,4,2,6,5]
num.sort()
num         # [1, 2, 3, 4, 5, 6]
num.reverse()
num         # [6, 5, 4, 3, 2, 1]



#List - alphabet sort, reverse

alpha = ['a','f','e','d','b']
alpha.sort()
alpha         # ['a', 'b', 'd', 'e', 'f']
alpha.reverse()
alpha         # ['f', 'e', 'd', 'b', 'a']



#List - num&alphabet sort, reverse

num_alpha = ['a1','f2','2e','2d','1b']
num_alpha.sort()
num_alpha         # ['1b', '2d', '2e', 'a1', 'f2']
num_alpha.reverse()
num_alpha         # ['f2', 'a1', '2e', '2d', '1b']



#List - Index

num_alpha = ['a1','f2','2e','2d','1b']
num_alpha.index("a1")   # 0
num_alpha.index("f2")   # 1
num_alpha.index("2e")   # 2
num_alpha.index("2d")   # 3
num_alpha.index("1b")   # 4
num_alpha.index("zz")   # error



#List - Index

num_alpha = ['a1','f2',['2e','2d','1b']]
num_alpha.index("a1")     # 0
num_alpha.index("f2")     # 1
num_alpha.index("2e")     # error
num_alpha.index("2d")     # error
num_alpha.index("1b")     # error
num_alpha.index("zz")     # error
num_alpha[0]              # a1
num_alpha[1]              # f2
num_alpha[2]              # ['2e', '2d', '1b']
num_alpha[2][0]           # 2e
num_alpha[2][1]           # 2d
num_alpha[2][2]           # 1b
num_alpha[2][3]           # error
num_alpha[3]              # error
num_alpha[0:0]            # []
num_alpha[0:0+1]          # ['a1']
num_alpha[0:1+1]          # ['a1', 'f2']
num_alpha[0:2+1]          # ['a1', 'f2', ['2e', '2d', '1b']]
num_alpha[0:3+1]          # ['a1', 'f2', ['2e', '2d', '1b']]


#List - Number

num_alpha1 = ['a1','f2',['2e','2d','1b']]
num_alpha2 = ['a1','f2','2e','2d','1b']

len(num_alpha1) # 3
len(num_alpha2) # 5