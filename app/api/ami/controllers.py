#!/usr/bin/env python
# -*- coding: utf-8 -*-

# General imports
import json
from flask import Blueprint, request, jsonify

# App scraper imports
from app import app
from app.scraper.controllers import AlesticAmiScraper

ami = Blueprint('ami', __name__, url_prefix="/ami")

# Logging
import logging
logger = logging.getLogger(__name__)

def request_alestic():
  # Init the Alestic Scraper
  aas = AlesticAmiScraper()
  # Scrape Alestic webpage
  return aas.scrape()

@ami.url_value_preprocessor
def pretty_json(endpoint, values):
  if 'pretty' in request.args.keys():
    app.config.update(JSONIFY_PRETTYPRINT_REGULAR = True)
  else:
    app.config.update(JSONIFY_PRETTYPRINT_REGULAR = False)

@ami.route('', methods=['GET'])
@ami.route('/', methods=['GET'])
def index():
  # Get updates from Alestic webpage
  ami_collection = request_alestic()
  # Filter results
  filtered_amis = ami_collection.find()
  # Return a Json response
  return jsonify(json.loads(filtered_amis.to_json()))

# Minimal endpoint ...
@ami.route('/<string:region>', methods=['GET'])
# @ami.route('/<string:region>/', methods=['GET'])
# ... codename filtering
@ami.route('/<string:region>/<string:codename>', methods=['GET'])
# @ami.route('/<string:region>/<string:codename>/', methods=['GET'])
@ami.route('/<string:region>/<string:codename>/hvm', defaults={'virtualization_type': 'HVM'}, methods=['GET'])
@ami.route('/<string:region>/<string:codename>/pv', defaults={'virtualization_type': 'PV'}, methods=['GET'])
# ... version filtering
@ami.route('/<string:region>/<float:version>', methods=['GET'])
# @ami.route('/<string:region>/<float:version>/', methods=['GET'])
@ami.route('/<string:region>/<float:version>/hvm', defaults={'virtualization_type': 'HVM'}, methods=['GET'])
@ami.route('/<string:region>/<float:version>/pv', defaults={'virtualization_type': 'PV'}, methods=['GET'])
# ... lts filtering
@ami.route('/<string:region>/lts', defaults={'is_lts': True}, methods=['GET'])
# @ami.route('/<string:region>/lts/', defaults={'is_lts': True}, methods=['GET'])
@ami.route('/<string:region>/lts/hvm', defaults={'is_lts': True, 'virtualization_type': 'HVM'}, methods=['GET'])
@ami.route('/<string:region>/lts/pv', defaults={'is_lts': True, 'virtualization_type': 'PV'}, methods=['GET'])
# ... virtualization type filtering
@ami.route('/<string:region>/hvm', defaults={'virtualization_type': 'HVM'}, methods=['GET'])
@ami.route('/<string:region>/pv', defaults={'virtualization_type': 'PV'}, methods=['GET'])
# ... latest version filtering
@ami.route('/<string:region>/latest', defaults={'latest': True}, methods=['GET'])
# @ami.route('/<string:region>/latest/', defaults={'latest': True}, methods=['GET'])
@ami.route('/<string:region>/latest/hvm', defaults={'latest': True, 'virtualization_type': 'HVM'}, methods=['GET'])
@ami.route('/<string:region>/latest/pv', defaults={'latest': True, 'virtualization_type': 'PV'}, methods=['GET'])
# ... latest lts version filtering
@ami.route('/<string:region>/latest/lts', defaults={'is_lts': True, 'latest': True}, methods=['GET'])
# @ami.route('/<string:region>/latest/lts/', defaults={'is_lts': True, 'latest': True}, methods=['GET'])
@ami.route('/<string:region>/latest/lts/hvm', defaults={'is_lts': True, 'latest': True, 'virtualization_type': 'HVM'}, methods=['GET'])
@ami.route('/<string:region>/latest/lts/pv', defaults={'is_lts': True, 'latest': True, 'virtualization_type': 'PV'}, methods=['GET'])

def ami_by_region_with_attr(region, distribution=None, codename=None, 
  version=None, is_lts=None, virtualization_type=None, latest=False):

  # Get updates from Alestic webpage
  ami_collection = request_alestic()
  
  # Filter results
  if latest:
    latest_version = ami_collection.latest_version(region=region,
      is_lts=is_lts)
    logger.debug("Latest endpoint call, only ami matching the version %s will be returned" % latest_version)

  filtered_amis = ami_collection.find(region=region,
    distribution=distribution,
    codename=codename,
    version=version if not latest else latest_version,
    is_lts= is_lts,
    virtualization_type=virtualization_type)

  # Sort results
  filtered_amis.sort_by(key="version", reverse=True)

  # Return a Json response
  return jsonify(json.loads(filtered_amis.to_json()))