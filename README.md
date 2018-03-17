# SUscan

_macscan.py_ - Updated version with logic for Apple's confusing alternative dist files.
It will return all build numbers and product id's even if the same build number is found in multiple products
```
usage: python macscan.py
```
```
 #    ProductID    Version    Build  Beta
 1    091-31306      10.13  17A360a  True
 2    091-71617    10.13.3  17D2104  False
 3    091-62779    10.13.3  17D2047  False
 4    091-52054    10.13.2    17C88  False
 5    091-52056    10.13.2    17C88  False
 6    091-73168    10.13.4  17E182a  True
 7    091-62780    10.13.3    17D47  False
 8    091-73170    10.13.4  17E182a  True
 9    091-71284    10.13.4  17E160g  True
 ```





_suscan.py is now outdated:_

```
usage: suscan.py [-h] [-s] [-e]

Find & Extract Build Numbers from Apple sucatalogs

Full Run: python suscan.py -se

optional arguments:
  -h, --help  show this help message and exit
  -s          Save urls for dist files with auxinfo key to local json
  -e          Extract Build Number from files in local json
```
