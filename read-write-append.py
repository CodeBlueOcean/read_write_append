# my_file = open('test.txt')

# print(my_file.readlines())

# my_file.close()

# example hey it' me!
with open('test.txt', mode='r+') as my_file:
    text = my_file.write('hey it\' me!')
    print(my_file.readlines())

# example :) it' me 
with open('test.txt', mode='r+') as my_file:
    text = my_file.write(':)')
    print(my_file.readlines())

# example :)
with open('sad.txt', mode='w') as my_file:
    text = my_file.write(':)')
    print(text)

# example :) it' me 
with open('test.txt', mode='r+') as my_file:
    text = my_file.write(':)')
    print(my_file.readlines())

# example hey it' me!:)
with open('test.txt', mode='a') as my_file:
    text = my_file.write(':)')
    print(text)


