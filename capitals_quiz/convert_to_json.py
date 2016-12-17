#!/bin/env python
import json

country_list = {}

json_file = 'country_capitals.json'
json_capitals = open(json_file,'w')

with open('capitals.txt','r') as f:
	#print(f.readlines())

	for line in f:
		country, capital = line.rstrip('\n').split(':')
		country_list[country] = capital
		

json.dump(country_list, json_capitals,sort_keys=True, indent=4)
json_capitals.close()
print("Converted text file to json %s" %(json_file))
