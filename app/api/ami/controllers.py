#!/usr/bin/env python
# -*- coding: utf-8 -*-

# General imports
import json
import time
from flask import Blueprint, request, jsonify

# App scraper imports
from app import app, scraper
from app.scraper.alestic_ami_scraper import AlesticAmiScraper
from app.scraper.cloud_images_scraper import CloudImagesScraper

# Api Errors handlers
from app.api.ami.errors import InvalidApiUsage

ami = Blueprint('ami', __name__, url_prefix="/ami")

# Logging
import logging
logger = logging.getLogger(__name__)


@app.errorhandler(InvalidApiUsage)
def handle_invalid_usage(error):
  response = jsonify(error.to_dict())
  response.status_code = error.status_code
  return response


def crawl():
  current_time = int(time.time())
  expired_time = scraper.last_request_time + int(app.config['CACHE_TIMEOUT'])

  # Check if the soup needs to be refreshed or initialized
  if scraper.soup is None or current_time > expired_time:
    logger.debug("current time is %s and has expired the period %s, refreshing page." %(current_time, expired_time))
    scraper.refresh()
  else:
    logger.debug("using cache as time is %s has not expired the period %s." %(current_time, expired_time))

  return scraper.scrape()

@ami.url_value_preprocessor
def pretty_json(endpoint, values):
  if 'pretty' in request.args.keys():
    app.config.update(JSONIFY_PRETTYPRINT_REGULAR = True)
  else:
    app.config.update(JSONIFY_PRETTYPRINT_REGULAR = False)

@ami.route('', methods=['GET', 'POST'])
def search_ami():
  # Get updates from Alestic webpage
  ami_collection = crawl()

  # Filter results
  filters = dict()

  if request.method == 'POST':
    filters = request.get_json()
  else:
    filters = request.args.to_dict()
    if 'pretty' in filters.keys():
      del filters['pretty']
  
  if filters:
    filtered_amis = ami_collection.find(**filters)
  else:
    filtered_amis = ami_collection
    
  # Sort the result
  filtered_amis.sort_by(key="version", reverse=True)

  # Return a Json response
  json_res = json.loads(filtered_amis.to_json())
  json_res['hits'] = len(filtered_amis)
  return jsonify(json_res)

@ami.route('/latest', methods=['GET', 'POST'])
@ami.route('/latest-lts', defaults={'is_lts': True}, methods=['GET', 'POST'])
def latest_ami(is_lts=None):
# Get updates from Alestic webpage
  ami_collection = crawl()

  # Filter results
  filters = dict()
  if request.method == 'POST':
      request.get_json()
  else:
    filters = request.args.to_dict()
    if 'pretty' in filters.keys():
      del filters['pretty']

  # Override parameters to make sure it matches latest critria
  filters['version'] = ami_collection.latest_version(is_lts=is_lts)
  if is_lts:
    filters['is_lts'] = is_lts
  
  filtered_amis = ami_collection.find(**filters)
  
  # Sort the result
  filtered_amis.sort_by(key="version", reverse=True)

  # Return a Json response
  json_res = json.loads(filtered_amis.to_json())
  json_res['hits'] = len(filtered_amis)
  return jsonify(json_res)