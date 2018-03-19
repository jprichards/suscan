#!/usr/bin/python
import json
import plistlib
import requests

ioscatalog = 'http://mesu.apple.com/assets/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'
iospublicseed = 'http://mesu.apple.com/assets/iOSPublicSeed/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'
ios11publicseed = 'http://mesu.apple.com/assets/iOS11PublicSeed/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'
tvoscatalog = 'http://mesu.apple.com/assets/tv/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'
tvos11publicseed = 'http://mesu.apple.com/assets/tvOS11PublicSeed/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'

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
    print "Fetching iOS Public Seed Builds from %s" % iospublicseed
    print parse(iospublicseed) + '\n'
    print "Fetching iOS 11 Public Seed Builds from %s" % ios11publicseed
    print parse(ios11publicseed) + '\n'
    print "Fetching tvOS 11 Public Seed Builds from %s" % tvos11publicseed
    print parse(tvos11publicseed) + '\n'

if __name__ == '__main__':
    main()
