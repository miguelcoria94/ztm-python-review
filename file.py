with open('test.txt', mode='r+') as my_file:
    text = my_file.write('Hey it\' me!')
    print(text)