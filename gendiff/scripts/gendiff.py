#!/usr/bin/env python3

import argparse
from gendiff.generate_diff import generate_diff

text = 'Compares two configuration files and shows a difference.'


def main():
    parser = argparse.ArgumentParser(description=text)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    # print(args.first_file, args.second_file)

    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
