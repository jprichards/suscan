# SUscan

_macbuildscan.py_ - Updated version with logic for Apple's confusing alternative dist files.
It will return all build numbers and product id's even if the same build number is found in multiple products
```
usage: python macbuildscan.py
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

Example Run:
```
15:59 jrichards @ suscan $  python suscan.py -se
Downloading https://swscan.apple.com/content/catalogs/others/index-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog
*** Found 525 English dist files ***
Downloading https://swscan.apple.com/content/catalogs/others/index-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog
*** Found 721 English dist files ***
Downloading https://swscan.apple.com/content/catalogs/others/index-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog
*** Found 985 English dist files ***
Downloading https://swscan.apple.com/content/catalogs/others/index-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog
*** Found 1315 English dist files ***
Downloading https://swscan.apple.com/content/catalogs/others/index-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog
*** Found 1318 English dist files ***
Downloading http://swscan.apple.com/content/catalogs/others/index-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog
*** Found 1460 English dist files ***
Downloading http://swscan.apple.com/content/catalogs/others/index-lion-snowleopard-leopard.merged-1.sucatalog
*** Found 1640 English dist files ***
Downloading http://swscan.apple.com/content/catalogs/others/index-leopard-snowleopard.merged-1.sucatalog
*** Found 1646 English dist files ***
Downloading http://swscan.apple.com/content/catalogs/others/index-leopard.merged-1.sucatalog
*** Found 1646 English dist files ***
Downloading http://swscan.apple.com/content/catalogs/index-1.sucatalog
*** Found 1646 English dist files ***
Downloading http://swscan.apple.com/content/catalogs/index.sucatalog
*** Found 1646 English dist files ***
Searching for auxinfo key in each dist file...
*** Found auxinfo for 091-52052 ***
*** Found auxinfo for 091-33271 ***
Writing matches to auxinfo.json file...
Complete
Reading from auxinfo.json file...
Extracting Build Info from each match...
[{'10.13.2': '17C2120'}, {'10.13.2': '17C88'}]
```
