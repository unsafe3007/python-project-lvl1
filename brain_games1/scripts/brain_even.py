from random import randint
from brain_games1.cli import welcome_user


def is_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no"')

    count = 0
    while count < 3:
        num = randint(1, 100)
        print('Question: ', num)
        answer = input('Your answer: ')

        if answer == 'yes' and num % 2 == 0:
            print('Correct!')
            count += 1

        elif answer == 'yes' and num % 2 != 0:
            print("'yes' is wrong answer ;(. "
                  "Correct answer was 'no'. Let's try again, " + name + "!")
            break
        elif answer == 'no' and num % 2 != 0:
            print('Correct!')
            count += 1

        elif answer == 'no' and num % 2 == 0:
            print("'no' is wrong answer ;(. "
                  "Correct answer was 'yes'. Let's try again, " + name + "!")
            break

        # elif answer != 'yes' or answer !='no':
        else:
            print('Error')
            break

    if count == 3:
        print(f'Congratulations, {name}!!!')


def main():

    print('Welcome to the Brain Games!!!')

    name = welcome_user()
    is_even(name)


if __name__ == '__main__':
    main()
