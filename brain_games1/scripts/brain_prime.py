#!/usr/bin/env python3
from brain_games1.cli import welcome_user
from brain_games1.games.prime import get_answer


def main():

    print('Welcome to the Brain Games!!!')

    name = welcome_user()
    get_answer(name)


if __name__ == '__main__':
    main()
