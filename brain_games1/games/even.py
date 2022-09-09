from random import randint


def get_correct_answer(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def is_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no"')

    count = 0

    while count < 3:
        num = randint(1, 100)
        correct_answer = get_correct_answer(num)

        print('Question:', num)

        answer = input('Your answer: ')

        if answer == correct_answer:
            print('Correct!')

            count += 1

        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f" Let's try again, " + name + "!")

            break

    if count == 3:
        print(f'Congratulations, {name}!!!')


is_even('ptiupt')
