#!/usr/bin/env python
# -*- coding: utf-8 -*-

# General imports
import re
import time
import json
import requests
from bs4 import BeautifulSoup

# App imports
from app.scraper.models import Ec2Ami, Ec2AmiCollection
from app.scraper.scraper import Scraper

# Logging
import logging
logger = logging.getLogger(__name__)

class CloudImagesScraper(Scraper):
  CLOUD_IMAGES_URL = "http://cloud-images.ubuntu.com/locator/ec2/releasesTable?_=%d"  % int(time.time()*1000)
  CLOUD_IMAGES_VERSION_RE = re.compile("(\d{2}.\d{2})\s?(LTS)?\w*")

  def __init__(self):
    # Inherits from the generirc scraper class
    Scraper.__init__(self, CloudImagesScraper.CLOUD_IMAGES_URL)

  def clean_json(self, string):
    string = re.sub("\\\\\"", "", string)
    string = re.sub(",[ \t\r\n]+}", "}", string)
    string = re.sub(",[ \t\r\n]+\]", "]", string)
    return string

  def scrape(self):
    """ 
      Scrape method that will find out how to extract AMI information 
      from the http://cloud-images.ubuntu.com/locator/ec2/releasesTable webpage.
      
      Returns an Ec2AmiCollection object which contains all
      amis scraped from the page.
    """
    ami_collection = Ec2AmiCollection()
    
    # Define usefull patterns
    # Virtualization Type + Root device extraction
    vt_re = re.compile('(hvm)?:?([a-z0-9\-]+)')
    version_re = re.compile('(\d{1,}.\d{2})\s?([A-Z]+)?')
    
    # Fix the json and load it as dict
    cloud_amis = json.loads(self.clean_json(str(self.soup)))
    for ami in cloud_amis["aaData"]:
      # Extract the virtualization type
      if vt_re.match(ami[4]).group(1) is not None:
        virtualization_type = 'HVM'
      else:
        virtualization_type = 'PV'
      
      # Extract the root device type
      if vt_re.match(ami[4]).group(2) is not None:
        root_device_type = vt_re.match(ami[4]).group(2)
      else:
        root_device_type = None
    
      # Extract the version number
      if version_re.match(ami[2]).group(1) is not None:
        version = version_re.match(ami[2]).group(1)
      else:
        version = None
      
      # Extract the version type
      if version_re.match(ami[2]).group(2) is not None:
        info_version = version_re.match(ami[2]).group(2)
      else:
        info_version = None
      
      ami_obj = Ec2Ami(
        distribution="Ubuntu",
        region=ami[0],
        codename=ami[1].capitalize(),
        version=version, 
        architecture=ami[3], 
        virtualization_type=virtualization_type, 
        release_date=ami[5],
        id=BeautifulSoup(ami[6]).a.string,
        is_lts=True if info_version == 'LTS' else False,
        is_devel=True if info_version == 'DEVEL' else False,
        is_eol=True if info_version == 'EOL' else False,
        root_device_type=root_device_type,
        aki_id=ami[7]
      )
      
      ami_collection.append(ami_obj)

    return ami_collection