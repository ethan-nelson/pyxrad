# -*- coding: utf-8 -*-
# MIT License (c) 2017 Ethan Nelson

import os
import requests
import StringIO
import xml.etree.cElementTree as ElementTree


AWS_URL = "https://noaa-nexrad-level2.s3.amazonaws.com/"


def get_filenames(year, month, day, hour, site):
    url = "%s?prefix=%s/%s/%s/%s/%s%s%s%s_%s" % \
            (AWS_URL, year, month.zfill(2), day.zfill(2), site,
             site, year, month.zfill(2), day.zfill(2), hour.zfill(2))
    content = requests.get(url)
    content = StringIO.StringIO(content.content)

    return content


def parse_xml(content):
    e = ElementTree.parse(content)
    r = e.getroot()

    filenames = []
    for child in r:
        if child.tag[-8:] == 'Contents':
            for c in child:
                if c.tag[-3:] == 'Key':
                    filenames.append(c.text)

    return filenames

def get_files(filelist, save_path=''):
    files = []
    for filename in filelist:
        content = requests.get(AWS_URL + filename)
        c = content.content
        name = os.path.basename(filename)
        f = open(save_path + name,'w')
        f.write(c)
        f.close()
        files.append(save_path + name)

    return files


def example():
    xml = get_filenames('2017','06','06','06','KMKX')
    filenames = parse_xml(xml)
    files = get_files(filenames)
