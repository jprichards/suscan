#!/usr/bin/python#!/usr/bin/python
import json
import plistlib
import requests

ioscatalog = 'http://mesu.apple.com/assets/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'
iospublicseed = 'http://mesu.apple.com/assets/iOSPublicSeed/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'
ios11publicseed = 'http://mesu.apple.com/assets/iOS11PublicSeed/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'
ios11devseed = 'https://mesu.apple.com/assets/iOS11DeveloperSeed/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'
tvoscatalog = 'http://mesu.apple.com/assets/tv/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'
tvos11publicseed = 'http://mesu.apple.com/assets/tvOS11PublicSeed/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'
tvos11devseed = 'https://mesu.apple.com/assets/tvOS11DeveloperSeed/com_apple_MobileAsset_SoftwareUpdate/com_apple_MobileAsset_SoftwareUpdate.xml'

def parse(catalog):
    builds = {}
    r = requests.get(catalog)
    rplist = plistlib.readPlistFromString(r.content)
    for asset in rplist['Assets']:
        sudocid = asset.get('SUDocumentationID')
        if asset['OSVersion'].startswith('9.9.'):
            osversion = asset['OSVersion'][4:]
        else:
            osversion = asset['OSVersion']
        if asset.get('ReleaseType'):
            isBeta = True
        elif asset.get('SUDocumentationID') == 'PreRelease':
            isBeta = True
        else:
            isBeta = False
        buildnum = asset['Build']
        builds.update({buildnum:{'Version':osversion,
                                 'Beta':isBeta,
                                 'SUDocumentationID':str(sudocid)
                                 }})


# SUDocumentationID
    return builds


def main():
    print "Fetching iOS Builds from %s" % ioscatalog
    ioscatbuilds = parse(ioscatalog)
    print "Fetching iOS Public Seed Builds from %s" % iospublicseed
    iospubbuilds = parse(iospublicseed)
    print "Fetching iOS 11 Public Seed Builds from %s" % ios11publicseed
    ioslatestpubbuilds = parse(ios11publicseed)
    print "Fetching iOS 11 Developer Seed Build from %s" % ios11devseed
    ioslatestdevbuilds = parse(ios11devseed)
    print "Fetching tvOS Builds from %s" % tvoscatalog
    tvoscatbuilds = parse(tvoscatalog)
    print "Fetching tvOS 11 Public Seed Builds from %s" % tvos11publicseed
    tvoslatestpubbuilds = parse(tvos11publicseed)
    print "Fetching tvOS 11 Developer Seed Builds from %s" % tvos11devseed
    tvoslatestdevbuilds = parse(tvos11devseed)

    ioslatestpubbuilds.update(iospubbuilds)
    ioslatestpubbuilds.update(ioscatbuilds)
    ioslatestpubbuilds.update(ioslatestdevbuilds)

    tvoslatestpubbuilds.update(tvoscatbuilds)
    tvoslatestpubbuilds.update(tvoslatestdevbuilds)

    # Pretty print taken from Greg N installinstallmacos.py
    # https://github.com/munki/macadmin-scripts/blob/master/installinstallmacos.py
    print '\niOS:'
    print '%2s %12s %9s %8s' % ('#', 'Build', 'Version', 'Beta')
    for index, build in enumerate(sorted(ioslatestpubbuilds)):
        print '%2s %12s %9s %8s' % (index+1,
                                    build,
                                    ioslatestpubbuilds[build]['Version'],
                                    ioslatestpubbuilds[build]['Beta'])


    print '\ntvOS:'
    print '%2s %10s %9s' % ('#', 'Build', 'Version')
    for index, build in enumerate(sorted(tvoslatestpubbuilds)):
        print '%2s %10s %9s' % (index+1,
                                build,
                                tvoslatestpubbuilds[build]['Version'])

if __name__ == '__main__':
    main()
