from random import randint
import operator


def math_function(num_1, num_2, name, math_op):
    if math_op == '+':
        function = operator.add
    elif math_op == '-':
        function = operator.sub
    elif math_op == '*':
        function = operator.mul

    print('Question:', num_1, math_op, num_2)

    answer = int(input('Your answer: '))

    if answer == function(num_1, num_2):
        print('Correct!')

        return True

    else:
        print(f'{answer} is wrong answer ;(. '
              f"Correct answer was {function(num_1, num_2)}. "
              f"Let's try again, {name}!")

        return False


def get_answer(name):
    print('What is the result of the expression?')

    num_1 = randint(1, 100)
    num_2 = randint(1, 100)

    count = 0

    while count < 3:
        if math_function(num_1, num_2, name, '+'):
            count += 1
        else:
            break

        if math_function(num_1, num_2, name, '-'):
            count += 1
        else:
            break

        if math_function(num_1, num_2, name, '*'):
            count += 1
        else:
            break

    if count == 3:
        print('Congratulations, ' + name + '!')
