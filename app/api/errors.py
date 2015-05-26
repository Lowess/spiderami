#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify

from app import app

class InvalidApiUsage(Exception):
  status_code = 500

  def __init__(self, message, status_code=None):
    Exception.__init__(self)
    self.message = message
    if status_code is not None:
      self.status_code = status_code

  def to_dict(self):
    rv = dict(message=self.message,
      code=self.status_code)
    return rv

  def to_json_response(self):
    response = jsonify(self.to_dict())
    response.status_code = self.status_code
    return response

@app.errorhandler(404)
@app.errorhandler(500)
def handle_not_found(error):
  api_error = InvalidApiUsage(message=error.description, 
    status_code=error.code)

  return api_error.to_json_response()

@app.errorhandler(InvalidApiUsage)
def handle_invalid_usage(error):
  return error.to_json_response()