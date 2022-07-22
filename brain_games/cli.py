# -*- coding: utf-8 -*-

"""CLI functions."""

import prompt


def get_user_name():
    """Prompt user for his/her name."""
    return prompt.string('May I have your name? ')
