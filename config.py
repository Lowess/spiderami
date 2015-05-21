#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

##############################################################################
## Flask Configuration
##############################################################################

VERSION = "2.00"

# Set the server name
#SERVER_NAME = ''

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "aagoori#odeeRee9UCh%ee4aiThai)ng/ux7aes3ge9ve3eic4"

# Secret key for signing cookies
SECRET_KEY = "yeigang9EizeKaecei7cohw_aedeewiwe[chahj4iePh4aem"

JSONIFY_PRETTYPRINT_REGULAR = True

# WEB_RESOURCE = 'alestic'
WEB_RESOURCE = 'cloudimages'

# Cache timeout in seconds
CACHE_TIMEOUT = 3600
