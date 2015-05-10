#!/usr/bin/env python
# -*- coding: utf-8 -*-

# General imports
import json
import copy 

# Logging
import logging
logger = logging.getLogger(__name__)

class AlesticEc2Ami(object):
  """
    Object representation of alestic Ec2 AMI.
  """
  def __init__(self, id=None, region=None, distribution=None, version=None, 
    is_lts=False, codename=False, virtualization_type=None, 
    root_device_type=None):
    self._id = id
    self._region = region
    self._distribution = distribution
    self._version = version
    self._is_lts = is_lts
    self._codename = codename
    self._virtualization_type = virtualization_type
    self._root_device_type = root_device_type
  
  def __repr__(self):
    return "[%s] %s %s %s %s - %s %s" %(self.id,
      self.distribution,
      self.version,
      "LTS" if self.is_lts else "",
      self.codename,
      self.virtualization_type,
      self.root_device_type)
    # return self.to_json()

  def to_json(self):
    return json.dumps({"id": self.id, 
      "region": self.region, 
      "distribution": self.distribution,
      "version": self.version,
      "is_lts": self.is_lts,
      "codename": self.codename,
      "virtualization_type": self.virtualization_type,
      "root_device_type": self.root_device_type
    })

  # Getters / Setters
  @property
  def id(self):
    return self._id

  @id.setter
  def id(self, value):
    self._id = value

  @property
  def region(self):
    return self._region

  @region.setter
  def region(self, value):
    self._region = value

  @property
  def distribution(self):
    return self._distribution  

  @distribution.setter
  def distribution(self, value):
    self._distribution = value

  @property
  def version(self):
    return self._version
  
  @version.setter
  def version(self, value):
    self._version = value

  @property
  def is_lts(self):
    return self._is_lts
  
  @is_lts.setter
  def is_lts(self, value):
    self._is_lts = value

  @property
  def codename(self):
    return self._codename
  
  @codename.setter
  def codename(self, value):
    self._codename = value

  @property
  def virtualization_type(self):
    return self._virtualization_type
  
  @virtualization_type.setter
  def virtualization_type(self, value):
    self._virtualization_type = value

  @property
  def root_device_type(self):
    return self._root_device_type
  
  @root_device_type.setter
  def root_device_type(self, value):
    self._root_device_type = value

class AlesticEc2AmiCollection(list):
  """
    Smart container class for AlesticEc2Ami.
  """
  def __init__(self, value=[]):
    list.__init__(self, value)

  def __repr__(self):
    return "\n" + "\n".join([elt.__repr__() for elt in self])
      
  def to_json(self):
    return json.dumps({
      "amis": [json.loads(ami.to_json()) for ami in self]
    })

  def sort_by(self, key, reverse=False):
    self.sort(key=lambda x: getattr(x, key), reverse=reverse)

  def find(self, **kwargs):
    # Start with all amis and intersect the list with filters
    res = set(self)
    for key, val in kwargs.iteritems():
      try:
        if val is not None:
          res = res & self.filter_by(key, val)
        else:
          logger.warning("Skipping filter filter_by(%s,%s) because of None value..." % (key, val))
      except Exception, e: 
        logger.error("Skipping filter filter_by(%s,%s) which can not be found..." % (key, val))        
        logger.error(e)        
    return AlesticEc2AmiCollection(res)

  def filter_by(self, arg, value):
    logger.info("Applying filter_by_%s with value: %s" % (arg, value))
    f = set([a for a in self if str(getattr(a, arg)).lower() == str(value).lower()])
    return f