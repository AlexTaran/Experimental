#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# This file contains code for fetching preps from preps-lists

import urllib2
import constants
import re
from get_letters import get_letters

# fetches list of preps

def get_preps():
  res = []
  for url in get_letters():
    data = urllib2.urlopen(url).read()
    prep_regexp = re.compile('<a class="red" href=[^>]*><')
    # prep_regexp.findall(data)
    res += ["http://"+constants.DOMAIN_NAME+"/"+s[21:-3] for s in prep_regexp.findall(data) ]
  return res

def main():
  lst = get_preps()
  for s in lst:
    print s
  print "All preps: " + str(len(lst))

if __name__ == "__main__":
  main()
