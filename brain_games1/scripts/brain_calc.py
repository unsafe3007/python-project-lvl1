#!/usr/bin/env python3
from brain_games1.cli import start_game
from brain_games1.games import calc


def main():
    start_game(calc)


if __name__ == '__main__':
    main()
