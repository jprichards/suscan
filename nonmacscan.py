#!/usr/bin/python
import json
import os
import pandas as pd
import plistlib
import re
import requests
import sqlite3
import sys
import xml.etree.ElementTree as xml
from datetime import datetime
from xml.dom import minidom
from xml.parsers.expat import ExpatError


dir_path = os.path.dirname(os.path.realpath(__file__))

slack_webhook = 'https://hooks.slack.com/services/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' #Apple Build Numbers

ioscatalog = 'http://mesu.apple.com/assets/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'
iospublicseed = 'http://mesu.apple.com/assets/iOSPublicSeed/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'
ios11publicseed = 'http://mesu.apple.com/assets/iOS11PublicSeed/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'
tvoscatalog = 'http://mesu.apple.com/assets/tv/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'
tvos11publicseed = 'http://mesu.apple.com/assets/tvOS11PublicSeed/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'

def parse_productid(url):
    if url.endswith('/'):
        url = url[:-1]
    url = url.rsplit('/', 1)[1]
    regex = r"\A(?:[^-]+-??){2}"
    match = re.search(regex, url).group()
    return match

def parseios(catalog):
    # xmlinfo = {}
    builds = {}
    r = requests.get(catalog)
    rplist = plistlib.readPlistFromString(r.content)
    for asset in rplist['Assets']:
        # pid = parse_productid(asset['__BaseURL'])
        if asset['OSVersion'].startswith('9.9.'):
            osversion = asset['OSVersion'][4:]
        else:
            osversion = asset['OSVersion']
        builds[asset['Build']] = osversion
        # xmlinfo[pid] = builds
    # return xmlinfo
    return builds

def checkdb(build):
    conn = sqlite3.connect('buildcache.db')
    c = conn.cursor()
    bt = (build,)
    c.execute('SELECT * FROM builds WHERE build=?', bt)
    data = c.fetchall()
    if len(data)==0:
        return False
    else:
        return True
    conn.close()

def insertiostodb(buildsdict, platform, isbeta):
    for b, v in buildsdict.items():
        if checkdb(b):
            print '%s found in db, skipping...' % b
        else:
            #DB - (platform, osversion, build, beta, productid, date)
            #(platform, vers, build, beta)
            posttoslack(platform, v, b, isbeta)
            insertdb(platform, v, b, isbeta, 'XX-XXXX', timenow())

def insertdb(platform, osversion, build, beta, productid, date):
    conn = sqlite3.connect('buildcache.db')
    c = conn.cursor()
    buildinfo = (platform, osversion, build, beta, productid, date,)
    c.execute('INSERT INTO builds VALUES (?,?,?,?,?,?)', buildinfo)
    conn.commit()
    conn.close()

def timenow():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def posttoslack(platform, vers, build, beta):
    if beta == 'True':
        isbeta = 'Beta'
    else:
        isbeta = ''
    fulltext = 'New Build Version for %s %s %s - %s' % (platform, vers, isbeta, build)
    print fulltext
    titlejson = {'text':str(fulltext)}
    print 'posting to Slack...'
    # r = requests.post(slack_webhook, headers={'Content-Type': 'application/json'}, json=titlejson)
    # print r.text

def main():
    print '\nFetching iOS Builds from %s' % ioscatalog
    iosprodbuilds = parseios(ioscatalog)
    insertiostodb(iosprodbuilds, 'iOS', 'False')
    print '\nFetching tvOS Builds from %s'% tvoscatalog
    tvosprodbuilds = parseios(tvoscatalog)
    insertiostodb(tvosprodbuilds, 'tvOS', 'False')
    print '\nFetching iOS Public Seed Builds from %s' % iospublicseed
    iospubseedbuilds = parseios(iospublicseed)
    insertiostodb(iospubseedbuilds, 'iOS', 'True')
    print '\nFetching iOS 11 Public Seed Builds from %s' % ios11publicseed
    ios11pubseedbuilds = parseios(ios11publicseed)
    insertiostodb(ios11pubseedbuilds, 'iOS', 'True')
    print '\nFetching tvOS 11 Public Seed Builds from %s'% tvos11publicseed
    tvos11pubseedbuilds = parseios(tvos11publicseed)
    insertiostodb(tvos11pubseedbuilds, 'tvOS', 'True')
    print

    conn = sqlite3.connect('buildcache.db')
    c = conn.cursor()
    print pd.read_sql_query('SELECT * FROM builds ORDER BY date DESC', conn)
    conn.close()
    print


if __name__ == '__main__':
    if not os.path.exists(os.path.join(dir_path, 'buildcache.db')):
        print 'DB file not found, creating...'
        conn = sqlite3.connect('buildcache.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE builds(platform, osversion, build, beta, productid, date)''')
        conn.commit()
        conn.close()
        main()
    else:
        main()
