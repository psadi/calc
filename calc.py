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
    operator = r"^(\+|\-|\*|\/|\(|\)|\.|\%)$"
    status = True
    for char in expression:
        if not (char.isnumeric() or re.match(operator, char)):
            status = False
            raise ValueError("Not a valid number/operator")
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
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', type=str, help="Pass an arithmetic expression")
    args = parser.parse_args()
    console_mode = False

    try:

        if not subprocess_run('which zenity')[0] == 0:
            raise ValueError("Zenity not found")

        if args.e is not None:
            expression = args.e
            console_mode = True
        else:
            expression = subprocess_run("zenity  --entry --text 'Expression?'")[1].strip()

        if not validate(expression):
            subprocess_run("zenity --info --text 'Invalid Expression!'")
            raise ValueError("Invalid Expression!")

        result = f"expression: {expression} = {eval(expression)}"
        if not console_mode: subprocess_run(f"zenity --info --text '{result}'")
        else: print(result)

    except (subprocess.CalledProcessError, SyntaxError, ValueError) as ex:
        print(ex)
        sys.exit(1)

if __name__ == "__main__":
    main()
