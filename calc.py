#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# pylint: disable=W0123
# calc:33:49: W0123: Use of eval (eval-used)

"""
    calc: a simple py3 script to perform arithmetic operations
"""

__version__ = '0.1.2'
__author__ = 'P S, Adithya (adithya3494@gmail.com)'
__license__ = 'MIT'


import re
import sys
import argparse
import subprocess


def validate(expression: str) -> bool:
    """Validate if the given expression is a valid mathematical expression"""
    operator = "^(\+|\-|\*|\/|\(|\)|\.|\%)$"
    status = True
    for char in expression:
        if char.isnumeric() or re.match(operator, char):
            pass
        else:
            status = False
    return status

def subprocess_run(command):
    """run a given command and return its exit code and stdout"""
    run = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        check=True
    )

    return [run.returncode, run.stdout.decode()]

def main():
    """calc: main func"""
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-e', type=str, help="Input a mathematical expression")
        args = parser.parse_args()

        if subprocess_run('which zenity')[0] == 0:
            if args.e is not None:
                expression = args.e
            else:
                expression = subprocess_run("zenity  --entry --text 'Expression?'")[1].strip()

            if validate(expression):
                evaluate = f"expression: {expression} = {eval(expression)}"
                subprocess_run(f"zenity --info --text '{evaluate}'")
            else:
                subprocess_run("zenity --info --text 'Invalid Expresson'")
        else:
            sys.exit(1)

    except subprocess.CalledProcessError:
        sys.exit(1)

if __name__ == "__main__":
    main()
