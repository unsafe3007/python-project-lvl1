import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}!')

    return name


def start_game(game):
    print('Welcome to the Brain Games!!!')

    name = welcome_user()

    print(game.CONDITION)

    count = 0

    while count < 3:
        question, correct_answer = game.get_answer()

        print(question)

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
