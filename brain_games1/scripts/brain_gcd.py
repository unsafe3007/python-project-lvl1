#!/usr/bin/env python3
from brain_games1.cli import welcome_user
from brain_games1.games.gcd import get_answer


def main():
    welcome_user(get_answer)


if __name__ == '__main__':
    main()
