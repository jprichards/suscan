# SUscan

_macscan.py_ - Updated version with logic for Apple's confusing alternative dist files.
It will return all build numbers and product id's even if the same build number is found in multiple products
```
usage: python macscan.py
```
```
#    ProductID    Version     Build     Beta     Full                   Date
1    091-31306      10.13   17A360a     True    False    2017-09-01 16:53:47
2    091-51300      10.13    17A501    False    False    2017-12-06 18:22:40
3    091-51303    10.13.1   17B1003    False    False    2017-12-06 18:23:10
4    091-52054    10.13.2     17C88    False    False    2017-12-13 18:02:30
5    091-52056    10.13.2     17C88    False    False    2017-12-13 18:02:17
6    091-62775    10.13.3   17D2047    False    False    2018-01-30 18:06:22
7    091-71284    10.13.4   17E160g     True     True    2018-02-23 17:58:51
8    091-76232    10.13.4    17E199    False    False    2018-04-05 17:00:07
9    091-76233    10.13.4    17E199    False     True    2018-03-29 23:09:25
10    091-76237    10.13.4    17E199    False    False    2018-04-05 17:00:07
11    091-80382    10.13.4    17E202    False    False    2018-05-01 17:02:45
12    091-81910    10.13.5    17F59b     True    False    2018-05-01 17:01:07
13    091-81913    10.13.5    17F59b     True    False    2018-05-01 17:01:44
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
11       15E302    11.3.1    False
12      15E6302    11.3.1     True
13     15F5061d      11.4    False
14     15F5061e      11.4    False
15        9B206     5.1.1    False

tvOS:
 #      Build   Version
 1     15L211      11.3
 2   15L5211b      11.3
 3   15L5560b      11.4
 4    15L6211      11.3
 ```






_suscan.py is now outdated and only up for archival purposes_
