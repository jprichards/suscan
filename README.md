# SUscan

_macscan.py_ - Updated version with logic for Apple's confusing alternative dist files.
It will return all build numbers and product id's even if the same build number is found in multiple products
```
usage: python macscan.py
```
```
 #    ProductID    Version    Build  Beta
 1    091-31306      10.13  17A360a  True
 2    091-51300      10.13   17A501  False
 3    091-51303    10.13.1  17B1003  False
 4    091-52054    10.13.2    17C88  False
 5    091-52056    10.13.2    17C88  False
 6    091-62775    10.13.3  17D2047  False
 7    091-62779    10.13.3  17D2047  False
 8    091-62780    10.13.3    17D47  False
 9    091-62782    10.13.3    17D47  False
10    091-62783    10.13.3    17D47  False
11    091-69251    10.13.3   17D102  False
12    091-71284    10.13.4  17E160g  True
13    091-71617    10.13.3  17D2104  False
14    091-75268    10.13.4  17E190a  True
15    091-75269    10.13.4  17E190a  True
 ```

_xmlscan.py_ - Scans Apple update xml for iOS and tvOS builds
```
usage: python xmlscan.py
```







_suscan.py is now outdated:_
