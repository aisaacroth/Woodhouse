#!/usr/bin/env python3.4
import argparse
import csv
import json


def setup_args():
    parser = argparse.ArgumentParser(description='Creates a JSON file containing the name, route, long, and lattitude of the subway station.')
    parser.add_argument('-s', '--stop_file', help='the stops.txt file', default='google_transit/stops.txt')
    parser.add_argument('-t', '--transfer_file', help='the transfer.txt file', default='google_transit/transfers.txt')
    args = parser.parse_args()
    return args


def main(args):
    print(args.stop_file)
    print(args.transfer_file)
    stops = read_stop_file(args.stop_file)
    transfers = read_transfer_file(args.transfer_file)
    print(transfers)

    for parent_id in transfers:
        if parent_id > min(transfers[parent_id]):
            continue
        
        print(parent_id)
        print(transfers[parent_id])
        for stop_id in transfers[parent_id]:
            stop = stops.pop(stop_id)
            print(stop)


def read_stop_file(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        stops = {}

        for row in reader:
            if row['parent_station']:
                continue

            gen_stop_info(row, stops)

        return stops


def gen_stop_info(row, stops):
    stops[row['stop_id']] = {
        'name': row['stop_name'],
        'lat': row['stop_lat'],
        'lon': row['stop_lon']
        }


def read_transfer_file(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        transfers = {}

        for row in reader:
            if row['from_stop_id'] == row['to_stop_id']:
                continue

            gen_transfer_info(row, transfers)

        return transfers


def gen_transfer_info(row, trans):
    try:
        trans[row['from_stop_id']].add(row['to_stop_id'])
    except KeyError as e:
        trans[row['from_stop_id']] = set([row['from_stop_id'], row['to_stop_id']])


if __name__ == '__main__':
    args = setup_args()
    main(args)
