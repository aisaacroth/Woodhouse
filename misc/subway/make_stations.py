#!/usr/bin/env python3.4
import argparse
import csv
import json

def main(args):
    print(args.stop_file)
    print(args.transfer_file)


def setup_args():
    parser = argparse.ArgumentParser(description='Creates a JSON file containing the name, route, long, and lattitude of the subway station.')
    parser.add_argument('stop_file')
    parser.add_argument('transfer_file')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = setup_args()
    main(args)
