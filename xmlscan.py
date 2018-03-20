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
        if asset.get('ReleaseType'):
            isBeta = True
        else:
            isBeta = False
        buildnum = asset['Build']
        builds.update({buildnum:{'Version':osversion,'Beta':isBeta}})

    return builds


def main():
    print "Fetching iOS Builds from %s" % ioscatalog
    ioscatbuilds = parse(ioscatalog)
    print "Fetching tvOS Builds from %s" % tvoscatalog
    tvoscatbuilds = parse(tvoscatalog)
    print "Fetching iOS Public Seed Builds from %s" % iospublicseed
    iospubbuilds = parse(iospublicseed)
    print "Fetching iOS 11 Public Seed Builds from %s" % ios11publicseed
    ioslatestpubbuilds = parse(ios11publicseed)
    print "Fetching tvOS 11 Public Seed Builds from %s" % tvos11publicseed
    tvoslatestpubbuilds = parse(tvos11publicseed)

    ioslatestpubbuilds.update(iospubbuilds)
    ioslatestpubbuilds.update(ioscatbuilds)

    tvoslatestpubbuilds.update(tvoscatbuilds)


    # Pretty print taken from Greg N installinstallmacos.py
    # https://github.com/munki/macadmin-scripts/blob/master/installinstallmacos.py
    print '\niOS:'
    print '%2s %8s %4s' % ('#', 'Build', 'Version')
    for index, build in enumerate(sorted(ioslatestpubbuilds)):
        print '%2s %8s %4s' % (index+1,
                                ioslatestpubbuilds[build]['Version'],
                                build)

    print '\ntvOS:'
    print '%2s %8s %4s' % ('#', 'Build', 'Version')
    for index, build in enumerate(sorted(tvoslatestpubbuilds)):
        print '%2s %8s %4s' % (index+1,
                                tvoslatestpubbuilds[build]['Version'],
                                build)

if __name__ == '__main__':
    main()
