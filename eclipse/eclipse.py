#!/usr/bin/env python3

from collections import namedtuple

import click

Line = namedtuple('Line', ['x1', 'x2'])


def is_overlapping(line1, line2):
    """Given two lines and return True if they overlap or False if not"""
    return max(line1) >= min(line2) and max(line2) >= min(line1)


def input_to_line(value):
    """Convert the user line input into an instance of Line"""
    try:
        return Line(*map(float, value.split(',')))
    except (TypeError, ValueError):
        raise click.BadParameter(
            'Invalid format, it should be something like this: 1,2'
        )


@click.command(help='Given two lines at the x-axis check if they overlap')
def cli():
    line1 = click.prompt(
        'Please enter the first line x1 and x2 separate by comma',
        value_proc=input_to_line,
    )
    line2 = click.prompt(
        'Please enter the first line x1 and x2 separate by comma',
        value_proc=input_to_line,
    )

    if is_overlapping(line1, line2):
        click.echo(click.style(
            f'The lines {line1} and {line2} do overlap',
            fg='green',
        ))
    else:
        click.echo(click.style(
            f'The lines {line1} and {line2} do not overlap',
            fg='red',
        ))


if __name__ == '__main__':
    cli()
