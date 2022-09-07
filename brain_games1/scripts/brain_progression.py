#!/usr/bin/env python3
from brain_games1.cli import welcome_user
from brain_games1.games.progression import get_progression


def main():

    print('Welcome to the Brain Games!!!')

    name = welcome_user()
    get_progression(name)


if __name__ == '__main__':
    main()
