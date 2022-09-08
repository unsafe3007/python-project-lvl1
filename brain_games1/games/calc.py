from random import randint


def get_answer(name):
    print('What is the result of the expression?')

    num_1 = randint(1, 100)
    num_2 = randint(1, 100)

    count = 0

    while count < 3:
        print('Question:', num_1, '+', num_2)
        answer = int(input('Your answer: '))
        if answer == num_1 + num_2:
            print('Correct!')
            count += 1
        else:
            print(f'{answer} is wrong answer ;(. '
                  f"Correct answer was {num_1 + num_2}. "
                  f"Let's try again, {name}!")
            break

        print('Question:', num_1, '-', num_2)
        answer = int(input('Your answer: '))
        if answer == num_1 - num_2:
            print('Correct!')
            count += 1
        else:
            print(f'{answer} is wrong answer ;(. '
                  f"Correct answer was {num_1 - num_2}. "
                  f"Let's try again, {name}!")
            break

        print('Question:', num_1, '*', num_2)
        answer = int(input('Your answer: '))
        if answer == num_1 * num_2:
            print('Correct!')
            count += 1
        else:
            print(f'{answer} is wrong answer ;(. '
                  f"Correct answer was {num_1 * num_2}. "
                  f"Let's try again, {name}!")
            break

    if count == 3:
        print('Congratulations, ' + name + '!')
