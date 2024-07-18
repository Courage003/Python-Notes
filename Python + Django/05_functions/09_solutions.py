def even_generator(limit):
    
    for i in range(2, limit + 1, 2):
        yield i
       
#memory reference returning of value
#Read more about yield

for num in even_generator(10):
    print(num)