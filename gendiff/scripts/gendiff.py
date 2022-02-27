#!/usr/bin/env python

import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='see format of output')
    args = parser.parse_args()
    print(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
