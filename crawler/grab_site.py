#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import get_preps
import urllib2

def prep_name_from_url(url):
  slash = url.rfind("/")
  dot = url.rfind(".")
  if slash < 0 or dot < 0 or dot <= slash:
    raise ValueError("Wrong prep url: '" + url + "' for prep_name_from_url")
  return url[slash + 1 : dot]

def ensure_dir(path):
  if not os.path.exists(path):
    os.makedirs(path)

def main():
  ensure_dir(ROOT_DIR_NAME)
  print "Trying to download list of preps..."
  preps = get_preps.get_preps()
  for prep in preps:
    print "Downloading prep: " + prep_name_from_url(prep)
    prep_folder = prep_name_from_url(prep)
    ensure_dir(ROOT_DIR_NAME + "/" + prep_folder)
    page_data = urllib2.urlopen(prep).read()
    with open(ROOT_DIR_NAME + "/" + prep_folder + "/" + prep_folder + ".html", "w") as f:
      f.write(page_data)
  print "Processed " + str(len(preps)) + "preps"

if __name__ == "__main__":
  main()
