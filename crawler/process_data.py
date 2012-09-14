#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# This file contains code for extractint preps' data from downloaded htmls 

import urllib2
import constants
import re
import os
from constants import *

class Prep:
  def __init__(self):
    self.nick_name = "[Nickname N/A]";
    self.first_name = "[Firstname N/A]";
    self.middle_name = "[Middlename N/A]";
    self.last_name = "[Lastname N/A]";

class ErrCounter:
  counter = 0

def process_prep(prep_name):
  prep = Prep()
  prep.nickname = prep_name
  file_name = ROOT_DIR_NAME + "/" + prep_name + "/" + prep_name + ".html"
  with open(file_name, "r") as f:
    data = f.read()
  # extracting full name
  re_fullname = re.compile(
    '<span class="family-name">([^<>]*)</span>\s*'+
    '<span class="given-name">([^<>]*)</span>\s*'+
    '<span>([^<>]*)</span>')
  lst = re_fullname.findall(data)
  if len(lst) != 1:
    print "Error processing prep: " + prep_name
    ErrCounter.counter += 1
    return False
  prep.first_name  = lst[0][1]
  prep.middle_name = lst[0][2]
  prep.last_name   = lst[0][0]
  print "Prep " + prep_name + " : " + prep.last_name + " " + prep.first_name + " " + prep.middle_name
  # extracting prep_photo
  return True

def main():
  print "Start processing data"
  preps_list = os.listdir(ROOT_DIR_NAME)
  for prep_name in preps_list:
    if os.path.isdir(ROOT_DIR_NAME + "/" + prep_name):
      process_prep(prep_name)
      #break
  print "Errors count: " + str(ErrCounter.counter)
  print "Processed preps: " + str(len(preps_list))

if __name__ == "__main__":
  main()
