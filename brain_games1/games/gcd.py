from random import randint


def get_gcd(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 = num_1 % num_2
        else:
            num_2 = num_2 % num_1

    gcd = num_1 + num_2

    return gcd


def get_answer(name):
    print('Find the greatest common divisor of given numbers.')

    count = 0

    while count < 3:
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)

        gcd = get_gcd(num_1, num_2)

        print('Question:', num_1, num_2)

        answer = int(input('Your answer: '))

        if answer == gcd:
            print('Correct!')

            count += 1
        else:
            print(f'{answer} is wrong answer ;(. '
                  f"Correct answer was {gcd}. Let's try again, {name}!")
            break

    if count == 3:
        print(f'Congratulations, {name}!')
