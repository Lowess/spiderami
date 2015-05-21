#!/usr/bin/env python
# -*- coding: utf-8 -*-

# General imports
import re
import requests
from bs4 import BeautifulSoup

# App imports
from app.scraper.models import Ec2Ami, Ec2AmiCollection
from app.scraper.scraper import Scraper

# Logging
import logging
logger = logging.getLogger(__name__)

class AlesticAmiScraper(Scraper):
  ALESTIC_URL = "http://old.alestic.com/"
  ALESTIC_AMI_PATTERN = "(\w+) (\d{2}.\d{2})\s?(LTS)? (\w+), (PV|HVM) (EBS-SSD boot)"
  ALESTIC_AMI_RE = re.compile(ALESTIC_AMI_PATTERN)

  def __init__(self):
    # Inherits from the generirc scraper class
    Scraper.__init__(self, AlesticAmiScraper.ALESTIC_URL)

  def parse_ami_info(self, rec, region):
    """ 
      Parse an AMI record and return an Ec2Ami object 
      if the record was parsable. One record should look like:

      - Ubuntu 14.04 LTS Trusty, PV EBS-SSD boot

      If the pattern is not found in the record SyntaxError exception 
      is thrown.
    """
    match = AlesticAmiScraper.ALESTIC_AMI_RE.match(rec)
    if match is not None:
      return Ec2Ami(id=None, 
        region=region,
        distribution=match.group(1),
        version=match.group(2), 
        is_lts=True if match.group(3) is not None else False,
        codename=match.group(4),
        virtualization_type=match.group(5), 
        root_device_type=match.group(6),
        architecture="amd64")
    else:
      raise SyntaxError("Could not parse the AMI record")

  def scrape(self):
    """ 
      Scrape method that will find out how to extract AMI information 
      from the http://alestic.com webpage.
      
      Returns an Ec2AmiCollection object which contains all
      amis scraped from the page.
    """
    ami_collection = Ec2AmiCollection()
    
    for region in self.soup.find_all('div', id=re.compile('^tab-')):
      # Extract the AWS region
      region_key = region.get('id')[4:]
      
      # Loop over AMIs from all regions
      for tr_record in region.find_all('tr'):
        # Build an empty object that will be completed after
        ami_obj = Ec2Ami()
        for td_record in tr_record.find_all('td'):
          # Description part of the AMI
          if td_record.get('class'):
            ami_obj = self.parse_ami_info(re.sub('\s+', ' ', td_record.get_text().replace('\n',',')), region_key)
          # AMI's Id
          else:
            ami_obj.id = td_record.get_text(strip=True)
        
        # Append to the list if the id was set
        if ami_obj.id:
          ami_collection.append(ami_obj)
        # Otherwise drop the object
        else: 
          del ami_obj

    return ami_collection
