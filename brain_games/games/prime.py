from random import randint

CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_prime(num):
    divisor_count = 0

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            divisor_count += 1

    if divisor_count <= 0:
        return 'yes'
    else:
        return 'no'


def get_answer():
    num = randint(2, 100)
    question = f'Question: {num}'
    correct_answer = get_prime(num)

    return question, correct_answer
