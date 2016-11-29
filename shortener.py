#!/usr/bin/env python

import urllib.request
import urllib.parse
import json
import sys

import config

# List of constants.
API_URL = 'https://www.googleapis.com/urlshortener/v1/url'

# Shorten URL using Google's url-shortener API.
def shorten(url):
  # Prepare data to be POSTed to Google.
  json_post_data = json.dumps({'longUrl': url})

  # POST request to Google.
  req = urllib.request.Request(
    url = API_URL + "?key=" + config.API_KEY,
    data = json_post_data.encode('utf-8'),
    headers ={
      'Content-Type': 'application/json',
      'Content-Length': len(json_post_data)})
  
  # Read result from Google.
  with urllib.request.urlopen(req) as f:
    ret = f.read().decode('utf-8')

  # Shorten URL is inside property 'id'.
  return json.loads(ret)['id']

"""
Return **True** if *url* looks like a result of
the *shorten* function. Return **False** other way.
"""
def is_short(url):
    return url.startswith('http://goo.gl/')

# FIXME: Might need to be updated later using similar approach as in
# function shorten.  Right now, I don't have time and all I need is
# shortening which has been fixed.
# 
# by dragontortoise
def expand(url):
    """
    :url: short url to expand.
    :returns: string, full url.
    """
    return json.loads(urllib2.urlopen(\
        '{0}?key={1}&shortUrl={2}'.format(API_URL, config.API_KEY,
        url)).read())['longUrl']

if __name__ == "__main__":
    print(shorten(sys.argv[1]))
