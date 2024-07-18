username = "Dhruv"

def test():
    #username = "aditya"
    print(username)

print(username)
test()


#x = 99

##def test2(y):
  #  z = x + y
 #   return z

#result = test2(1)
#print(result)##

#x accessed global declaration
#y from parameters

x = 98
def test3():
    global x 
    x = 12
    

test3()
print(x)   

#don't adopt this practice , leads to overwriting of existing codespace

def f1():
    x = 88
    def f2():
        print(x)

    return f2
myRes = f1()
myRes()    

#closure not only takes the function but also inclusive of function defintions associated with it


def chaicoder(num):
    def actual(x):
        return x ** num
    return actual



f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))

#concept of closure