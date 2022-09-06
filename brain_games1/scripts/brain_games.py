#!/usr/bin/env python3
from brain_games1.cli import welcome_user
from brain_games1.scripts.brain_even import is_even


def main():

    print('Welcome to the Brain Games!!!')

    name = welcome_user()
    is_even(name)


if __name__ == '__main__':
    main()
