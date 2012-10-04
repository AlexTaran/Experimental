#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# This file contains code for extracting preps' data from downloaded htmls 

import urllib2
import constants
import re
import os
import pickle
from constants import *
from bs4 import BeautifulSoup

class Prep:
  def __init__(self):
    self.nick_name = "[Nickname N/A]";
    self.first_name = "[Firstname N/A]";
    self.middle_name = "[Middlename N/A]";
    self.last_name = "[Lastname N/A]";
    self.work_places = list()
    self.photo_urls = set()
    self.courses = list()

class ErrCounter:
  counter = 0

class GeneralInfo:
  err_counter = 0
  chairs = dict()
  photo_counter = 0
  preps_with_photo_counter = 0

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
  # extracting work_places
  re_workplaces = re.compile('<li><a class="black" href="/chairs/([^<>]*).html">([^<>]*)</a></li>')
  workplaces = re_workplaces.findall(data)
  for workplace in workplaces:
    if GeneralInfo.chairs.has_key(workplace[0]) and GeneralInfo.chairs[workplace[0]] != workplace[1]:
      print "Error: chair " + workplace[0] + " has different display names!"
      print "Old was '" + GeneralInfo.chairs[workplace[0]] + "' but new is '" + workplace[1]
      return False
    GeneralInfo.chairs[workplace[0]] = workplace[1]
    prep.work_places.append(workplace[0])
    #print "Works at " + workplace[0] + " aka " + workplace[1]
  # extracting links to photos
  re_photo_urls = re.compile('<a class="prepphoto" href="([^"]*)"')
  photo_urls = re_photo_urls.findall(data)
  if len(photo_urls) != 0:
    GeneralInfo.preps_with_photo_counter += 1
    for photo_url in photo_urls:
      prep.photo_urls.add(photo_url) 
    GeneralInfo.photo_counter += len(prep.photo_urls)
    #print photo_urls
  # extracting courses
  re_courses = re.compile(u': </font>'+
    u'<div style="margin-left: 15px; margin-top: 5px; margin-bottom: 5px;"><a class="black" href="#">'+
    u'([^<>]*)</a></div></font>')
  courses = re_courses.findall(data.decode('utf-8'))
  if len(courses) > 0:
    prep.courses += map(lambda s: s.strip(), courses[0].split(',')) # TODO: split by ';'
    if len(courses) > 1:
      print "Error: found more than one list of courses"
      return False
  for course in prep.courses:
    print course
  soup = BeautifulSoup(data);
  print soup.prettify()
  # dump extracted data
  with open(ROOT_DIR_NAME + "/" + prep_name + "/" + prep_name + ".pickledump", "w") as f:
    pickle.dump(prep, f)
  return True

def main():
  print "Start processing data"
  preps_list = os.listdir(ROOT_DIR_NAME)
  for prep_name in preps_list:
    if os.path.isdir(ROOT_DIR_NAME + "/" + prep_name):
      process_prep(prep_name)
      break
  print "Errors count: " + str(ErrCounter.counter)
  print "Processed preps: " + str(len(preps_list))
  print "Found chairs: "
  for chair in GeneralInfo.chairs.keys():
    print "  " + chair + " aka " + GeneralInfo.chairs[chair]
  print "Preps with photos: " + str(GeneralInfo.preps_with_photo_counter)
  print "All photos: " + str(GeneralInfo.photo_counter)

if __name__ == "__main__":
  main()
