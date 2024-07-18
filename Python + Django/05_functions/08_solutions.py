def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")



print_kwargs(name = "Dhruv", power = "Lazer")
print_kwargs(name = "Aditya")
print_kwargs(name = "Soumyajit", power = "Radiation", enemy = "Dr. Jackaal")
