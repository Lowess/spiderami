#!/usr/bin/env python
# -*- coding: utf-8 -*-

# General imports
import json
import copy 

# Logging
import logging
logger = logging.getLogger(__name__)

class Ec2Ami(object):
  """
    Object representation of alestic Ec2 AMI.
  """
  def __init__(self, id=None, region=None, distribution=None, version=None, 
    is_lts=None, is_eol=None, is_devel=None, codename=False, virtualization_type=None, 
    root_device_type=None, architecture=None, release_date=None, aki_id=None):
    self._id = id
    self._region = region
    self._distribution = distribution
    self._version = version
    self._is_lts = is_lts
    self._is_eol = is_eol
    self._is_devel = is_devel
    self._codename = codename
    self._virtualization_type = virtualization_type
    self._root_device_type = root_device_type
    self._architecture = architecture
    self._release_date = release_date
    self._aki_id = aki_id
  
  def __repr__(self):
    return "[%s][%s] %s %s%s%s %s %s %s - %s %s %s %s" %(self.region,
      self.id,
      self.distribution,
      self.version,
      "LTS" if self.is_lts else "",
      "EOL" if self.is_eol else "",
      "DEVEL" if self.is_devel else "",
      self.codename,
      self.virtualization_type,
      self.root_device_type,
      self.release_date,
      self.architecture,
      self.aki_id)
    # return self.to_json()

  def to_json(self):
    return json.dumps({"id": self.id, 
      "region": self.region, 
      "distribution": self.distribution,
      "version": self.version,
      "is_lts": self.is_lts,
      "is_eol": self.is_eol,
      "is_devel": self.is_devel,
      "codename": self.codename,
      "virtualization_type": self.virtualization_type,
      "root_device_type": self.root_device_type,
      "architecture": self.architecture,
      "release_date": self.release_date,
      "aki_id": self.aki_id
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
  def is_eol(self):
    return self._is_eol
  
  @is_eol.setter
  def is_eol(self, value):
    self._is_eol = value

  @property
  def is_devel(self):
    return self._is_devel
  
  @is_devel.setter
  def is_devel(self, value):
    self._is_devel = value

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

  @property
  def architecture(self):
    return self._architecture
  
  @architecture.setter
  def architecture(self, value):
    self._architecture = value

  @property
  def release_date(self):
    return self._release_date
  
  @release_date.setter
  def release_date(self, value):
    self._release_date = value

  @property
  def aki_id(self):
    return self._aki_id
  
  @aki_id.setter
  def aki_id(self, value):
    self._aki_id = value

class Ec2AmiCollection(list):
  """
    Smart container class for Ec2Ami.
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
    self.sort(key=lambda x: getattr(x, key) + x.virtualization_type, reverse=reverse)
  
  def latest_version(self, **kwargs):
    res = set(self) 
    res = self.find(**kwargs)
    res_obj = Ec2AmiCollection(res)
    res_obj.sort_by('version', reverse=True)
    return res_obj[0].version

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
    return Ec2AmiCollection(res)

  def filter_by(self, arg, value):
    logger.info("Applying filter_by_%s with value: %s" % (arg, value))
    f = set([a for a in self if str(getattr(a, arg)).lower() == str(value).lower()])
    return f