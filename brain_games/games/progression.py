from random import randint, choice

CONDITION = 'What number is missing in the progression?'


def generate_progression():
    numbers = []
    first_num = randint(1, 10)
    step = randint(2, 10)
    lenght = randint(6, 10)
    last_num = first_num + step * lenght

    for i in range(first_num, last_num, step):
        numbers.append(i)

    correct_answer = choice(numbers)

    num_x = numbers.index(correct_answer)

    numbers[num_x] = ".."
    progression = " ".join(map(str, numbers))

    return correct_answer, progression


def get_answer():
    correct_answer, progression = generate_progression()
    question = f'Question: {progression}'

    return question, str(correct_answer)
