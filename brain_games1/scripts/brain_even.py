#!/usr/bin/env python3
from brain_games1.cli import welcome_user
from brain_games1.games.even import is_even


def main():
    welcome_user(is_even)


if __name__ == '__main__':
    main()
