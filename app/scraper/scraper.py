#!/usr/bin/env python
# -*- coding: utf-8 -*-

# General imports
import re
import time
import requests
from bs4 import BeautifulSoup

# App imports

from app.scraper.models import Ec2Ami, Ec2AmiCollection

# Logging
import logging
logger = logging.getLogger(__name__)

class Scraper(object):
  """
    Generic Scraper class.
  """
  def __init__(self, url):
    self._url = url
    self._soup = None
    self._last_request_time = 0

  # Getters / Setters
  @property
  def url(self):
    return self._url

  @url.setter
  def url(self, value):
    self._url = value

  @property
  def soup(self):
    return self._soup

  @soup.setter
  def soup(self, value):
    self._soup = value

  @property
  def last_request_time(self):
    return self._last_request_time

  @last_request_time.setter
  def last_request_time(self, value):
    self._last_request_time = int(value)

  def scrape(self):
    raise NotImplemented("Implement the scrape method...")

  def refresh(self):
    r = requests.get(self.url)
    if r.status_code == 200:
      logger.info("%s scraped succefully." % self.url)

      self.last_request_time = time.time()
      self.soup = BeautifulSoup(r.text)
