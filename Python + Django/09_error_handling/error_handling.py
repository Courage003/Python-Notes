file = open('youtube.txt', 'w')

try:
    file.write('Dhruv is good')
finally:
    file.close()


#both same syntax second one mostly preferred
with open('youtube.txt', 'w') as file:
    file.write('Dhruv')
