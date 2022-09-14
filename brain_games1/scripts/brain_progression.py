#!/usr/bin/env python3
from brain_games1.cli import welcome_user
from brain_games1.games.progression import get_progression


def main():
    welcome_user(get_progression)


if __name__ == '__main__':
    main()
