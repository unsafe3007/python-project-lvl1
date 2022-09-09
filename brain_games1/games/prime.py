from random import randint


def get_prime(num):
    divisor_count = 0

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            divisor_count += 1

    if divisor_count <= 0:
        return 'yes'
    else:
        return 'no'


def get_answer(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    count = 0

    while count < 3:

        num = randint(2, 100)
        correct_answer = get_prime(num)

        print('Question:', num)
        answer = input('Your answer: ')

        if answer == correct_answer:
            print('Correct!')

            count += 1
        else:
            print(f'{answer} is wrong answer ;(. '
                  f"Correct answer was '{correct_answer}'."
                  f" Let's try again, {name}!")

            break

    if count == 3:
        print(f'Congratulations, {name}!')
