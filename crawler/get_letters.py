#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# This file contains code for fetching letters list from a domain

import urllib2
import constants


# fetches list of letters

def fetch_letters_list():
  yield "lol1"
  yield "lol2"


def main():
  for s in fetch_letters_list():
    print s

if __name__ == "__main__":
  main()
