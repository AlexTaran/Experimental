#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import get_preps
import urllib2

ROOT_DIR_NAME = "PREPS"

def prep_name_from_url(url):
  slash = url.rfind("/")
  dot = url.rfind(".")
  if slash < 0 or dot < 0 or dot <= slash:
    raise ValueError("Wrong prep url: '" + url + "' for prep_name_from_url")
  return url[slash + 1 : dot]

def ensure_dir(path):
  folder = os.path.dirname(path)
  if not os.path.exists(path):
    os.makedirs(path)

def main():
  ensure_dir(ROOT_DIR_NAME)
  preps = get_preps.get_preps()
  for prep in preps:
    print prep_name_from_url(prep)
    ensure_dir(ROOT_DIR_NAME + "/" + prep_name_from_url(prep))
  print len(preps)

if __name__ == "__main__":
  main()
