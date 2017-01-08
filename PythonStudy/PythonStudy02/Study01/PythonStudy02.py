#
var1 = 10
var1

#
a=5
a

#
var2 = "hello World"
var2


a=3
b=4
a+b  # add
a*b  # 
a/b  # 
a%b  # 
a//b # 
a**b # 
a+=3 
a
a*=3 
a
a/=3 
a
a-=3 
a
a//3




# String print
print("python mm;")

str2="hi there?"
print(str2)


# input String
inValue1 = input()
inValue2 = input("input02")


print("%s" %inValue1)

print("inValue1: %s inValue2: %s" %(inValue1, inValue2))

# input String int
inputValue3 = int(input("inputValue3"))
inputValue4 = int(input("inputValue4"))

print("inputValue3: %s * inputValue4: %s = %d" %(inputValue3, inputValue4, inputValue3*inputValue4))


# input String float
inputValue5 = float(input("inputValue5"))
inputValue6 = float(input("inputValue6"))

print("inputValue5: %s * inputValue6: %s = %.2f" %(inputValue5, inputValue6, inputValue5*inputValue6))

# String Parsing

str1 ="abcdefg hijk lmn"
print(str1)

print(str1[0])      #a
print(str1[1])      #b
print(str1[2])      #c
print(str1[3])      #d
print(str1[4])      #e

print(str1[:])      #abcdefg hijk lmn

print(str1[0:3+1])  #abcd
print(str1[1:3+1])  #bcd
print(str1[2:3+1])  #cd
print(str1[3:3+1])  #d
print(str1[4:3+1])  #

print(str1[0:])     #abcdefg hijk lmn
print(str1[1:])     #bcdefg hijk lmn
print(str1[2:])     #cdefg hijk lmn
print(str1[3:])     #defg hijk lmn

print(str1[0:0])    #
print(str1[0:-1])   #abcdefg hijk lm
print(str1[0:-2])   #abcdefg hijk l
print(str1[0:-3])   #abcdefg hijk
print(str1[0:-4])   #abcdefg hijk

print(str1[1:-4])   #bcdefg hijk
print(str1[2:-4])   #cdefg hijk

# String \n Test
print("abce \n efgh");  # abce 
                        # efgh

print("abce \\n efgh"); # abce \n efgh

# upper, lower
str6="Apple";
str6.upper();
str6.lower();

#count
str7="Apple";
str7.count("p");  #2
str7.count("P");  #0
str7.count("p",0);#2
str7.count("p",1);#2
str7.count("p",2);#1
str7.count("p",3);#0

#index
str8="Apple";
str8.index("p");  #1
str8.index("P");  #error
str8.index("p",0);#1
str8.index("p",1);#1
str8.index("p",2);#2
str8.index("p",3);#error


#strip(trim)
str8=" Apple ";
str8.lstrip();  #'Apple '
str8.rstrip();  #' Apple'
str8.strip();   #'Apple'

#replace
str8=" Apple ";
str8.replace("pp","tt");   #' Attle '
str8=" Apple ";
str8.replace("p","t",-1);  #' Attle '
str8=" Apple ";
str8.replace("p","t",0);   #' Apple '
str8=" Apple ";
str8.replace("p","t",1);   #' Atple '
str8=" Apple ";
str8.replace("p","t",2);   #' Attle '
str8=" Apple ";
str8.replace("p","t",3);   #' Attle '


#split
str8="A,p,p,l,e";
str8.split(",");    #['A', 'p', 'p', 'l', 'e']
str8.split(",",0);  #['A,p,p,l,e']
str8.split(",",1);  #['A', 'p,p,l,e']
str8.split(",",2);  #['A', 'p', 'p,l,e']
str8.split(",",3);  #['A', 'p', 'p', 'l,e']
str8.split(",",4);  #['A', 'p', 'p', 'l', 'e']


#len
len("hithere")  # 7

#String loop
print("**" *20);
print("1\n" *3);


#String 
A='''h1
h2
h3'''
print(A)