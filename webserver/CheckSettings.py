#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time

def check():
	file = requests.get('')
	local = open('./web-config.json', 'w+')
	local.write(file.text)
	local.close()
	
	time.sleep(5)
	check()

if __name__ == '__main__':
	check()