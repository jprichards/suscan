#!/usr/bin/python
import json
import plistlib
import requests

ioscatalog = 'http://mesu.apple.com/assets/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'
tvoscatalog = 'http://mesu.apple.com/assets/tv/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'

def parse(catalog):
    builds = {}
    r = requests.get(catalog)
    rplist = plistlib.readPlistFromString(r.content)
    for asset in rplist['Assets']:
        if asset['OSVersion'].startswith('9.9.'):
            osversion = asset['OSVersion'][4:]
        else:
            osversion = asset['OSVersion']
        builds[asset['Build']] = osversion
    return json.dumps(builds, indent=1, sort_keys=True)


def main():
    print "Fetching iOS Builds from %s" % ioscatalog
    print parse(ioscatalog) + '\n'
    print "Fetching tvOS Builds from %s" % tvoscatalog
    print parse(tvoscatalog) + '\n'

if __name__ == '__main__':
    main()
