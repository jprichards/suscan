# SUscan
Current for iOS 12, tvOS 12, and macOS 10.14

_macscan.py_ - Updated version with logic for Apple's confusing alternative dist files.
It will return all build numbers and product id's even if the same build number is found in multiple products. The 'Full' column specifies if the product id is for a full installer (rather than a stub installer) that can be used for VM's or bootable usb's.
```
usage: python macscan.py
```
```
 #    ProductID    Version     Build     Beta     Full                   Date
 1    041-03369      10.14   18A384a     True     True    2018-09-12 18:58:56
 2    041-03712      10.14    18A389    False    False    2018-09-12 18:53:39
 3    041-09593    10.14.2     18C54    False    False    2018-12-05 18:03:41
 4    041-18148    10.14.1   18B2107    False    False    2018-11-14 17:59:03
 5    041-19985    10.14.2     18C54    False     True    2018-12-05 18:04:13
 6    041-19988    10.14.2     18C54    False    False    2018-12-05 18:03:15
 7    041-20511    10.13.6   17G4015    False    False    2018-12-05 18:11:33
 8    041-26479    10.14.3    18D21c     True    False    2018-12-10 17:58:10
 9    041-26480    10.14.3    18D21c     True    False    2018-12-10 17:58:09
10    091-51300      10.13    17A501    False    False    2017-12-06 18:22:40
11    091-51303    10.13.1   17B1003    False    False    2017-12-06 18:23:10
12    091-52054    10.13.2     17C88    False    False    2017-12-13 18:02:30
13    091-52056    10.13.2     17C88    False    False    2017-12-13 18:02:17
14    091-62775    10.13.3   17D2047    False    False    2018-01-30 18:06:22
15    091-65648      10.14    18A389    False    False    2018-09-12 18:53:39
16    091-94326    10.13.6     17G65    False     True    2018-07-11 00:43:04
17    091-94329    10.13.6     17G65    False    False    2018-09-28 03:31:26
18    091-94330    10.13.6     17G65    False    False    2018-09-28 03:31:36
19    091-95774    10.13.6   17G2208    False     True    2018-07-30 23:56:03
20    091-97092    10.14.2     18C54    False    False    2018-12-05 18:02:00
21    091-97109    10.13.6   17G2307    False    False    2018-09-28 03:31:13
```

_xmlscan.py_ - Scans Apple update xml for iOS and tvOS builds
```
usage: python xmlscan.py
```
```
iOS:
 #        Build   Version     Beta
 1       10A444       6.0    False
 2       10B329     6.1.3    False
 3       10B500     6.1.6    False
 4       11D257     7.1.2    False
 5       11D258     7.1.2    False
 6       12H321     8.4.1    False
 7       12H606     8.4.2     True
 8        13G36     9.3.5    False
 9        14G60    10.3.3    False
10      14G6060    10.3.3     True
11      15G6077    11.4.1     True
12        15G77    11.4.1    False
13        16C50    12.1.1    False
14     16C5050a    12.1.1    False
15      16C6050    12.1.1     True
16     16D5024a    12.1.2    False
17       99Z999      11.4    False
18        9B206     5.1.1    False

tvOS:
 #      Build   Version
 1   15L5570a      11.4
 2      16K45    12.1.1
 3   16K5524a    12.1.2
 4    16K6045    12.1.1
 ```
