#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
from datetime import datetime
import pandas as pd
import urlparse
import os
from urllib import urlretrieve
import string

letters = list(string.ascii_uppercase)
letters.append('1')

for letter in letters:
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    url = 'http://kassiesa.net/uefa/clubs/html/' + letter + '.html'
    req = urllib2.Request(url, None, headers)
    data = urllib2.urlopen(req).read()

    soup = BeautifulSoup(data,'lxml')

    for image in soup.findAll("img"):
        image_url = urlparse.urljoin(url, image['src'])
        filename = image["src"].split("/")[-1]
        if '%40' not in filename:
            outpath = os.path.join('./ClubLogos', filename)
            urlretrieve(image_url, outpath)