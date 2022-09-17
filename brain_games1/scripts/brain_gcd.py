#!/usr/bin/env python3
from brain_games1.cli import start_game
from brain_games1.games import gcd


def main():
    start_game(gcd)


if __name__ == '__main__':
    main()
