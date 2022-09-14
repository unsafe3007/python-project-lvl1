#!/usr/bin/env python3
from brain_games1.cli import start_game
from brain_games1.games.progression import get_progression


def main():
    start_game(get_progression)


if __name__ == '__main__':
    main()
