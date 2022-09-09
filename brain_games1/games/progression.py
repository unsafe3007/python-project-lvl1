from random import randint, choice


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


def get_progression(name):
    print('What number is missing in the progression?')
    total = 0
    while total < 3:
        correct_answer, progression = generate_progression()

        print("Question:", progression)
        answer = int(input('Your answer: '))
        if answer == correct_answer:
            total += 1
        else:
            print(f'{answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}. '
                  f'Let\'s try again, {name}!')
            break
    if total == 3:
        print(f'Congratulations, {name}!')
