#!/usr/bin/env python

from gendiff import cli
from gendiff import engine


def main():
    args = cli.get_args()
    engine.run(args)


if __name__ == '__main__':
    main()
