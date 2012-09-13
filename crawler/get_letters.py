#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# This file contains code for fetching letters list from a domain

import urllib2
import constants
import re

# fetches list of letters

def get_letters():
  data = urllib2.urlopen("http://"+constants.DOMAIN_NAME).read()
  letter_regexp = re.compile('<a class="purple" href=[^>]*')
  res = []
  for str in letter_regexp.findall(data):
    res.append("http://"+constants.DOMAIN_NAME+"/"+str[24:-1])
  return res

def main():
  for s in get_letters():
    print s

if __name__ == "__main__":
  main()
