#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
import json

def getConfig():
	with open('./config.json', 'r') as f:
		return json.load(f)


def check():
	config = getConfig()
	if config['REMOTE_API'] != "":
		file = requests.get(config['REMOTE_API'])
		local = open('./web-config.json', 'w+')
		local.write(file.text)
		local.close()
		
		time.sleep(5)
		check()

if __name__ == '__main__':
	check()