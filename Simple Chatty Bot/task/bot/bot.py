def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("What is pizza?")
    print("1. Apples.")
    print("2. Juice.")
    print("3. Donuts.")
    print("4. Bread with sauce and cheese.")

    i = int(input())
    while i != 4:
        print("Please, try again.")
        i = int(input())

    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Base', '2022')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
