from Practice_makes_you_perfect.Questions import Question
# a = "jagdish", "mehra"
# b = a
# #print(b)
#print('yesterday\ntoday\ntommorow')
# string = 'abcdapple'
# #print(string[:-1])
# print(string[::-1])
# import csv
# with open('some.csv', 'wb') as f:
#     writer = csv.writer(f)
# f = []
# for i in range(2000,3200):
#     if i%7==0 and i%5!=0:
#         #print(i)
#         f.append(str(i))
#
#
# print(','.join(f))

#factorial
# inp = input()
#
# def fact(num):
#     if num==0:
#         return 1
#     return num*fact(num-1)
#
# #print(type(inp))
# print(fact(inp))

#dictionary
# inp = input()
# squares = {x:x*x for x in range(1,inp+1)}
# print(squares)


#tuple
# values=input()
# l = list(values)
# print(values)
# print(l)

#class

# class Myclass(object):
#     a = 100
#     b = 99
#
# p = Myclass()
# print(p)
# class InputOutString(object):
#     def __init__(self):
#         self.s = ""
#
#     def getString(self):
#         self.s = input()
#
#     def printString(self):
#         print(self.s.upper())
#
#
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()

#math

# import math
# c = 50
# h = 30
# values = []
# items = [x for x in input().split(',')]
# for i in items:
#     values.append(str(int(round(math.sqrt(2*c*float(i)/h)))))
#
# print(','.join(values))

#Dimensions

# input_str = input()
# dimensions=[int(x) for x in input_str.split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
#
# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col]= row*col
#
# print(multilist)

#sort

# items=[x for x in input().split(',')]
# items.sort()
# print(''.join(items))

#multiline

# lines = []
# while True:
#     s = input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break
#
# for sent in lines:
#     print(sent)

#duplication

# lines = [x for x in input().split(' ')]
# #lines.sort()
# print(' '.join(sorted(list(set(lines)))))

#each digit

# values  = []
# for i in range(1000,3001):
#     if i%2==0:
#         values.append(str(i))
#
# print(','.join(values))

#system solution
# values = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print(",".join(values))

# #nmcli
# import nmcli

# def main():
#     print("hello world!")
#
#
# print("Guru99")
#
# if __name__ == "__main__":
#     main()

# var1 = "Guru99!"
# var2 = "Software Testing"
# # print ("var1[0]:",var1[0])
# # print ("var2[1:5]:",var2[1:5])
# print(var1*2)
# print(var2)
# print(''.join(reversed(var1)))
# print(var2.split(' '))

#tuple
# tup = ()
# typ1 = (a)
# print(tup+typ1)
# x = ("Guru99", 20, "Education")    # tuple packing
# (company, emp, profile) = x    # tuple unpacking
# print(company)
# print(emp)
# print(profile)

# Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
# print("Students Name: %s" % list(Dict.items()))
#
#
# Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
# print("printable string:%s" % str (Dict))

# x = 4
# y = 5
# print(('x > y  is',x>y))

# def SwitchExample(argument):
#     switcher = {
#         0: " This is Case Zero ",
#         1: " This is Case One ",
#         2: " This is Case Two ",
#     }
#     return switcher.get(argument, "nothing")



#
# if __name__ == "__main__":
#     argument = 1
#     print (SwitchExample(argument))

#classes

# class myClass():
#     def method1(self):
#         print("Guru99")
#
#     def method2(self, someString):
#         print("Software Testing:" + someString)
#
#
# def main():
#     # exercise the class methods
#     c = myClass()
#     c.method1()
#     c.method2(" Testing is fun")
#
#
# if __name__ == "__main__":
#     main()

# def F(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return F(n-1)+F(n-2)
#
# for i in range(5):
#     print(F(i))

# def simpleGeneratorFun():
#     i = 5
#     while True:
#         yield i
#         i+=1
#
# for b in simpleGeneratorFun():
#     print(b)
#     if b>=10:
#         break

# a = input()
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# n4 = int( "%s%s%s%s" % (a,a,a,a) )
# print(n1+n2+n3+n4)

quest = [ "what is a? \n(a)\n(b)\n(c) ",
          "what is b? \n(a)\n(b)\n(c)",
          "what is c? \n(a)\n(b)\n(c)"]

q = [Question(quest[0], "a"),
     Question(quest[1], "b"),
     Question(quest[2], "c")]


def run_test(qu):
    score = 0
    for qz in qu:
        res = input(qz.prompt)
        if res == qz.answer:
            score+=1

    print(str(score) + "/3")


run_test(q)