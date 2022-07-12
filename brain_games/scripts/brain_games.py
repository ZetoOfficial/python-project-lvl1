# -*- coding: utf-8 -*-

"""Main module."""

import prompt


def welcome_user():
    """Welcome user function."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def main():
    """Master function."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
