#!/usr/bin/env python3.4
from google.transit import gtfs_realtime_pb2
import nyct_subway_pb2
import urllib
import datetime

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen('http://datamine.mta.info/mta_esi.php?key=396a051a03e2448c103793b1005b5516&feed_id=1')
feed.ParseFromString(response.read())

for entity in feed.entity:
    print entity
