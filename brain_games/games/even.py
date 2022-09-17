from random import randint

CONDITION = 'Answer "yes" if the number is even, otherwise answer "no"'


def get_correct_answer(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def get_answer():
    num = randint(1, 100)
    question = f'Question: {num}'
    correct_answer = get_correct_answer(num)

    return question, correct_answer
