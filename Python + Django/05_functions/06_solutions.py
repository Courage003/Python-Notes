#lambda functions are those having no name
def cube(n):
    return n ** 3

cube = lambda x: x ** 3
#this definitions can't be referenced to another variable
print(cube(3))

#lambda frequently used in frameworks

