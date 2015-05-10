#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

##############################################################################
## Flask Initialisation
##############################################################################

# Import flask
from flask import Blueprint, Flask, url_for, redirect

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Override with production settings
if "FLASK_ENV" in os.environ:
  app.config.from_object(os.environ["FLASK_ENV"])

##############################################################################
## Flask Blueprints registration
##############################################################################

# Import a modules / components using its blueprint handler variable
from app.api.ami.controllers import ami as ami_module

# Register blueprint(s)
app.register_blueprint(ami_module)

@app.route('/', methods=['GET'])
def index():
  return redirect(url_for('ami.index'))
