#!/usr/bin/python

# OUTDATED - USE MACSCAN.PY

import argparse
import datetime
import json
import plistlib
import requests
import xml.etree.ElementTree as xml

sucatalog = ['https://swscan.apple.com/content/catalogs/others/index-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog',
            'https://swscan.apple.com/content/catalogs/others/index-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog',
            'https://swscan.apple.com/content/catalogs/others/index-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog',
            'https://swscan.apple.com/content/catalogs/others/index-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog',
            'https://swscan.apple.com/content/catalogs/others/index-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog',
            'http://swscan.apple.com/content/catalogs/others/index-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog',
            'http://swscan.apple.com/content/catalogs/others/index-lion-snowleopard-leopard.merged-1.sucatalog',
            'http://swscan.apple.com/content/catalogs/others/index-leopard-snowleopard.merged-1.sucatalog',
            'http://swscan.apple.com/content/catalogs/others/index-leopard.merged-1.sucatalog',
            'http://swscan.apple.com/content/catalogs/index-1.sucatalog',
            'http://swscan.apple.com/content/catalogs/index.sucatalog']

def main():
    ap = argparse.ArgumentParser(description='Find & Extract Build Numbers from latest sucatalog updates')
    ap.add_argument('-s', action='store_true', help='Save urls for dist files with auxinfo key to local json')
    ap.add_argument('-e', action='store_true', help='Extract Build Number from files in local json')
    args = ap.parse_args()

    if args.s:
        urls = {}
        # Download each sucatalog and find all product-id's with Engish dist files
        for catalog in sucatalog:
            print 'Downloading %s' % catalog
            r = requests.get(catalog)
            rplist = plistlib.readPlistFromString(r.content)
            # Find all English dist file urls and map to their product-id in a dict
            for product in rplist['Products']:
                for content in rplist['Products'][product]:
                    try:
                        urls[str(product)] = {'url' : str(rplist['Products'][product]['Distributions']['English']),
                                              'date' : str(rplist['Products'][product]['PostDate'])}
                    except KeyError:
                        continue
            print '*** Found %s English dist files ***' % len(urls)

        matches = {}
        # Download each dist and search for 'auxinfo'
        print 'Searching for auxinfo key in each dist file...'
        for product in urls:
            r = requests.get(urls[product]['url'])
            if 'auxinfo' in str(r.content):
                print '*** Found auxinfo for %s ***' % product
                matches[str(product)] = urls[product]

        print 'Writing matches to auxinfo.json file...'
        with open('auxinfo.json', 'w') as auxfile:
            json.dump(matches, auxfile)
        print 'Complete'

    if args.e:
        product = {}
        print 'Reading from auxinfo.json file...'
        with open('auxinfo.json') as auxfile:
            product = json.load(auxfile)

        auxxmlstrings = []
        finalbuildlist = []
        print 'Extracting Build Info from each match...'
        for build in product:
            r = requests.get(product[build]['url']) # download dist file
            root = xml.fromstring(r.content) # parse XML from request content
            auxelem = root.getchildren()[6] # isolate 'auxinfo' XML element

            buildinfo = []
            # Depending on the update, it can be either be nested in a dict
            # or as direct child elements of 'auxinfo'
            if auxelem.getchildren()[0].tag == 'dict':
                for child in auxelem.getchildren()[0].getchildren():
                    if child.tag == 'string':
                        buildinfo.append(child.text)
            else:
                for child in auxelem.getchildren():
                    if child.tag == 'string':
                        buildinfo.append(child.text)

            # Build a list of dicts for each version and build number
            buildinfo.sort()
            finalbuildlist.append(dict([buildinfo]))

        print finalbuildlist

if __name__ == '__main__':
    main()
