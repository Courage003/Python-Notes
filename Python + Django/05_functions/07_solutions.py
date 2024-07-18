def sum_all(*args):
    print(args)  #return tuple format
    for i in args:
        print(i * 2)
    return sum(args)
    


print(sum_all(1, 2))
print(sum_all(1, 2, 3, 4))