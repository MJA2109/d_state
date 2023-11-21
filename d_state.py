#!/usr/bin/python3

import os
import sys
import json
import argparse


bundle = sys.argv[1]

try:
    api_call_arg = sys.argv[2]
except IndexError:
	api_call_arg = ""

os.chdir(bundle)
path = os.getcwd()
DS='desired_state_manager.json'
PATH_FILE = path + "/" + DS

with open(PATH_FILE, "r", encoding='UTF-8') as t_file:

	api_calls = json.load(t_file)


if not api_call_arg:
    for api_call in api_calls:
        print(api_call)
else:
	for api_call in api_calls:
		if api_call == api_call_arg:
			print("API: GET " + api_call)
			print("-------------------------------------------------")
			print(json.dumps(api_calls[api_call], indent = 4))
	    











