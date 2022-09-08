from random import randint


def get_prime(num):
    divisor_count = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            divisor_count += 1
    if (divisor_count <= 0):
        return True
    else:
        return False


def get_answer(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    count = 0
    while count < 3:

        num = randint(2, 100)
        is_prime = get_prime(num)

        print('Question:', num)
        answer = input('Your answer: ')
        if answer == 'yes' and is_prime is True:

            print('Correct!')
            count += 1
        elif answer == 'yes' and is_prime is False:
            print(f'{answer} is wrong answer ;(. '
                  f"Correct answer was 'no'. Let's try again, {name}!")
            break

        if answer == 'no' and is_prime is False:
            print('Correct!')
            count += 1
        elif answer == 'no' and is_prime is True:
            print(f'{answer} is wrong answer ;(. '
                  f"Correct answer was 'yes'. Let's try again, {name}!")
            break

    if count == 3:
        print(f'Congratulations, {name}!')
