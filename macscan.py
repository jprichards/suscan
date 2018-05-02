#!/usr/bin/python

from xml.dom import minidom
from xml.parsers.expat import ExpatError
import xml.etree.ElementTree as xml
import sys
import plistlib
import requests

macurls = ['https://swscan.apple.com/content/catalogs/others/index-10.13seed-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog',
           'https://swscan.apple.com/content/catalogs/others/index-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog',
           'https://swscan.apple.com/content/catalogs/others/index-10.13beta-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog',
           'https://swscan.apple.com/content/catalogs/others/index-10.13customerseed-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog']


# this func shamelessy stolen from Greg N as it is more elegant than my previous version (in suscan.py) :P
# https://github.com/munki/macadmin-scripts/blob/master/installinstallmacos.py
def auxparse(dist):
    '''Parses a softwareupdate dist file, returning a dict of info of
    interest'''
    dist_info = {}
    try:
        dom = minidom.parseString(dist)
    except ExpatError:
        print >> sys.stderr, 'Invalid XML in %s' % dist
        return dist_info
    except IOError, err:
        print >> sys.stderr, 'Error reading %s: %s' % (dist, err)
        return dist_info

    auxinfos = dom.getElementsByTagName('auxinfo')
    if not auxinfos:
        return dist_info
    auxinfo = auxinfos[0]
    key = None
    value = None
    children = auxinfo.childNodes
    # handle the possibility that keys from auxinfo may be nested
    # within a 'dict' element
    dict_nodes = [n for n in auxinfo.childNodes
                  if n.nodeType == n.ELEMENT_NODE and
                  n.tagName == 'dict']
    if dict_nodes:
        children = dict_nodes[0].childNodes
    for node in children:
        if node.nodeType == node.ELEMENT_NODE and node.tagName == 'key':
            key = node.firstChild.wholeText
        if node.nodeType == node.ELEMENT_NODE and node.tagName == 'string':
            value = node.firstChild.wholeText
        if key and value:
            dist_info[key] = value
            key = None
            value = None
    return dist_info


def easyparse(dist):
    root = xml.fromstring(dist)
    bundleid = None
    for r in root:
        try:
            if r.attrib['id'].startswith('com.apple.update.fullbundleupdate'):
                bundleid = r.attrib['id']
            elif r.attrib['id'].startswith('com.apple.pkg.update.os'):
                bundleid = r.attrib['id']
        except KeyError:
            continue
    if bundleid is not None:
        return bundleid.split('.')[-1]


def findeligible(plist):
    product_ids = []
    for product in plist['Products']:
        for info in plist['Products'][product]:
            if info == 'ExtendedMetaInfo':
                if product not in product_ids:
                    product_ids.append(product)
            elif info == 'State':
                if product not in product_ids:
                    product_ids.append(product)
    return product_ids


def main():
    results = {}
    for macurl in macurls:
        print '\nFetching macOS Builds from %s' % macurl
        r = requests.get(macurl)
        urlplist = plistlib.readPlistFromString(r.content)
        eligibleids = findeligible(urlplist)
        proper_dists = {}
        other_dists = {}
        for pid in eligibleids:
            for e in urlplist['Products'][pid].keys():
                if e == 'ExtendedMetaInfo':
                    for i in urlplist['Products'][pid]['ExtendedMetaInfo'].keys():
                        if i == 'ProductType':
                            if urlplist['Products'][pid]['ExtendedMetaInfo']['ProductType'] == 'macOS':
                                proper_dists[pid] = {'url' : urlplist['Products'][pid]['Distributions']['English'],
                                                     'date': str(urlplist['Products'][pid]['PostDate']),
                                                     'version': urlplist['Products'][pid]['ExtendedMetaInfo']['ProductVersion'],
                                                     'pid' : pid}
                        elif i == 'InstallAssistantPackageIdentifiers':
                            for o in urlplist['Products'][pid]['ExtendedMetaInfo']['InstallAssistantPackageIdentifiers'].keys():
                                if o == 'OSInstall':
                                    other_dists[pid] = {'url' : urlplist['Products'][pid]['Distributions']['English'],
                                                        'date': str(urlplist['Products'][pid]['PostDate']),
                                                        'pid' : pid}

        for p in proper_dists:
            r = requests.get(proper_dists[p]['url'])
            parsedbuild = easyparse(r.content)
            proper_dists[p]['build'] = parsedbuild
            if parsedbuild[-1].isdigit():
                proper_dists[p]['beta'] = False
            if parsedbuild[-1].isalpha():
                proper_dists[p]['beta'] = True
            proper_dists[p]['fullinstaller'] = False

        for o in other_dists:
            r = requests.get(other_dists[o]['url'])
            parsed = auxparse(r.content)
            other_dists[o]['build'] = parsed['BUILD']
            other_dists[o]['version'] = parsed['VERSION']
            if parsed['BUILD'][-1].isdigit():
                other_dists[o]['beta'] = False
            if parsed['BUILD'][-1].isalpha():
                other_dists[o]['beta'] = True
            other_dists[o]['fullinstaller'] = True

        results.update(proper_dists)
        results.update(other_dists)

    # Pretty print again taken from Greg N installinstallmacos.py
    print '%2s %12s %10s %9s %8s %8s %22s' % ('#', 'ProductID', 'Version',
                                     'Build', 'Beta', 'Full', 'Date')
    for index, product_id in enumerate(sorted(results)):
        print '%2s %12s %10s %9s %8s %8s %22s' % (index+1,
                                         product_id,
                                         results[product_id]['version'],
                                         results[product_id]['build'],
                                         results[product_id]['beta'],
                                         results[product_id]['fullinstaller'],
                                         results[product_id]['date'])



if __name__ == '__main__':
    main()
