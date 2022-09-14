#!/usr/bin/env python3
from brain_games1.cli import start_game
from brain_games1.games.even import is_even


def main():
    start_game(is_even)


if __name__ == '__main__':
    main()
