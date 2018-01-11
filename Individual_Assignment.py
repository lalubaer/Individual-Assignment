#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:42:58 2018

@author: Momo
"""
# Import the JSON and CSV packages
import json
import csv

# Load in the conflict JSON data
with open('conflict_data/conflict_data_full.json') as file:
    data = json.load(file)

# Open the output CSV file we want to write to
with open('preprocessed_data.csv', 'w') as file:
    csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(['Country', 'Lat', 'Lng', 'Active'])#forgot year
    for item in data:
        csvwriter.writerow([item['country'], item['latitude'], item['longitude'], item['active_year']])
        
#Here's the corrected version that has the year in it     
with open('useful_data.csv', 'w') as file:
    csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(['country', 'year', 'latitude', 'longitude', 'active'])
    for item in data:
        csvwriter.writerow([item['country'], item['year'], item['latitude'], item['longitude'], item['active_year']])
    