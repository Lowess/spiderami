#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify

class InvalidApiUsage(Exception):
  status_code = 500

  def __init__(self, message, status_code=None, payload=None):
    Exception.__init__(self)
    self.message = message
    if status_code is not None:
      self.status_code = status_code
      self.payload = payload

  def to_dict(self):
    rv = dict(self.payload or ())
    rv['message'] = self.message
    rv['error'] = self.status_code
    return rv