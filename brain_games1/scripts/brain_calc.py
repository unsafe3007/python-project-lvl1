#!/usr/bin/env python3
from brain_games1.cli import start_game
from brain_games1.games.calc import get_answer


def main():
    start_game(get_answer)


if __name__ == '__main__':
    main()
