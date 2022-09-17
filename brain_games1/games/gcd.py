from random import randint

CONDITION = 'Find the greatest common divisor of given numbers.'


def get_gcd(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 = num_1 % num_2
        else:
            num_2 = num_2 % num_1

    gcd = num_1 + num_2

    return gcd


def get_answer():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    question = f'Question: {num_1}, {num_2}'
    correct_answer = get_gcd(num_1, num_2)

    return question, str(correct_answer)
