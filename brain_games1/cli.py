import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}!')

    return name


def start_game(function):
    print('Welcome to the Brain Games!!!')

    name = welcome_user()

    function(name)
