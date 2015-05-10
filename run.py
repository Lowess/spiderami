#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import coloredlogs

logger = logging.getLogger(__name__)

from app import app

def main():
  app.run(host='0.0.0.0', port=8080, debug=True)

if __name__ == '__main__':
  # Initialize coloredlogs.
  coloredlogs.install(level=logging.DEBUG)  
  # Start the scraper
  main()
