__author__ = 'dealen'

i = 1

while i <= 100:

    if i % 5 == 0 and i % 3 == 0:
        print('output: ', 'FizzBuzz')
    elif i % 5 == 0:
        print('output: ', 'Buzz')
    elif i % 3 == 0:
        print('output: ', 'Fizz')
    else:
        print('output: ', str(i))
    i += 1

value = input('Press any key...')
